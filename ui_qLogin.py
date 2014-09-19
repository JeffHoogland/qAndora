# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qLogin.ui'
#
# Created: Thu Sep 18 23:00:00 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qLogin(object):
    def setupUi(self, qLogin):
        qLogin.setObjectName("qLogin")
        qLogin.resize(400, 212)
        self.buttonBox = QtGui.QDialogButtonBox(qLogin)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
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

        self.retranslateUi(qLogin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), qLogin.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), qLogin.reject)
        QtCore.QMetaObject.connectSlotsByName(qLogin)

    def retranslateUi(self, qLogin):
        qLogin.setWindowTitle(QtGui.QApplication.translate("qLogin", "qAndora - Login", None, QtGui.QApplication.UnicodeUTF8))
        self.nameFrame.setToolTip(QtGui.QApplication.translate("qLogin", "Enter login email", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("qLogin", "Pandora Login Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("qLogin", "Password:", None, QtGui.QApplication.UnicodeUTF8))

