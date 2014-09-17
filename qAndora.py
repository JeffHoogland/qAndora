import sys

from PySide.QtGui import *

from ui_qAndora import Ui_qAndora

import playerVLC

class MainWindow(QMainWindow, Ui_qAndora):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignButtons()
        
    def assignButtons( self ):
        self.playPauseButton.setIcon(QIcon("images/pause.png"))
        self.skipButton.setIcon(QIcon("images/skip.png"))
        self.loveButton.setIcon(QIcon("images/favorite.png"))
        self.banButton.setIcon(QIcon("images/ban.png"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit( app.exec_() )
