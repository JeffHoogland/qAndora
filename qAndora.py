import sys
import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_qAndora import Ui_qAndora
from ui_qLogin import Ui_qLogin

import playerVLC
import tempfile
import urllib

tempdir = tempfile.gettempdir()

#print "Current tmp directory is %s"%tempdir

class MainWindow(QMainWindow, Ui_qAndora):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignButtons()
        
        self.radioPlayer = playerVLC.volcanoPlayer()
        
        self.loginWin = LoginWindow( self )
        
        #Read login information
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/userinfo"%home):
            f = open('%s/.config/qAndora/userinfo'%home, 'r')
            lines = f.readlines()
            self.loginUser(lines[0].rstrip("\n"), lines[1].rstrip("\n"))
        else:
            self.loginWin.show()
    
    def loginUser( self, userName, userPassword ):
        self.radioPlayer.auth( userName, userPassword )
        
        lines = []
        
        #Get last used station
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/stationinfo"%home):
            f = open('%s/.config/qAndora/stationinfo'%home, 'r')
            lines = f.readlines()
            #print "Last station: %s"%lines[0]
            self.radioPlayer.setStation(self.radioPlayer.getStationFromName(lines[0].rstrip("\n")))
        else:
            self.radioPlayer.setStation(self.radioPlayer.getStations()[0])
        
        self.radioPlayer.setChangeCallBack( self.songChangeQ )
        self.radioPlayer.addSongs()
        
        stations = self.radioPlayer.getStations()
        stationlist = []
        for station in stations:
            self.stationBox.addItem(station['stationName'])
            stationlist.append(station['stationName'])
        
        if len(lines):
            self.stationBox.setCurrentIndex(stationlist.index(lines[0].rstrip("\n")))
        
        #Hook to read when the box changes
        self.stationBox.activated[str].connect(self.stationChange)
        
        self.show()
        
    def stationChange( self, newStation ):
        self.radioPlayer.setStation(self.radioPlayer.getStationFromName(newStation))
        
        home = os.path.expanduser("~")
        if not os.path.exists("%s/.config/qAndora"%home):
            os.makedirs("%s/.config/qAndora"%home)
        if os.path.exists("%s/.config/qAndora/stationinfo"%home):
            os.remove('%s/.config/qAndora/stationinfo'%home)
        f = open('%s/.config/qAndora/stationinfo'%home, 'w')
        f.write('%s\n'%newStation)
        f.close()
        self.radioPlayer.pauseSong()
        self.radioPlayer.clearSongs()
        self.radioPlayer.addSongs()
        
    def assignButtons( self ):
        self.playPauseButton.setIcon(QIcon("images/pause.png"))
        self.playPauseButton.clicked.connect(self.playPausePressed)
        self.skipButton.setIcon(QIcon("images/skip.png"))
        self.skipButton.clicked.connect(self.skipPressed)
        self.loveButton.setIcon(QIcon("images/favorite.png"))
        self.loveButton.clicked.connect(self.lovePressed)
        self.banButton.setIcon(QIcon("images/ban.png"))
        self.banButton.clicked.connect(self.banPressed)
        
    def songChangeQ( self ):
        invoke_in_main_thread(self.songChange)
    
    def songChange( self ):
        #print "Song changed"
        info = self.radioPlayer.songinfo[self.radioPlayer.curSong]
        self.titleLabel.setText('<b>Song:</b> <a href="%s">%s</a>'%(info['object'].songDetailURL, info['title']))
        self.albumLabel.setText('<b>Album:</b> <a href="%s">%s</a>'%(info['object'].albumDetailURL, info['album']))
        self.artistLabel.setText("<b>Artist:</b> %s"%info['artist'])
        if info['rating'] == "love":
            self.loveButton.setIcon(QIcon("images/love.png"))
            self.loveButton.setToolTip(QApplication.translate("qAndora", "Favorited", None, QApplication.UnicodeUTF8))
        else:
            self.loveButton.setIcon(QIcon("images/favorite.png"))
            self.loveButton.setToolTip(QApplication.translate("qAndora", "Mark Favorite", None, QApplication.UnicodeUTF8))
            
        '''try:
            os.remove(os.path.join(tempdir, 'albumart.png'))
        except:
            pass'''
        urllib.urlretrieve(str(info['thumbnail']), os.path.join(tempdir, 'albumart.jpg'))
        
        albumart = QPixmap(os.path.join(tempdir, 'albumart.jpg'))
        #print os.path.join(tempdir, 'albumart.jpg')
        #print albumart.isNull()
        self.albumImage.setPixmap(albumart)
        #print self.albumImage.pixmap()
        
    def playPausePressed( self ):
        if self.radioPlayer.playing:
            self.radioPlayer.pauseSong()
            self.playPauseButton.setIcon(QIcon("images/play.png"))
            self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Play", None, QApplication.UnicodeUTF8))
        else:
            self.radioPlayer.playSong()
            self.playPauseButton.setIcon(QIcon("images/pause.png"))
            self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Pause", None, QApplication.UnicodeUTF8))
    
    def skipPressed( self ):
        self.radioPlayer.skipSong()
    
    def lovePressed( self ):
        self.radioPlayer.loveSong()
        self.loveButton.setIcon(QIcon("images/love.png"))
        self.loveButton.setToolTip(QApplication.translate("qAndora", "Favorited", None, QApplication.UnicodeUTF8))
        
    def banPressed( self ):
        self.radioPlayer.banSong()
        
class LoginWindow(QDialog, Ui_qLogin):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignButtons()
        
        self.rent = parent
        
    def assignButtons( self ):
        self.loginButton.clicked.connect(self.loginPressed)
        
    def loginPressed( self ):
        home = os.path.expanduser("~")
        if not os.path.exists("%s/.config/qAndora"%home):
            os.makedirs("%s/.config/qAndora"%home)
        f = open('%s/.config/qAndora/userinfo'%home, 'w')
        f.write('%s\n'%self.nameEdit.text())
        f.write('%s\n'%self.passwordEdit.text())
        f.close()
        self.hide()
        self.rent.loginUser( self.nameEdit.text(), self.passwordEdit.text() )
        
"""Code from stack overflow to add events to the GUI thread from VLC backend

http://stackoverflow.com/questions/10991991/pyside-easier-way-of-updating-gui-from-another-thread"""
from Queue import Queue

class Invoker(QObject):
    def __init__(self):
        super(Invoker, self).__init__()
        self.queue = Queue()

    def invoke(self, func, *args):
        f = lambda: func(*args)
        self.queue.put(f)
        QMetaObject.invokeMethod(self, "handler", Qt.QueuedConnection)

    @Slot()
    def handler(self):
        f = self.queue.get()
        f()
invoker = Invoker()

def invoke_in_main_thread(func, *args):
    invoker.invoke(func,*args)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    #mainWin.show()
    sys.exit( app.exec_() )
