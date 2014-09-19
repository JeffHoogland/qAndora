import sys
import os

from PySide.QtGui import *
from PySide import QtCore

from ui_qAndora import Ui_qAndora

import playerVLC
import tempfile
import urllib

tempdir = tempfile.gettempdir()

print "Current tmp directory is %s"%tempdir

class MainWindow(QMainWindow, Ui_qAndora):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignButtons()
        
        self.radioPlayer = playerVLC.volcanoPlayer()
        
        #Read login information
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/userinfo"%home):
            f = open('%s/.config/qAndora/userinfo'%home, 'r')
            lines = f.readlines()
            self.radioPlayer.auth(lines[0].rstrip("\n"), lines[1].rstrip("\n"))
        else:
            #TODO: write login screen
            pass
            
        #Set default station
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/stationinfo"%home):
            f = open('%s/.config/qAndora/stationinfo'%home, 'r')
            lines = f.readlines()
            self.radioPlayer.setStation(self.radioPlayer.getStationFromName(lines[0].rstrip("\n")))
        else:
            self.radioPlayer.setStation(self.radioPlayer.getStations()[0])
        
        self.radioPlayer.setChangeCallBack( self.songChangeQ )
        self.radioPlayer.addSongs()
        
        stations = self.radioPlayer.getStations()
        
        for station in stations:
            self.stationBox.addItem(station['stationName'])
            #print station['stationName']
            
        #Hook to read when the box changes
        self.stationBox.activated[str].connect(self.stationChange)
        
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
        invoke_in_main_thread(self.songChange())
    
    def songChange( self ):
        print "Song changed"
        info = self.radioPlayer.songinfo[self.radioPlayer.curSong]
        self.titleLabel.setText(info['title'])
        self.albumLabel.setText(info['album'])
        if info['rating'] == "love":
            self.loveButton.setIcon(QIcon("images/love.png"))
        else:
            self.loveButton.setIcon(QIcon("images/favorite.png"))
            
        '''try:
            os.remove(os.path.join(tempdir, 'albumart.png'))
        except:
            pass'''
        urllib.urlretrieve(str(info['thumbnail']), os.path.join(tempdir, 'albumart.jpg'))
        
        albumart = QPixmap(os.path.join(tempdir, 'albumart.jpg'))
        print os.path.join(tempdir, 'albumart.jpg')
        print albumart.isNull()
        self.albumImage.setPixmap(albumart)
        print self.albumImage.pixmap()
        
    def playPausePressed( self ):
        if self.radioPlayer.playing:
            self.radioPlayer.pauseSong()
            self.playPauseButton.setIcon(QIcon("images/play.png"))
        else:
            self.radioPlayer.playSong()
            self.playPauseButton.setIcon(QIcon("images/pause.png"))
    
    def skipPressed( self ):
        self.radioPlayer.skipSong()
    
    def lovePressed( self ):
        self.radioPlayer.loveSong()
        self.loveButton.setIcon(QIcon("images/love.png"))
        
    def banPressed( self ):
        self.radioPlayer.banSong()
        
"""Code from stack overflow to add events to the GUI thread from VLC backend

http://stackoverflow.com/questions/10991991/pyside-easier-way-of-updating-gui-from-another-thread"""
class InvokeEvent(QtCore.QEvent):
    EVENT_TYPE = QtCore.QEvent.Type(QtCore.QEvent.registerEventType())

    def __init__(self, fn, *args, **kwargs):
        QtCore.QEvent.__init__(self, InvokeEvent.EVENT_TYPE)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs


class Invoker(QtCore.QObject):
    def event(self, event):
        #event.fn(*event.args, **event.kwargs)

        return True

_invoker = Invoker()


def invoke_in_main_thread(fn, *args, **kwargs):
    QtCore.QCoreApplication.postEvent(_invoker,
        InvokeEvent(fn, *args, **kwargs))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit( app.exec_() )
