# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qAndora.ui'
#
# Created: Thu Sep 18 14:14:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qAndora(object):
    def setupUi(self, qAndora):
        qAndora.setObjectName("qAndora")
        qAndora.resize(400, 300)
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
        self.titleLabel.setGeometry(QtCore.QRect(100, 20, 201, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.albumLabel = QtGui.QLabel(qAndora)
        self.albumLabel.setGeometry(QtCore.QRect(100, 50, 201, 21))
        self.albumLabel.setObjectName("albumLabel")
        self.albumImage = QtGui.QLabel(qAndora)
        self.albumImage.setGeometry(QtCore.QRect(100, 80, 241, 191))
        self.albumImage.setMinimumSize(QtCore.QSize(241, 191))
        self.albumImage.setObjectName("albumImage")

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
        self.albumImage.setText(QtGui.QApplication.translate("qAndora", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

