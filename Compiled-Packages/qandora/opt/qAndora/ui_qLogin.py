# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI-Layouts/qLogin.ui'
#
# Created: Thu Dec 18 15:07:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qLogin(object):
    def setupUi(self, qLogin):
        qLogin.setObjectName("qLogin")
        qLogin.resize(356, 229)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/qAndora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qLogin.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(qLogin)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nameFrame = QtGui.QFrame(qLogin)
        self.nameFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.nameFrame.setObjectName("nameFrame")
        self.verticalLayout = QtGui.QVBoxLayout(self.nameFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtGui.QLabel(self.nameFrame)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(self.nameFrame)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.verticalLayout_3.addWidget(self.nameFrame)
        self.frame = QtGui.QFrame(qLogin)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.passwordLabel = QtGui.QLabel(self.frame)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_2.addWidget(self.passwordLabel)
        self.passwordEdit = QtGui.QLineEdit(self.frame)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout_2.addWidget(self.passwordEdit)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(qLogin)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginButton = QtGui.QPushButton(self.frame_2)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.accountButton = QtGui.QPushButton(self.frame_2)
        self.accountButton.setObjectName("accountButton")
        self.horizontalLayout.addWidget(self.accountButton)
        self.verticalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(qLogin)
        QtCore.QMetaObject.connectSlotsByName(qLogin)

    def retranslateUi(self, qLogin):
        qLogin.setWindowTitle(QtGui.QApplication.translate("qLogin", "qAndora - Login", None, QtGui.QApplication.UnicodeUTF8))
        self.nameFrame.setToolTip(QtGui.QApplication.translate("qLogin", "Enter login email", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("qLogin", "Pandora Login Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("qLogin", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("qLogin", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.accountButton.setText(QtGui.QApplication.translate("qLogin", "Create Account", None, QtGui.QApplication.UnicodeUTF8))

