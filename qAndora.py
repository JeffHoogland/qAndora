import sys
import os
import platform

from PySide.QtGui import *
from PySide.QtCore import *

if not "arm" in platform.machine():
    from ui_qAndora import Ui_MainWindow
else:
    from ui_qAndora_mobile import Ui_MainWindow

from ui_qLogin import Ui_qLogin
from ui_qPreferences import Ui_qPreferences

from playerGst import volcanoPlayer
import tempfile
import urllib
import webbrowser
import datetime
import cPickle as pickle

#See if system supports these notifications
try:
    import pynotify
    pynotify.init("Song Changed")
    notiLoaded = True
except:
    notiLoaded = False

tempdir = tempfile.gettempdir()

#print "Current tmp directory is %s"%tempdir

APP_ID = 'qAndora'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        #Local keybinds for just when app is focused
        #self.assignShortcuts()
        #Global Keybinds - work on this
        self.enableKeyBinds()
        
        self.stationBox.setEditable(True)
        self.stationBox.lineEdit().setAlignment(Qt.AlignCenter)
        self.stationBox.lineEdit().setReadOnly(True)
        
        self.radioPlayer = volcanoPlayer()
        
        self.loginWin = LoginWindow( self )
        
        #build our systray icon
        icon = QIcon("images/qAndora.png")
        menu = QMenu()
        self.playPauseAction = menu.addAction("Pause")
        self.playPauseAction.setIcon(QIcon("images/pause.png"))
        self.playPauseAction.triggered.connect(self.playPausePressed)
        skipTrackAction = menu.addAction("Skip Track")
        skipTrackAction.triggered.connect(self.skipPressed)
        skipTrackAction.setIcon(QIcon("images/skip.png"))
        self.loveAction = menu.addAction("Favorite Track")
        self.loveAction.triggered.connect(self.lovePressed)
        self.loveAction.setIcon(QIcon("images/favorite.png"))
        banAction = menu.addAction("Ban Track")
        banAction.triggered.connect(self.banPressed)
        banAction.setIcon(QIcon("images/ban.png"))
        tiredAction = menu.addAction("Tired Track")
        tiredAction.triggered.connect(self.tiredPressed)
        tiredAction.setIcon(QIcon("images/tired.png"))
        
        #exitAction = menu.addAction("Exit")
        #exitAction.triggered.connect(self.exitPressed)
        #exitAction.setIcon(QIcon("images/exit.png"))
        
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.trayClicked)
        
        #Read in stored preferences
        home = os.path.expanduser("~")
        if os.path.exists("%s/.config/qAndora/preferences.cfg"%home):
            self.preferences = pickle.load( open( "%s/.config/qAndora/preferences.cfg"%home, "rb" ) )
            if self.preferences['username']:
                self.loginUser(self.preferences['username'], self.preferences['password'])
            else:
                self.loginWin.show()
        else:
            self.defaultPreferences()
            self.loginWin.show()
            
        self.preferencesWin = PreferencesWindow( self )
        
    def trayClicked( self, reason ):
        if reason == self.tray.Trigger:
            if self.isVisible:
                self.hide()
                self.isVisible = False
            else:
                self.show()
                self.isVisible = True
        
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
            
    def savePreferences( self ):
        home = os.path.expanduser("~")
        if not os.path.exists("%s/.config/qAndora"%home):
            os.makedirs("%s/.config/qAndora"%home)
        pickle.dump( self.preferences, open( "%s/.config/qAndora/preferences.cfg"%home, "wb" ))
    
    def loginUser( self, userName, userPassword ):
        self.preferences['username'] = userName
        self.preferences['password'] = userPassword
        self.savePreferences()
        
        self.radioPlayer.setVolume( self.preferences['volume'] )
        self.volumeSlider.setValue( self.preferences['volume'] )
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
        self.tray.show()
        self.isVisible = True
        
    def timerTick( self ):
        pos = str(datetime.timedelta(seconds=int(self.radioPlayer.getPosition())))
        dur = str(datetime.timedelta(seconds=int(self.radioPlayer.getLength())))
        
        posh, posm, poss = pos.split(":")
        durh, durm, durs = dur.split(":")
        
        pos = "%s:%s"%(posm, poss)
        dur = "%s:%s"%(durm, durs)
        
        t = "<b>%s  /  %s</b>" % (pos, dur)
        self.positionLabel.setText(t)
        
        if pos == dur and pos != "00:00":
            self.radioPlayer.nextSong()
        
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
        self.tiredButton.clicked.connect(self.tiredPressed)
        self.settingsButton.clicked.connect(self.settingsPressed)
        self.volumeSlider.valueChanged.connect(self.volumeChange)
        
    def assignShortcuts( self ):
        self.playPauseShortcut = QShortcut(QKeySequence(Qt.Key_Space), self)
        self.playPauseShortcut.setContext(Qt.ApplicationShortcut)
        self.playPauseShortcut.activated.connect(self.playPausePressed)
        
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
        if "arm" in platform.machine():
            fontsize = "18"
        else:
            fontsize = "12"
        self.titleLabel.setText('<span style=" font-size:%spt;"><b>Song:</b> <a href="%s">%s</a></span>'%(fontsize, info['object'].songDetailURL, info['title']))
        self.albumLabel.setText('<span style=" font-size:%spt;"><b>Album:</b> <a href="%s">%s</a></span>'%(fontsize, info['object'].albumDetailURL, info['album']))
        self.artistLabel.setText('<span style=" font-size:%spt;"><b>Artist:</b> %s</span>'%(fontsize, info['artist']))
        if info['rating'] == "love":
            self.loveButton.setIcon(QIcon("images/love.png"))
            self.loveAction.setIcon(QIcon("images/love.png"))
            self.loveButton.setToolTip(QApplication.translate("qAndora", "Favorited", None, QApplication.UnicodeUTF8))
        else:
            self.loveButton.setIcon(QIcon("images/favorite.png"))
            self.loveAction.setIcon(QIcon("images/favorite.png"))
            self.loveButton.setToolTip(QApplication.translate("qAndora", "Mark Favorite", None, QApplication.UnicodeUTF8))
            
        self.playPauseButton.setIcon(QIcon("images/pause.png"))
        self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Pause", None, QApplication.UnicodeUTF8))
        self.playPauseAction.setText("Pause")
        self.playPauseAction.setIcon(QIcon("images/pause.png"))
        
        try:
            urllib.urlretrieve(str(info['thumbnail']), os.path.join(tempdir, 'albumart.jpg'))
            albumartpath = os.path.join(tempdir, 'albumart.jpg')
        except:
            albumartpath = 'images/albumart.png'
        
        albumart = QPixmap(albumartpath)
        
        self.albumImage.setPixmap(albumart)
        
        newItem = QListWidgetItem()
        #newItem.setTextAlignment(Qt.AlignRight)
        newItem.setText(info['title'])
        newItem.setToolTip("By: %s"%info['artist'])
        newItem.setIcon(albumart)
        self.historyList.insertItem(0, newItem)
        
        if self.preferences['notifications'] == "Yes":
            if notiLoaded:
                songNoti=pynotify.Notification("Song Changed","%s by %s"%(info['title'], info['artist']))
                songNoti.show ()
            else:
                self.tray.showMessage("Song Changed", "%s by %s"%(info['title'], info['artist']))
        
        self.tray.setToolTip("%s by %s"%(info['title'], info['artist']))
        
    def settingsPressed( self ):
        self.preferencesWin.show()
        
    def playPausePressed( self ):
        if self.radioPlayer.playing:
            self.radioPlayer.pauseSong()
            self.playPauseButton.setIcon(QIcon("images/play.png"))
            self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Play", None, QApplication.UnicodeUTF8))
            self.playPauseAction.setText("Play")
            self.playPauseAction.setIcon(QIcon("images/play.png"))
        else:
            self.radioPlayer.playSong()
            self.playPauseButton.setIcon(QIcon("images/pause.png"))
            self.playPauseButton.setToolTip(QApplication.translate("qAndora", "Pause", None, QApplication.UnicodeUTF8))
            self.playPauseAction.setText("Pause")
            self.playPauseAction.setIcon(QIcon("images/pause.png"))
    
    def skipPressed( self ):
        self.radioPlayer.skipSong()
    
    def tiredPressed( self ):
        self.radioPlayer.tiredSong()
        self.radioPlayer.skipSong()
    
    def lovePressed( self ):
        self.radioPlayer.loveSong()
        self.loveButton.setIcon(QIcon("images/love.png"))
        self.loveButton.setToolTip(QApplication.translate("qAndora", "Favorited", None, QApplication.UnicodeUTF8))
        
    def banPressed( self ):
        self.radioPlayer.banSong()
        self.radioPlayer.skipSong()

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
        self.rent.hide()
        self.hide()
        self.rent.radioPlayer.pauseSong()
        self.rent.defaultPreferences()
        self.rent.loginWin.show()

class LoginWindow(QDialog, Ui_qLogin):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignCallbacks()
        
        self.rent = parent
        
    def assignCallbacks( self ):
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
    ret = app.exec_()
    if os.name == 'posix' and "arm" not in platform.machine():
        mainWin.hookman.cancel()
    sys.exit( ret )
