import sys
import os
import platform
from PySide.QtGui import *
from PySide.QtCore import *
if not "arm" in platform.machine():
    from ui_qAndora import Ui_MainWindow
else:
    from ui_qAndora_mobile import Ui_MainWindow

from ui_qPreferences import Ui_qPreferences
from ui_qError import Ui_qError
from playerVLC import volcanoPlayer
import tempfile
import urllib
import webbrowser
import datetime
import cPickle as pickle
import time
        
try:
    import pynotify
    pynotify.init("Song Changed")
    notiLoaded = True
except:
    notiLoaded = False
    
tempdir = tempfile.gettempdir()

APP_ID = 'qAndora'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        icon = QIcon()
        icon.addPixmap(QPixmap("images/qAndora.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.isVisible = True
        self.muted = None
        self.notGotSongDuration = True
        self.albumart = None
        self.radioPlayer = volcanoPlayer()
        self.menu = QMenu()
        self.ErrorWin = ErrorWindow(self)
        self.assignWidgets()
        self.sysTrayIcon()
        ourUser = self.readPreferences()
        self.preferencesWin = PreferencesWindow(self)
        if ourUser == "new user":
            self.preferencesWin.show()
        else:
            self.show()
            self.tray.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.viewToggle.setText("Show qAndora")
        self.isVisible = False
        
    def viewTogglePressed(self):
        if self.isVisible:
            self.viewToggle.setText("Show qAndora")
            self.hide()
        else:
            self.viewToggle.setText("Hide qAndora")
            self.show()
        
        self.isVisible = not self.isVisible
    
    def sysTrayIcon(self):
        icon = QIcon("images/qAndora.png")
        
        self.songHeader = self.menu.addAction("Song Title")
        self.songHeader.setIcon(QIcon("images/albumart"))
        self.songHeader.triggered.connect(self.infoPressed)
        
        self.viewToggle = self.menu.addAction("Hide qAndora")
        self.viewToggle.triggered.connect(self.viewTogglePressed)
        
        self.playPauseAction = self.menu.addAction("Pause")
        self.playPauseAction.setIcon(QIcon.fromTheme("media-playback-pause", QIcon("images/pause.png")))
        self.playPauseAction.triggered.connect(self.playPausePressed)
        
        skipTrackAction = self.menu.addAction("Skip")
        skipTrackAction.triggered.connect(self.skipPressed)
        skipTrackAction.setIcon(QIcon.fromTheme("media-skip-forward", QIcon("images/skip.png")))

        self.loveAction = self.menu.addAction("Love this Song")
        self.loveAction.triggered.connect(self.lovePressed)
        self.loveAction.setIcon(QIcon.fromTheme("favorites", QIcon("images/favorite.png")))
        
        banAction = self.menu.addAction("Ban this Song")
        banAction.triggered.connect(self.banPressed)
        banAction.setIcon(QIcon.fromTheme("edit-delete", QIcon("images/ban.png")))
        
        tiredAction = self.menu.addAction("Tired of this Song")
        tiredAction.triggered.connect(self.tiredPressed)
        tiredAction.setIcon(QIcon.fromTheme("edit-redo", QIcon("images/tired.png")))
        
        exitAction = self.menu.addAction("Quit")
        exitAction.triggered.connect(self.exitPressed)
        exitAction.setIcon(QIcon.fromTheme("application-exit", QIcon("images/exit.png")))
        
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(self.menu)
        self.tray.activated.connect(self.trayClicked)
        
    def trayClicked(self, reason):
        if reason == self.tray.Trigger:
            if self.isVisible:
                self.hide()
                self.isVisible = False
                self.viewToggle.setText("Show qAndora")
            else:
                invoke_in_main_thread(self.updateSongTimeText)
                self.show()
                self.isVisible = True
                self.viewToggle.setText("Hide qAndora")
                
    def readPreferences(self):
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/preferences.cfg"%home):
            self.preferences = pickle.load( open( "%s/.config/qAndora/preferences.cfg"%home, "rb" ) )
            if self.preferences['username']:
                self.loginUser(self.preferences['username'], self.preferences['password'])
                return "existing user"
            else:
                return "new user"
        else:
            self.defaultPreferences()
            return "new user"
    
    def assignShortcuts(self):
        self.playPauseShortcut = QShortcut(QKeySequence(Qt.Key_Space), self)
        self.playPauseShortcut.setContext(Qt.ApplicationShortcut)
        self.playPauseShortcut.activated.connect(self.playPausePressed)
        
    def defaultPreferences( self ):
        self.preferences = {    "username":"",
                                    "password":"",
                                    "quality":"Medium",
                                    "notifications":"Yes",
                                    "station":None,
                                    "volume":75,
                                    "skiplive":False,
                                    "skipremix":False,
                                    "skipedit":False,
                                    "banskips":False}
        self.savePreferences()
            
    def savePreferences(self):
        home = os.path.expanduser("~")
        if not os.path.exists("%s/.config/qAndora"%home):
            os.makedirs("%s/.config/qAndora"%home)
        pickle.dump(self.preferences, open( "%s/.config/qAndora/preferences.cfg"%home, "wb"))
    
    def loginUser(self, userName, userPassword):
        self.preferences['username'] = userName
        self.preferences['password'] = userPassword
        self.savePreferences()
        
        self.radioPlayer.setVolume(self.preferences['volume'])
        self.volumeSlider.setValue(self.preferences['volume'])

        try:
            self.radioPlayer.auth(userName, userPassword)
            self.getLastStation()
            self.show()
            self.tray.show()
        except:
            self.preferencesWin.show()
            
    def getLastStation(self):
        if self.preferences['station']:
            self.radioPlayer.setStation(self.radioPlayer.getStationFromName(self.preferences['station']))
        else:
            self.radioPlayer.setStation(self.radioPlayer.getStations()[0])
            self.preferences['station'] = self.radioPlayer.getStations()[0]['stationName']
        
        try:
            self.radioPlayer.addSongs()
        except:
            self.ErrorWin.show()
            
        stations = self.radioPlayer.getStations()
        stationlist = []
        #Clear existing stations in case we are relogging
        self.stationBox.clear()
        for station in stations:
            self.stationBox.addItem(station['stationName'])
            stationlist.append(station['stationName'])
        
        self.stationBox.setCurrentIndex(stationlist.index(self.preferences['station']))
        
    def qTimer(self):        
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.updateSongTimeText)
        self.timer.start(1000)
                
    def updateSongTimeText(self):
        if self.isVisible:
            self.getSongDuration()
            self.getSongPostion()
            time = '%s / %s' %(self.songPos, self.songDur)
            self.positionLabel.setText(time)

    def formatTime(self, timeInt):
        timeInt = timeInt // 1000
        s = timeInt % 60
        timeInt //= 60
        m = timeInt % 60
        
        return "%02i:%02i"%(m,s)        
                    
    def getSongDuration(self):
        if self.notGotSongDuration is not None and self.radioPlayer.getLength() > 500:
            #Only calculate the song duration once per song. "> 500" is so to make sure we don't get 00:00 as our duration in self.updateSongTimeText.
            self.songDur = self.formatTime(int(self.radioPlayer.getLength()))
            self.notGotSongDuration = None            
            
    def getSongPostion(self):    
        self.songPos = self.formatTime((int(self.radioPlayer.getPosition())))

    def stationChange(self, newStation):
        self.notGotSongDuration = True
        self.radioPlayer.setStation(self.radioPlayer.getStationFromName(newStation))
        
        self.preferences['station'] = newStation
        self.savePreferences()
        self.radioPlayer.pauseSong()
        self.radioPlayer.clearSongs()
        self.radioPlayer.addSongs()
        
    def assignWidgets(self):
        self.playPauseButton.clicked.connect(self.playPausePressed)
        self.skipButton.clicked.connect(self.skipPressed)
        self.skipButton.setIcon(QIcon.fromTheme("media-skip-forward", QIcon("images/skip.png")))
        self.loveButton.clicked.connect(self.lovePressed)
        self.banButton.clicked.connect(self.banPressed)
        self.banButton.setIcon(QIcon.fromTheme("edit-delete", QIcon("images/ban.png")))
        self.tiredButton.clicked.connect(self.tiredPressed)
        self.tiredButton.setIcon(QIcon.fromTheme("edit-redo", QIcon("images/tired.png")))
        self.settingsButton.clicked.connect(self.settingsPressed)
        self.settingsButton.setIcon(QIcon.fromTheme("preferences-system", QIcon("images/settings.png")))
        self.volumeSlider.valueChanged.connect(self.volumeChange)
        #All other UI's need extra buttons added.
        self.muteButton.clicked.connect(self.mutePressed)
        self.muteButton.setIcon(QIcon.fromTheme("audio-volume-high", QIcon("images/audio-volume.png")))
        self.muteButton.setToolTip(QApplication.translate("qAndora", "Mute Volume", None, QApplication.UnicodeUTF8))
        self.infoButton.clicked.connect(self.infoPressed)
        self.infoButton.setIcon(QIcon.fromTheme("dialog-information", QIcon("images/about.png")))
        
        #Moved this here from getLastStation to make them not double apply when you relog
        self.radioPlayer.setChangeCallBack(self.songChangeQ)
        self.stationBox.activated[str].connect(self.stationChange)

    def volumeChange(self, val):
        self.preferences['volume'] = val
        self.radioPlayer.setVolume(val)
        self.savePreferences()
        
    def songChangeQ(self):
        invoke_in_main_thread(self.qTimer)
        invoke_in_main_thread(self.updateHistoryList)
        invoke_in_main_thread(self.fetchAlbumArt)
        invoke_in_main_thread(self.updateSongText)
        invoke_in_main_thread(self.desktopNotifications)
        invoke_in_main_thread(self.resetIcons)
        
    def updateSongText(self):       
        self.titleLabel.setText("<b>%s</b>"%(self.info['title']))
        self.albumLabel.setText("from <i>%s</i>"%(self.info['album']))
        self.artistLabel.setText("by %s"%(self.info['artist']))
        
        self.windowTitle = ("qAndora - %s by %s"%(self.info['title'], self.info['artist']))
        self.setWindowTitle(self.windowTitle)
        
        self.trayTitle = ("%s by %s"%(self.info['title'], self.info['artist']))
        self.songHeader.setText(self.trayTitle)
        
    def resetIcons(self):            
        if self.info['rating'] == "love":
            self.loveButton.setIcon(QIcon.fromTheme("emblem-favorite", QIcon("images/love.png")))
            self.loveAction.setIcon(QIcon.fromTheme("emblem-favorite", QIcon("images/love.png")))
            self.loveButton.setToolTip(QApplication.translate("qAndora", "Song Loved", None, QApplication.UnicodeUTF8))
            self.loveAction.setText("Song Loved")
        else:
            self.loveButton.setIcon(QIcon.fromTheme("favorites", QIcon("images/favorite.png")))
            self.loveAction.setIcon(QIcon.fromTheme("favorites", QIcon("images/favorite.png")))
            self.loveButton.setToolTip(QApplication.translate("qAndora", "Love this Song", None, QApplication.UnicodeUTF8))
            self.loveAction.setText("Love this Song")
            
        self.playPauseButton.setIcon(QIcon.fromTheme("media-playback-pause", QIcon("images/pause")))
        self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Pause", None, QApplication.UnicodeUTF8))
        self.playPauseAction.setText("Pause")
        self.playPauseAction.setIcon(QIcon.fromTheme("media-playback-pause", QIcon("images/pause")))
        
    def fetchAlbumArt(self):
        self.notGotSongDuration = True
        self.info = self.radioPlayer.songinfo[self.radioPlayer.curSong]
        
        try:
            self.uniqueFilename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            urllib.urlretrieve(str(self.info['thumbnail']), os.path.join(tempdir, self.uniqueFilename))
            self.albumartpath = os.path.join(tempdir, self.uniqueFilename)
            
        except:
            self.albumartpath = 'images/albumart.png'
            
        self.albumart = QPixmap(self.albumartpath) 
        self.albumImage.setPixmap(self.albumart)
        self.songHeader.setIcon(QIcon(self.albumartpath))
        
    def desktopNotifications(self):       
        if self.preferences['notifications'] == "Yes":
            if notiLoaded:
	        if self.albumartpath == 'images/albumart.png': 
                    songNoti=pynotify.Notification("%s"%(self.info['title']),"by %s\nfrom %s"%(self.info['artist'], self.info['album']))
                    songNoti.show()
                else:
                    songNoti=pynotify.Notification("%s"%(self.info['title']),"by %s\nfrom %s"%(self.info['artist'], self.info['album']),self.albumartpath)
                    songNoti.show()
            else:
                self.tray.showMessage("%s"%(self.info['title']),"by %s\nfrom %s"%(self.info['artist'], self.info['album']))
        
        self.tray.setToolTip("%s\nby %s\nfrom %s"%(self.info['title'], self.info['artist'], self.info['album']))

    def updateHistoryList(self):
        if self.albumart:
            newItem = QListWidgetItem()
            newItem.setText(("%s\nby %s\nfrom %s"%(self.info['title'], self.info['artist'], self.info['album'])))
            newItem.setIcon(self.albumart)
            self.historyList.insertItem(0, newItem)
        
    def settingsPressed(self):
        self.preferencesWin.show()
        
    def playPausePressed(self):
        if self.radioPlayer.playing:
            self.radioPlayer.pauseSong()
            self.playPauseButton.setIcon(QIcon.fromTheme("media-playback-start", QIcon("images/play")))
            self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Play", None, QApplication.UnicodeUTF8))
            self.playPauseAction.setText("Play")
            self.playPauseAction.setIcon(QIcon.fromTheme("media-playback-start", QIcon("images/play")))
        else:
            self.radioPlayer.playSong()
            self.playPauseButton.setIcon(QIcon.fromTheme("media-playback-pause", QIcon("images/pause")))
            self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Pause", None, QApplication.UnicodeUTF8))
            self.playPauseAction.setText("Pause")
            self.playPauseAction.setIcon(QIcon.fromTheme("media-playback-pause", QIcon("images/pause")))
        
    def skipPressed(self):
        self.radioPlayer.skipSong()
  
    def tiredPressed(self):       
        self.radioPlayer.tiredSong()
        self.radioPlayer.skipSong()

    def lovePressed(self):
        self.radioPlayer.loveSong()
        self.loveButton.setIcon(QIcon.fromTheme("emblem-favorite", QIcon("images/love")))
        self.loveButton.setToolTip(QApplication.translate("qAndora", "Song Loved", None, QApplication.UnicodeUTF8))
        self.loveAction.setText("Song Loved")
        self.loveAction.setIcon(QIcon.fromTheme("emblem-favorite", QIcon("images/love")))
        
    def banPressed(self):
        self.radioPlayer.banSong()
        self.radioPlayer.skipSong()

    def infoPressed(self):
        infoUrl = self.info['object'].songDetailURL
        openBrowser(infoUrl)

    def mutePressed(self):
        #Alternative volume button icons will need to be found
        if not self.muted:
            self.muteButton.setIcon(QIcon.fromTheme("audio-volume-muted", QIcon("images/audio-mute")))
            self.muteButton.setToolTip(QApplication.translate("qAndora", "Unmute Volume", None, QApplication.UnicodeUTF8))
            self.muted = True      
            
        else:
            self.muteButton.setIcon(QIcon.fromTheme("audio-volume-high", QIcon("images/audio-volume")))
            self.muteButton.setToolTip(QApplication.translate("qAndora", "Mute Volume", None, QApplication.UnicodeUTF8))
            self.muted = None
            
        self.radioPlayer.toggleMute()
        
    def exitPressed(self):
        sys.exit()

    def winKBevent(self, event):
        if event.KeyID == 179 or event.Key == 'Media_Play_Pause':
            invoke_in_main_thread(self.playPausePressed)
        if event.KeyID == 176 or event.Key == 'Media_Next_Track':
            invoke_in_main_thread(self.skipPressed)
        return True
        
    def linuxKBevent(self, event):
        if event.Key == "[269025044]":
            invoke_in_main_thread(self.playPausePressed)
        
        return True

    def bindWin32(self):
        try:
            import pyHook
        except ImportError:
            print('Please install PyHook: http://sourceforge.net/projects/pyhook/ using local bindings for now')
            self.assignShortcuts()
            return False
        self.hookman = pyHook.HookManager()
        self.hookman.KeyDown = self.winKBevent
        self.hookman.HookKeyboard()
        return True
        
    def bindLinux(self):
        try:
            import pyxhook
        except ImportError:
            print('Failed to import pyxhook.')
            self.assignShortcuts()
            return False
        self.hookman = pyxhook.HookManager()
        self.hookman.KeyDown = self.linuxKBevent
        self.hookman.HookKeyboard()
        self.hookman.start()
        return True
        
    def enableKeyBinds(self):
        if sys.platform == 'win32':
            self.assignShortcuts()
            loaded = self.bindWin32()
        elif sys.platform == 'darwin':
            print "Key bindings not supported on OSX loading focused keys instead."
            self.assignShortcuts()
        else:
            #print "Key bindings not supported on Linux loading focused keys instead."
            self.assignShortcuts()
            if not "arm" in platform.machine():
                loaded = self.bindLinux()
        
class PreferencesWindow(QDialog, Ui_qPreferences):
    def __init__(self, parent=None):
        super(PreferencesWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.rent = parent
        self.assignCallbacks()
        self.populateDrops()
        self.fillInLoginText()
        
    def closeEvent(self, event):
        self.close()
        
    def populateDrops( self ):
        qualities = ['High', 'Medium', 'Low']
        for q in qualities:
            self.qualityBox.addItem(q)
            
        self.qualityBox.setCurrentIndex(qualities.index(self.rent.preferences['quality']))
        self.qualityBox.activated[str].connect(self.qualityChange)
            
        choices = ['Yes', 'No']
        for s in choices:
            self.notificationBox.addItem(s)
            
        self.notificationBox.setCurrentIndex(choices.index(self.rent.preferences['notifications']))
        self.notificationBox.activated[str].connect(self.notificationChange)
        
    def qualityChange( self, q ):
        self.rent.preferences['quality'] = q
        self.rent.radioPlayer.setAudioFormat(q)
        self.rent.savePreferences()
        
    def notificationChange( self, s ):
        self.rent.preferences['notifications'] = s
        self.rent.savePreferences()
        
    def assignCallbacks( self ):
        self.logoutButton.clicked.connect(self.logoutPressed)
        self.liveCheck.stateChanged.connect(self.liveCheckChanged)
        self.liveCheck.setChecked(self.rent.preferences['skiplive'])
        self.rent.radioPlayer.setAutoSkip( "live", self.rent.preferences['skiplive'] )
        self.remixCheck.stateChanged.connect(self.remixCheckChanged)
        self.remixCheck.setChecked(self.rent.preferences['skipremix'])
        self.rent.radioPlayer.setAutoSkip( "remix", self.rent.preferences['skipremix'] )
        self.editCheck.stateChanged.connect(self.editCheckChanged)
        self.editCheck.setChecked(self.rent.preferences['skipedit'])
        self.rent.radioPlayer.setAutoSkip( "edit", self.rent.preferences['skipedit'] )
        self.rateCheck.stateChanged.connect(self.rateCheckChanged)
        self.rateCheck.setChecked(self.rent.preferences['banskips'])
        self.rent.radioPlayer.setAutoSkip( "ban", self.rent.preferences['banskips'] )
        self.loginButton.clicked.connect(self.loginPressed)
        self.accountButton.clicked.connect(self.accountPressed)
        
    def liveCheckChanged( self, state ):
        if state == Qt.Checked:
            self.rent.radioPlayer.setAutoSkip( "live", True )
            self.rent.preferences['skiplive'] = True
        else:
            self.rent.radioPlayer.setAutoSkip( "live", False )
            self.rent.preferences['skiplive'] = False
        self.rent.savePreferences()
            
    def remixCheckChanged( self, state ):
        if state == Qt.Checked:
            self.rent.radioPlayer.setAutoSkip( "remix", True )
            self.rent.preferences['skipremix'] = True
        else:
            self.rent.radioPlayer.setAutoSkip( "remix", False )
            self.rent.preferences['skipremix'] = False
        self.rent.savePreferences()
            
    def editCheckChanged( self, state ):
        if state == Qt.Checked:
            self.rent.radioPlayer.setAutoSkip( "edit", True )
            self.rent.preferences['skipedit'] = True
        else:
            self.rent.radioPlayer.setAutoSkip( "edit", False )
            self.rent.preferences['skipedit'] = False
        self.rent.savePreferences()
            
    def rateCheckChanged( self, state ):
        if state == Qt.Checked:
            self.rent.radioPlayer.setAutoSkip( "ban", True )
            self.rent.preferences['banskips'] = True
        else:
            self.rent.radioPlayer.setAutoSkip( "ban", False )
            self.rent.preferences['banskips'] = False
        self.rent.savePreferences()
    
    def logoutPressed( self ):
        self.nameEdit.setText("")
        self.passwordEdit.setText("")
        self.rent.radioPlayer.pauseSong()
        self.rent.defaultPreferences()
        self.rent.radioPlayer = volcanoPlayer()
        self.rent.radioPlayer.setChangeCallBack(self.rent.songChangeQ)
        self.rent.tray.hide()
        self.rent.hide()
        
    def loginPressed(self):
        self.hide()
        self.rent.loginUser(self.nameEdit.text(), self.passwordEdit.text())
      
    def fillInLoginText(self):
        if self.rent.preferences['username']:
            self.nameEdit.setText(self.rent.preferences['username'])    

        if self.rent.preferences['password']:
            self.passwordEdit.setText(self.rent.preferences['password'])

    def accountPressed( self ):
        openBrowser("https://www.pandora.com/account/register")
        
class ErrorWindow(QDialog, Ui_qError):
    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent)
        self.setupUi(self)
        
    def closeEvent(self, event):
        sys.exit()
        
def openBrowser(url):
    webbrowser.open(url)
    try:
        os.wait()
    except:
        pass
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
    ret = app.exec_()
    if os.name == 'posix' and "arm" not in platform.machine():
        mainWin.hookman.cancel()    
    sys.exit( ret )
