# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qPreferences.ui'
#
# Created: Wed Oct 15 23:24:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qPreferences(object):
    def setupUi(self, qPreferences):
        qPreferences.setObjectName("qPreferences")
        qPreferences.resize(400, 236)
        self.prefWidget = QtGui.QTabWidget(qPreferences)
        self.prefWidget.setEnabled(True)
        self.prefWidget.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.prefWidget.setObjectName("prefWidget")
        self.aboutTab = QtGui.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.aboutLabel = QtGui.QLabel(self.aboutTab)
        self.aboutLabel.setGeometry(QtCore.QRect(10, 10, 361, 131))
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setOpenExternalLinks(True)
        self.aboutLabel.setObjectName("aboutLabel")
        self.prefWidget.addTab(self.aboutTab, "")
        self.generlTab = QtGui.QWidget()
        self.generlTab.setAccessibleName("")
        self.generlTab.setObjectName("generlTab")
        self.userFrame = QtGui.QFrame(self.generlTab)
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
        self.qualityFrame = QtGui.QFrame(self.generlTab)
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
        self.notificationFrame = QtGui.QFrame(self.generlTab)
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
        self.prefWidget.addTab(self.generlTab, "")
        self.filterTab = QtGui.QWidget()
        self.filterTab.setObjectName("filterTab")
        self.liveCheck = QtGui.QCheckBox(self.filterTab)
        self.liveCheck.setGeometry(QtCore.QRect(20, 10, 151, 26))
        self.liveCheck.setChecked(False)
        self.liveCheck.setObjectName("liveCheck")
        self.remixCheck = QtGui.QCheckBox(self.filterTab)
        self.remixCheck.setGeometry(QtCore.QRect(20, 40, 171, 26))
        self.remixCheck.setObjectName("remixCheck")
        self.editCheck = QtGui.QCheckBox(self.filterTab)
        self.editCheck.setGeometry(QtCore.QRect(190, 10, 171, 26))
        self.editCheck.setObjectName("editCheck")
        self.label = QtGui.QLabel(self.filterTab)
        self.label.setGeometry(QtCore.QRect(20, 70, 341, 91))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.rateCheck = QtGui.QCheckBox(self.filterTab)
        self.rateCheck.setGeometry(QtCore.QRect(190, 40, 181, 26))
        self.rateCheck.setObjectName("rateCheck")
        self.prefWidget.addTab(self.filterTab, "")

        self.retranslateUi(qPreferences)
        self.prefWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(qPreferences)

    def retranslateUi(self, qPreferences):
        qPreferences.setWindowTitle(QtGui.QApplication.translate("qPreferences", "qAndora - Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutLabel.setText(QtGui.QApplication.translate("qPreferences", "<html><head/><body><p>qAndora is a cross platform, open source, <a href=\"www.pandora.com\"><span style=\" text-decoration: underline; color:#0057ae;\">Pandora Internet Radio</span></a> client written in <a href=\"https://www.python.org/\"><span style=\" text-decoration: underline; color:#0057ae;\">Python</span></a> using <a href=\"http://qt-project.org/\"><span style=\" text-decoration: underline; color:#0057ae;\">Qt</span></a> and <a href=\"http://www.videolan.org/\"><span style=\" text-decoration: underline; color:#0057ae;\">VLC</span></a> by <a href=\"http://www.jeffhoogland.com/\"><span style=\" text-decoration: underline; color:#0057ae;\">Jeff Hoogland</span></a>.<br/><br/><a href=\"https://github.com/JeffHoogland/qAndora\"><span style=\" text-decoration: underline; color:#0057ae;\">qAndora source on GitHub</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.prefWidget.setTabText(self.prefWidget.indexOf(self.aboutTab), QtGui.QApplication.translate("qPreferences", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("qPreferences", "<b>Change User:", None, QtGui.QApplication.UnicodeUTF8))
        self.logoutButton.setText(QtGui.QApplication.translate("qPreferences", "Logout", None, QtGui.QApplication.UnicodeUTF8))
        self.qualityLabel.setText(QtGui.QApplication.translate("qPreferences", "<b>Audio Quality:", None, QtGui.QApplication.UnicodeUTF8))
        self.notificationLabel.setText(QtGui.QApplication.translate("qPreferences", "<b>Desktop Notifications:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefWidget.setTabText(self.prefWidget.indexOf(self.generlTab), QtGui.QApplication.translate("qPreferences", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.liveCheck.setText(QtGui.QApplication.translate("qPreferences", "Filter live songs", None, QtGui.QApplication.UnicodeUTF8))
        self.remixCheck.setText(QtGui.QApplication.translate("qPreferences", "Filter remix songs", None, QtGui.QApplication.UnicodeUTF8))
        self.editCheck.setText(QtGui.QApplication.translate("qPreferences", "Filter edit songs", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("qPreferences", "<html><head/><body><p>Remix are songs that have &quot;mix&quot; in () or []</p><p>Live are songs that have &quot;live&quot; in () or []</p><p>Edit are songs that contain &quot;edit&quot; in () or []</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rateCheck.setText(QtGui.QApplication.translate("qPreferences", "Ban Filtered Songs", None, QtGui.QApplication.UnicodeUTF8))
        self.prefWidget.setTabText(self.prefWidget.indexOf(self.filterTab), QtGui.QApplication.translate("qPreferences", "Filters", None, QtGui.QApplication.UnicodeUTF8))

