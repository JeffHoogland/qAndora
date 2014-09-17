# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qAndora.ui'
#
# Created: Wed Sep 17 11:24:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qAndora(object):
    def setupUi(self, qAndora):
        qAndora.setObjectName("qAndora")
        qAndora.resize(400, 300)
        self.playPauseButton = QtGui.QToolButton(qAndora)
        self.playPauseButton.setGeometry(QtCore.QRect(20, 220, 71, 61))
        self.playPauseButton.setObjectName("playPauseButton")
        self.skipButton = QtGui.QToolButton(qAndora)
        self.skipButton.setGeometry(QtCore.QRect(110, 220, 71, 61))
        self.skipButton.setObjectName("skipButton")
        self.loveButton = QtGui.QToolButton(qAndora)
        self.loveButton.setGeometry(QtCore.QRect(200, 220, 71, 61))
        self.loveButton.setObjectName("loveButton")
        self.banButton = QtGui.QToolButton(qAndora)
        self.banButton.setGeometry(QtCore.QRect(290, 220, 71, 61))
        self.banButton.setObjectName("banButton")
        self.titleLabel = QtGui.QLabel(qAndora)
        self.titleLabel.setGeometry(QtCore.QRect(30, 20, 321, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.albumLabel = QtGui.QLabel(qAndora)
        self.albumLabel.setGeometry(QtCore.QRect(30, 50, 201, 21))
        self.albumLabel.setObjectName("albumLabel")
        self.albumArtView = QtGui.QGraphicsView(qAndora)
        self.albumArtView.setGeometry(QtCore.QRect(30, 90, 201, 111))
        self.albumArtView.setObjectName("albumArtView")

        self.retranslateUi(qAndora)
        QtCore.QMetaObject.connectSlotsByName(qAndora)

    def retranslateUi(self, qAndora):
        qAndora.setWindowTitle(QtGui.QApplication.translate("qAndora", " qAndora", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setText(QtGui.QApplication.translate("qAndora", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setText(QtGui.QApplication.translate("qAndora", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.loveButton.setText(QtGui.QApplication.translate("qAndora", "Love", None, QtGui.QApplication.UnicodeUTF8))
        self.banButton.setText(QtGui.QApplication.translate("qAndora", "Ban", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("qAndora", "Song Title Goes Here", None, QtGui.QApplication.UnicodeUTF8))
        self.albumLabel.setText(QtGui.QApplication.translate("qAndora", "Album Name Goes Here", None, QtGui.QApplication.UnicodeUTF8))

