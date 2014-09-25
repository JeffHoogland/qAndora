# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qAndora.ui'
#
# Created: Wed Sep 24 23:46:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qAndora(object):
    def setupUi(self, qAndora):
        qAndora.setObjectName("qAndora")
        qAndora.resize(381, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/qAndora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qAndora.setWindowIcon(icon)
        self.titleLabel = QtGui.QLabel(qAndora)
        self.titleLabel.setGeometry(QtCore.QRect(100, 210, 261, 21))
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.albumLabel = QtGui.QLabel(qAndora)
        self.albumLabel.setGeometry(QtCore.QRect(100, 240, 261, 21))
        self.albumLabel.setWordWrap(True)
        self.albumLabel.setObjectName("albumLabel")
        self.albumImage = QtGui.QLabel(qAndora)
        self.albumImage.setGeometry(QtCore.QRect(100, 10, 261, 191))
        self.albumImage.setMinimumSize(QtCore.QSize(241, 191))
        self.albumImage.setScaledContents(True)
        self.albumImage.setObjectName("albumImage")
        self.stationBox = QtGui.QComboBox(qAndora)
        self.stationBox.setGeometry(QtCore.QRect(10, 300, 361, 31))
        self.stationBox.setObjectName("stationBox")
        self.frame = QtGui.QFrame(qAndora)
        self.frame.setGeometry(QtCore.QRect(0, 20, 91, 261))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.playPauseButton = QtGui.QToolButton(self.frame)
        self.playPauseButton.setGeometry(QtCore.QRect(10, 10, 71, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playPauseButton.setIcon(icon1)
        self.playPauseButton.setObjectName("playPauseButton")
        self.skipButton = QtGui.QToolButton(self.frame)
        self.skipButton.setGeometry(QtCore.QRect(10, 70, 71, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skipButton.setIcon(icon2)
        self.skipButton.setObjectName("skipButton")
        self.loveButton = QtGui.QToolButton(self.frame)
        self.loveButton.setGeometry(QtCore.QRect(10, 130, 71, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loveButton.setIcon(icon3)
        self.loveButton.setObjectName("loveButton")
        self.banButton = QtGui.QToolButton(self.frame)
        self.banButton.setGeometry(QtCore.QRect(10, 190, 71, 61))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/ban.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.banButton.setIcon(icon4)
        self.banButton.setObjectName("banButton")
        self.artistLabel = QtGui.QLabel(qAndora)
        self.artistLabel.setGeometry(QtCore.QRect(100, 270, 261, 21))
        self.artistLabel.setObjectName("artistLabel")

        self.retranslateUi(qAndora)
        QtCore.QMetaObject.connectSlotsByName(qAndora)

    def retranslateUi(self, qAndora):
        qAndora.setWindowTitle(QtGui.QApplication.translate("qAndora", " qAndora - Internet Radio", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("qAndora", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.albumLabel.setText(QtGui.QApplication.translate("qAndora", "Album", None, QtGui.QApplication.UnicodeUTF8))
        self.albumImage.setText(QtGui.QApplication.translate("qAndora", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setToolTip(QtGui.QApplication.translate("qAndora", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setText(QtGui.QApplication.translate("qAndora", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setToolTip(QtGui.QApplication.translate("qAndora", "Skip Song", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setText(QtGui.QApplication.translate("qAndora", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.loveButton.setToolTip(QtGui.QApplication.translate("qAndora", "Mark Favorite", None, QtGui.QApplication.UnicodeUTF8))
        self.loveButton.setText(QtGui.QApplication.translate("qAndora", "Love", None, QtGui.QApplication.UnicodeUTF8))
        self.banButton.setToolTip(QtGui.QApplication.translate("qAndora", "Ban Song", None, QtGui.QApplication.UnicodeUTF8))
        self.banButton.setText(QtGui.QApplication.translate("qAndora", "Ban", None, QtGui.QApplication.UnicodeUTF8))
        self.artistLabel.setText(QtGui.QApplication.translate("qAndora", "Artist", None, QtGui.QApplication.UnicodeUTF8))

