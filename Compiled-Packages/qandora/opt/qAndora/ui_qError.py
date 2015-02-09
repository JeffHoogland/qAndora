# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI-Layouts/qError.ui'
#
# Created: Sat Feb  7 19:49:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qError(object):
    def setupUi(self, qError):
        qError.setObjectName("qError")
        qError.resize(250, 100)
        qError.setMinimumSize(QtCore.QSize(250, 100))
        qError.setMaximumSize(QtCore.QSize(250, 100))
        self.gridLayout_3 = QtGui.QGridLayout(qError)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(qError)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(qError)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(8)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(qError)
        QtCore.QMetaObject.connectSlotsByName(qError)

    def retranslateUi(self, qError):
        qError.setWindowTitle(QtGui.QApplication.translate("qError", "qAndora - ERROR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("qError", "Houston we have a problem!!!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("qError", "Most likely you\'ve requested too many playlists. Try back in a little while.", None, QtGui.QApplication.UnicodeUTF8))

