# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qLogin.ui'
#
# Created: Fri Oct  3 10:26:01 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qLogin(object):
    def setupUi(self, qLogin):
        qLogin.setObjectName("qLogin")
        qLogin.resize(400, 212)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/qAndora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qLogin.setWindowIcon(icon)
        self.nameFrame = QtGui.QFrame(qLogin)
        self.nameFrame.setGeometry(QtCore.QRect(20, 10, 361, 71))
        self.nameFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.nameFrame.setObjectName("nameFrame")
        self.nameLabel = QtGui.QLabel(self.nameFrame)
        self.nameLabel.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.nameLabel.setObjectName("nameLabel")
        self.nameEdit = QtGui.QLineEdit(self.nameFrame)
        self.nameEdit.setGeometry(QtCore.QRect(10, 30, 341, 27))
        self.nameEdit.setObjectName("nameEdit")
        self.frame = QtGui.QFrame(qLogin)
        self.frame.setGeometry(QtCore.QRect(20, 90, 361, 71))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.passwordLabel = QtGui.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordEdit = QtGui.QLineEdit(self.frame)
        self.passwordEdit.setGeometry(QtCore.QRect(10, 30, 341, 27))
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.loginButton = QtGui.QPushButton(qLogin)
        self.loginButton.setGeometry(QtCore.QRect(30, 170, 161, 31))
        self.loginButton.setAutoDefault(False)
        self.loginButton.setObjectName("loginButton")
        self.accountButton = QtGui.QToolButton(qLogin)
        self.accountButton.setGeometry(QtCore.QRect(205, 170, 161, 29))
        self.accountButton.setObjectName("accountButton")

        self.retranslateUi(qLogin)
        QtCore.QMetaObject.connectSlotsByName(qLogin)

    def retranslateUi(self, qLogin):
        qLogin.setWindowTitle(QtGui.QApplication.translate("qLogin", "qAndora - Login", None, QtGui.QApplication.UnicodeUTF8))
        self.nameFrame.setToolTip(QtGui.QApplication.translate("qLogin", "Enter login email", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("qLogin", "Pandora Login Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("qLogin", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("qLogin", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.accountButton.setText(QtGui.QApplication.translate("qLogin", "Create Account", None, QtGui.QApplication.UnicodeUTF8))

