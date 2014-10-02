import sys
import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_qAndora import Ui_MainWindow
from ui_qLogin import Ui_qLogin
from ui_qPreferences import Ui_qPreferences

from playerVLC import volcanoPlayer
import tempfile
import urllib
import webbrowser
import datetime
import cPickle as pickle

tempdir = tempfile.gettempdir()

#print "Current tmp directory is %s"%tempdir

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        
        self.radioPlayer = volcanoPlayer()
        
        self.loginWin = LoginWindow( self )
        self.preferencesWin = PreferencesWindow( self )
        
        #Read in stored preferences
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/preferences.cfg"%home):
            self.preferences = pickle.load( open( "%s/.config/qAndora/preferences.cfg"%home, "rb" ) )
            self.loginUser(self.preferences['username'], self.preferences['password'])
        else:
            self.preferences = {    "username":"",
                                    "password":"",
                                    "quality":"medium",
                                    "notifications":"Yes",
                                    "station":None,
                                    "volume":75}
            self.loginWin.show()
            
        self.radioPlayer.setVolume( self.preferences['volume'] )
        self.volumeSlider.setValue( self.preferences['volume'] )
            
    def savePreferences( self ):
        home = os.path.expanduser("~")
        if not os.path.exists("%s/.config/qAndora"%home):
            os.makedirs("%s/.config/qAndora"%home)
        pickle.dump( self.preferences, open( "%s/.config/qAndora/preferences.cfg"%home, "wb" ))
    
    def loginUser( self, userName, userPassword ):
        self.preferences['username'] = userName
        self.preferences['password'] = userPassword
        self.savePreferences()
        
        self.radioPlayer.auth( userName, userPassword )
        
        #Get last used station
        if self.preferences['station']:
            self.radioPlayer.setStation(self.radioPlayer.getStationFromName(self.preferences['station']))
        else:
            self.radioPlayer.setStation(self.radioPlayer.getStations()[0])
            self.preferences['station'] = self.radioPlayer.getStations()[0]['stationName']
        
        self.radioPlayer.setChangeCallBack( self.songChangeQ )
        self.radioPlayer.addSongs()
        
        stations = self.radioPlayer.getStations()
        stationlist = []
        for station in stations:
            self.stationBox.addItem(station['stationName'])
            stationlist.append(station['stationName'])
        
        self.stationBox.setCurrentIndex(stationlist.index(self.preferences['station']))
        
        #Hook to read when the box changes
        self.stationBox.activated[str].connect(self.stationChange)
        
        #Start a loop for updating current track time
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.timerTick)
        self.timer.start(250)
        
        self.show()
        
    def timerTick( self ):
        pos = self.radioPlayer.player.get_time() / 1000.0

        pos = str(datetime.timedelta(seconds=int(pos)))
        dur = str(datetime.timedelta(seconds=int(self.radioPlayer.player.get_length() / 1000.0)))
        
        posh, posm, poss = pos.split(":")
        durh, durm, durs = dur.split(":")
        
        pos = "%s:%s"%(posm, poss)
        dur = "%s:%s"%(durm, durs)
        
        t = "<b>%s  /  %s</b>" % (pos, dur)
        self.positionLabel.setText(t)
        
    def stationChange( self, newStation ):
        self.radioPlayer.setStation(self.radioPlayer.getStationFromName(newStation))
        
        self.preferences['station'] = newStation
        self.savePreferences()
        self.radioPlayer.pauseSong()
        self.radioPlayer.clearSongs()
        self.radioPlayer.addSongs()
        
    def assignWidgets( self ):
        self.playPauseButton.clicked.connect(self.playPausePressed)
        self.skipButton.clicked.connect(self.skipPressed)
        self.loveButton.clicked.connect(self.lovePressed)
        self.banButton.clicked.connect(self.banPressed)
        self.settingsButton.clicked.connect(self.settingsPressed)
        self.volumeSlider.valueChanged.connect(self.volumeChange)
        
    def volumeChange( self, val ):
        #print("New audio value is %s"%val)
        self.preferences['volume'] = val
        self.radioPlayer.setVolume( val )
        self.savePreferences()
        
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
            
        urllib.urlretrieve(str(info['thumbnail']), os.path.join(tempdir, 'albumart.jpg'))
        
        albumart = QPixmap(os.path.join(tempdir, 'albumart.jpg'))
        self.albumImage.setPixmap(albumart)
        
    def settingsPressed( self ):
        self.preferencesWin.show()
        
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
        self.radioPlayer.skipSong()

class PreferencesWindow(QDialog, Ui_qPreferences):
    def __init__(self, parent=None):
        super(PreferencesWindow, self).__init__(parent)
        self.setupUi(self)

class LoginWindow(QDialog, Ui_qLogin):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignButtons()
        
        self.rent = parent
        
    def assignButtons( self ):
        self.loginButton.clicked.connect(self.loginPressed)
        self.accountButton.clicked.connect(self.accountPressed)
        
    def loginPressed( self ):
        self.hide()
        self.rent.loginUser( self.nameEdit.text(), self.passwordEdit.text() )
        
    def accountPressed( self ):
        openBrowser("http://www.pandora.com")
        
def openBrowser(url):
    print("Opening %s"%url)
    webbrowser.open(url)
    try:
        os.wait() # workaround for http://bugs.python.org/issue5993
    except:
        pass
"""Code from stack overflow to add events to the GUI thread from VLC backend

http://stackoverflow.com/questions/10991991/pyside-easier-way-of-updating-gui-from-another-thread"""
import Queue

class Invoker(QObject):
    def __init__(self):
        super(Invoker, self).__init__()
        self.queue = Queue.Queue()

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
