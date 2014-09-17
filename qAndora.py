import sys

from PySide.QtGui import *

from ui_qAndora import Ui_qAndora

import playerVLC

class MainWindow(QMainWindow, Ui_qAndora):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignButtons()
        
        self.radioPlayer = playerVLC.volcanoPlayer()
        self.radioPlayer.auth( "jeffhoogland@linux.com", "")
        self.radioPlayer.setStation(self.radioPlayer.getStations()[0])
        self.radioPlayer.setChangeCallBack( self.songChange )
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
    
    def songChange( self ):
        print "Song changed"
        info = self.radioPlayer.songinfo[self.radioPlayer.curSong]
        self.titleLabel.setText(info['title'])
        self.albumLabel.setText(info['album'])
        if info['rating'] == "love":
            self.loveButton.setIcon(QIcon("images/love.png"))
        else:
            self.loveButton.setIcon(QIcon("images/favorite.png"))
        
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit( app.exec_() )
