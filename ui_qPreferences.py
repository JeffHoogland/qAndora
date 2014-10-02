# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qPreferences.ui'
#
# Created: Thu Oct  2 14:20:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qPreferences(object):
    def setupUi(self, qPreferences):
        qPreferences.setObjectName("qPreferences")
        qPreferences.resize(400, 243)
        self.prefWidget = QtGui.QTabWidget(qPreferences)
        self.prefWidget.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.prefWidget.setObjectName("prefWidget")
        self.generalSettings = QtGui.QWidget()
        self.generalSettings.setAccessibleName("")
        self.generalSettings.setObjectName("generalSettings")
        self.userFrame = QtGui.QFrame(self.generalSettings)
        self.userFrame.setGeometry(QtCore.QRect(10, 10, 361, 51))
        self.userFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.userFrame.setObjectName("userFrame")
        self.userLabel = QtGui.QLabel(self.userFrame)
        self.userLabel.setGeometry(QtCore.QRect(20, 10, 121, 21))
        self.userLabel.setObjectName("userLabel")
        self.logoutButton = QtGui.QToolButton(self.userFrame)
        self.logoutButton.setGeometry(QtCore.QRect(190, 10, 151, 29))
        self.logoutButton.setObjectName("logoutButton")
        self.qualityFrame = QtGui.QFrame(self.generalSettings)
        self.qualityFrame.setGeometry(QtCore.QRect(10, 70, 361, 51))
        self.qualityFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qualityFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.qualityFrame.setObjectName("qualityFrame")
        self.qualityLabel = QtGui.QLabel(self.qualityFrame)
        self.qualityLabel.setGeometry(QtCore.QRect(20, 10, 121, 21))
        self.qualityLabel.setObjectName("qualityLabel")
        self.qualityBox = QtGui.QComboBox(self.qualityFrame)
        self.qualityBox.setGeometry(QtCore.QRect(190, 10, 151, 31))
        self.qualityBox.setObjectName("qualityBox")
        self.notificationFrame = QtGui.QFrame(self.generalSettings)
        self.notificationFrame.setGeometry(QtCore.QRect(10, 130, 361, 51))
        self.notificationFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.notificationFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.notificationFrame.setObjectName("notificationFrame")
        self.notificationLabel = QtGui.QLabel(self.notificationFrame)
        self.notificationLabel.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.notificationLabel.setObjectName("notificationLabel")
        self.notificationBox = QtGui.QComboBox(self.notificationFrame)
        self.notificationBox.setGeometry(QtCore.QRect(241, 10, 101, 31))
        self.notificationBox.setObjectName("notificationBox")
        self.prefWidget.addTab(self.generalSettings, "")
        self.keySettings = QtGui.QWidget()
        self.keySettings.setObjectName("keySettings")
        self.prefWidget.addTab(self.keySettings, "")
        self.filterSettings = QtGui.QWidget()
        self.filterSettings.setObjectName("filterSettings")
        self.prefWidget.addTab(self.filterSettings, "")

        self.retranslateUi(qPreferences)
        self.prefWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(qPreferences)

    def retranslateUi(self, qPreferences):
        qPreferences.setWindowTitle(QtGui.QApplication.translate("qPreferences", "qAndora - Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("qPreferences", "<b>Change User:", None, QtGui.QApplication.UnicodeUTF8))
        self.logoutButton.setText(QtGui.QApplication.translate("qPreferences", "Logout", None, QtGui.QApplication.UnicodeUTF8))
        self.qualityLabel.setText(QtGui.QApplication.translate("qPreferences", "<b>Audio Quality:", None, QtGui.QApplication.UnicodeUTF8))
        self.notificationLabel.setText(QtGui.QApplication.translate("qPreferences", "<b>Desktop Notifications:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefWidget.setTabText(self.prefWidget.indexOf(self.generalSettings), QtGui.QApplication.translate("qPreferences", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.prefWidget.setTabText(self.prefWidget.indexOf(self.keySettings), QtGui.QApplication.translate("qPreferences", "Hotkeys", None, QtGui.QApplication.UnicodeUTF8))
        self.prefWidget.setTabText(self.prefWidget.indexOf(self.filterSettings), QtGui.QApplication.translate("qPreferences", "Filters", None, QtGui.QApplication.UnicodeUTF8))

