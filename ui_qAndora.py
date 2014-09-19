# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qAndora.ui'
#
# Created: Thu Sep 18 22:35:18 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qAndora(object):
    def setupUi(self, qAndora):
        qAndora.setObjectName("qAndora")
        qAndora.resize(381, 361)
        self.playPauseButton = QtGui.QToolButton(qAndora)
        self.playPauseButton.setGeometry(QtCore.QRect(10, 20, 71, 61))
        self.playPauseButton.setObjectName("playPauseButton")
        self.skipButton = QtGui.QToolButton(qAndora)
        self.skipButton.setGeometry(QtCore.QRect(10, 90, 71, 61))
        self.skipButton.setObjectName("skipButton")
        self.loveButton = QtGui.QToolButton(qAndora)
        self.loveButton.setGeometry(QtCore.QRect(10, 160, 71, 61))
        self.loveButton.setObjectName("loveButton")
        self.banButton = QtGui.QToolButton(qAndora)
        self.banButton.setGeometry(QtCore.QRect(10, 230, 71, 61))
        self.banButton.setObjectName("banButton")
        self.titleLabel = QtGui.QLabel(qAndora)
        self.titleLabel.setGeometry(QtCore.QRect(100, 20, 261, 21))
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.albumLabel = QtGui.QLabel(qAndora)
        self.albumLabel.setGeometry(QtCore.QRect(100, 50, 261, 21))
        self.albumLabel.setWordWrap(True)
        self.albumLabel.setObjectName("albumLabel")
        self.albumImage = QtGui.QLabel(qAndora)
        self.albumImage.setGeometry(QtCore.QRect(100, 80, 241, 191))
        self.albumImage.setMinimumSize(QtCore.QSize(241, 191))
        self.albumImage.setScaledContents(True)
        self.albumImage.setObjectName("albumImage")
        self.stationBox = QtGui.QComboBox(qAndora)
        self.stationBox.setGeometry(QtCore.QRect(10, 310, 361, 31))
        self.stationBox.setObjectName("stationBox")

        self.retranslateUi(qAndora)
        QtCore.QMetaObject.connectSlotsByName(qAndora)

    def retranslateUi(self, qAndora):
        qAndora.setWindowTitle(QtGui.QApplication.translate("qAndora", " qAndora", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setToolTip(QtGui.QApplication.translate("qAndora", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setText(QtGui.QApplication.translate("qAndora", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setToolTip(QtGui.QApplication.translate("qAndora", "Skip Song", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setText(QtGui.QApplication.translate("qAndora", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.loveButton.setToolTip(QtGui.QApplication.translate("qAndora", "Mark Favorite", None, QtGui.QApplication.UnicodeUTF8))
        self.loveButton.setText(QtGui.QApplication.translate("qAndora", "Love", None, QtGui.QApplication.UnicodeUTF8))
        self.banButton.setToolTip(QtGui.QApplication.translate("qAndora", "Ban Song", None, QtGui.QApplication.UnicodeUTF8))
        self.banButton.setText(QtGui.QApplication.translate("qAndora", "Ban", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("qAndora", "Song Title Goes Here", None, QtGui.QApplication.UnicodeUTF8))
        self.albumLabel.setText(QtGui.QApplication.translate("qAndora", "Album Name Goes Here", None, QtGui.QApplication.UnicodeUTF8))
        self.albumImage.setText(QtGui.QApplication.translate("qAndora", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

