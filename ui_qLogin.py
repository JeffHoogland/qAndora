# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qLogin.ui'
#
# Created: Thu Sep 18 22:35:18 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qLogin(object):
    def setupUi(self, qLogin):
        qLogin.setObjectName("qLogin")
        qLogin.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(qLogin)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.userName = QtGui.QFrame(qLogin)
        self.userName.setGeometry(QtCore.QRect(20, 20, 361, 51))
        self.userName.setFrameShape(QtGui.QFrame.StyledPanel)
        self.userName.setFrameShadow(QtGui.QFrame.Raised)
        self.userName.setObjectName("userName")

        self.retranslateUi(qLogin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), qLogin.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), qLogin.reject)
        QtCore.QMetaObject.connectSlotsByName(qLogin)

    def retranslateUi(self, qLogin):
        qLogin.setWindowTitle(QtGui.QApplication.translate("qLogin", "qAndora - Login", None, QtGui.QApplication.UnicodeUTF8))

