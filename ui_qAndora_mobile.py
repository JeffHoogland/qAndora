# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qAndora-mobile.ui'
#
# Created: Thu Oct 16 21:46:56 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 370)
        MainWindow.setMinimumSize(QtCore.QSize(850, 360))
        MainWindow.setMaximumSize(QtCore.QSize(850, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/qAndora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWidget = QtGui.QTabWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(440, 10, 401, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mainWidget.setFont(font)
        self.mainWidget.setStyleSheet("QTabBar::tab { height: 100px; width: 90px; }")
        self.mainWidget.setTabPosition(QtGui.QTabWidget.East)
        self.mainWidget.setObjectName("mainWidget")
        self.currentTab = QtGui.QWidget()
        self.currentTab.setObjectName("currentTab")
        self.albumImage = QtGui.QLabel(self.currentTab)
        self.albumImage.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.albumImage.setMinimumSize(QtCore.QSize(300, 200))
        self.albumImage.setMaximumSize(QtCore.QSize(0, 0))
        self.albumImage.setScaledContents(True)
        self.albumImage.setObjectName("albumImage")
        self.positionFrame = QtGui.QFrame(self.currentTab)
        self.positionFrame.setGeometry(QtCore.QRect(60, 130, 181, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 147, 145, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 147, 145, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 147, 145, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.positionFrame.setPalette(palette)
        self.positionFrame.setAutoFillBackground(True)
        self.positionFrame.setFrameShape(QtGui.QFrame.Panel)
        self.positionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.positionFrame.setObjectName("positionFrame")
        self.positionLabel = QtGui.QLabel(self.positionFrame)
        self.positionLabel.setGeometry(QtCore.QRect(15, 10, 151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 147, 145, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 147, 145, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 236, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 147, 145, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 110, 108, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 220, 217, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.positionLabel.setPalette(palette)
        self.positionLabel.setAutoFillBackground(True)
        self.positionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLabel.setObjectName("positionLabel")
        self.mainWidget.addTab(self.currentTab, "")
        self.historyTab = QtGui.QWidget()
        self.historyTab.setObjectName("historyTab")
        self.historyList = QtGui.QListWidget(self.historyTab)
        self.historyList.setGeometry(QtCore.QRect(0, 0, 311, 211))
        self.historyList.setMinimumSize(QtCore.QSize(285, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.historyList.setFont(font)
        self.historyList.setObjectName("historyList")
        self.mainWidget.addTab(self.historyTab, "")
        self.infoFrame = QtGui.QFrame(self.centralwidget)
        self.infoFrame.setGeometry(QtCore.QRect(360, 230, 481, 131))
        self.infoFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.infoFrame.setObjectName("infoFrame")
        self.titleLabel = QtGui.QLabel(self.infoFrame)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setIndent(-1)
        self.titleLabel.setOpenExternalLinks(True)
        self.titleLabel.setObjectName("titleLabel")
        self.albumLabel = QtGui.QLabel(self.infoFrame)
        self.albumLabel.setGeometry(QtCore.QRect(10, 49, 461, 31))
        self.albumLabel.setWordWrap(True)
        self.albumLabel.setIndent(-1)
        self.albumLabel.setOpenExternalLinks(True)
        self.albumLabel.setObjectName("albumLabel")
        self.artistLabel = QtGui.QLabel(self.infoFrame)
        self.artistLabel.setGeometry(QtCore.QRect(10, 89, 461, 31))
        self.artistLabel.setOpenExternalLinks(True)
        self.artistLabel.setObjectName("artistLabel")
        self.loveButton = QtGui.QPushButton(self.centralwidget)
        self.loveButton.setGeometry(QtCore.QRect(10, 120, 125, 100))
        self.loveButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loveButton.setIcon(icon1)
        self.loveButton.setIconSize(QtCore.QSize(75, 75))
        self.loveButton.setObjectName("loveButton")
        self.tiredButton = QtGui.QPushButton(self.centralwidget)
        self.tiredButton.setGeometry(QtCore.QRect(150, 120, 125, 100))
        self.tiredButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/tired.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tiredButton.setIcon(icon2)
        self.tiredButton.setIconSize(QtCore.QSize(75, 75))
        self.tiredButton.setObjectName("tiredButton")
        self.banButton = QtGui.QPushButton(self.centralwidget)
        self.banButton.setGeometry(QtCore.QRect(290, 120, 125, 100))
        self.banButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/ban.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.banButton.setIcon(icon3)
        self.banButton.setIconSize(QtCore.QSize(75, 75))
        self.banButton.setObjectName("banButton")
        self.playPauseButton = QtGui.QPushButton(self.centralwidget)
        self.playPauseButton.setGeometry(QtCore.QRect(10, 10, 125, 100))
        self.playPauseButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playPauseButton.setIcon(icon4)
        self.playPauseButton.setIconSize(QtCore.QSize(75, 75))
        self.playPauseButton.setObjectName("playPauseButton")
        self.skipButton = QtGui.QPushButton(self.centralwidget)
        self.skipButton.setGeometry(QtCore.QRect(150, 10, 125, 100))
        self.skipButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skipButton.setIcon(icon5)
        self.skipButton.setIconSize(QtCore.QSize(75, 75))
        self.skipButton.setObjectName("skipButton")
        self.settingsButton = QtGui.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(290, 10, 125, 100))
        self.settingsButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon6)
        self.settingsButton.setIconSize(QtCore.QSize(75, 75))
        self.settingsButton.setObjectName("settingsButton")
        self.lowerFrame = QtGui.QFrame(self.centralwidget)
        self.lowerFrame.setGeometry(QtCore.QRect(10, 230, 331, 131))
        self.lowerFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lowerFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.lowerFrame.setObjectName("lowerFrame")
        self.volumeSlider = QtGui.QSlider(self.lowerFrame)
        self.volumeSlider.setGeometry(QtCore.QRect(10, 30, 301, 41))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 75)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.stationBox = QtGui.QComboBox(self.lowerFrame)
        self.stationBox.setGeometry(QtCore.QRect(10, 90, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stationBox.setFont(font)
        self.stationBox.setObjectName("stationBox")
        self.volumeLabel = QtGui.QLabel(self.lowerFrame)
        self.volumeLabel.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.volumeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.volumeLabel.setObjectName("volumeLabel")
        self.stationLabel = QtGui.QLabel(self.lowerFrame)
        self.stationLabel.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.stationLabel.setObjectName("stationLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "qAndora - Internet Radio", None, QtGui.QApplication.UnicodeUTF8))
        self.albumImage.setText(QtGui.QApplication.translate("MainWindow", "Album art here", None, QtGui.QApplication.UnicodeUTF8))
        self.positionLabel.setText(QtGui.QApplication.translate("MainWindow", "Track Position", None, QtGui.QApplication.UnicodeUTF8))
        self.mainWidget.setTabText(self.mainWidget.indexOf(self.currentTab), QtGui.QApplication.translate("MainWindow", "Playing", None, QtGui.QApplication.UnicodeUTF8))
        self.mainWidget.setTabText(self.mainWidget.indexOf(self.historyTab), QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Title</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.albumLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Album</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.artistLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Artist</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.loveButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Favorite Song", None, QtGui.QApplication.UnicodeUTF8))
        self.tiredButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Set song to tired", None, QtGui.QApplication.UnicodeUTF8))
        self.banButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Ban song", None, QtGui.QApplication.UnicodeUTF8))
        self.playPauseButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Pause Song", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Skip Song", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeSlider.setToolTip(QtGui.QApplication.translate("MainWindow", "Adjust Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Volume:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.stationLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Station:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

