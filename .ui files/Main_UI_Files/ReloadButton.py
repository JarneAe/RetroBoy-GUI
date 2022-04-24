# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Prototype.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 567)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonRetro = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRetro.setGeometry(QtCore.QRect(40, 70, 191, 191))
        self.ButtonRetro.setAutoFillBackground(False)
        self.ButtonRetro.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Pictures/retro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRetro.setIcon(icon)
        self.ButtonRetro.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRetro.setCheckable(False)
        self.ButtonRetro.setAutoExclusive(False)
        self.ButtonRetro.setObjectName("ButtonRetro")
        self.ButtonFire = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonFire.setGeometry(QtCore.QRect(270, 70, 191, 191))
        self.ButtonFire.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Pictures/firefox.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonFire.setIcon(icon1)
        self.ButtonFire.setIconSize(QtCore.QSize(256, 256))
        self.ButtonFire.setObjectName("ButtonFire")
        self.ButtonRasp = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRasp.setGeometry(QtCore.QRect(510, 70, 191, 191))
        self.ButtonRasp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Pictures/Raspi-PGB001.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRasp.setIcon(icon2)
        self.ButtonRasp.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRasp.setObjectName("ButtonRasp")
        self.ButtenNet = QtWidgets.QPushButton(self.centralwidget)
        self.ButtenNet.setGeometry(QtCore.QRect(40, 280, 191, 191))
        self.ButtenNet.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Pictures/netflix-png-icon-19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtenNet.setIcon(icon3)
        self.ButtenNet.setIconSize(QtCore.QSize(256, 256))
        self.ButtenNet.setObjectName("ButtenNet")
        self.ButtonDisney = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDisney.setGeometry(QtCore.QRect(270, 280, 191, 191))
        self.ButtonDisney.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../Pictures/apps.9878.14495311847124170.294fed91-ba37-4b8a-83dc-b4098d97cebb.df2390ec-16fb-4849-a952-5f4780c309bd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonDisney.setIcon(icon4)
        self.ButtonDisney.setIconSize(QtCore.QSize(256, 256))
        self.ButtonDisney.setObjectName("ButtonDisney")
        self.ButtonYT = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonYT.setGeometry(QtCore.QRect(510, 280, 191, 191))
        self.ButtonYT.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../Pictures/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonYT.setIcon(icon5)
        self.ButtonYT.setIconSize(QtCore.QSize(256, 256))
        self.ButtonYT.setObjectName("ButtonYT")
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(700, 480, 51, 41))
        self.ButtonExit.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../Pictures/31784.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonExit.setIcon(icon6)
        self.ButtonExit.setIconSize(QtCore.QSize(36, 180))
        self.ButtonExit.setObjectName("ButtonExit")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(720, 0, 47, 13))
        self.Time.setText("")
        self.Time.setObjectName("Time")
        self.Date = QtWidgets.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(640, 0, 47, 13))
        self.Date.setText("")
        self.Date.setObjectName("Date")
        self.ButtonSettings = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSettings.setGeometry(QtCore.QRect(630, 480, 51, 41))
        self.ButtonSettings.setText("")
        self.ButtonSettings.setIcon(icon6)
        self.ButtonSettings.setIconSize(QtCore.QSize(36, 180))
        self.ButtonSettings.setObjectName("ButtonSettings")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(115, 12, 47, 13))
        self.label_2.setObjectName("label_2")
        self.ButtonReload = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonReload.setGeometry(QtCore.QRect(10, 480, 51, 41))
        self.ButtonReload.setText("")
        self.ButtonReload.setIcon(icon6)
        self.ButtonReload.setIconSize(QtCore.QSize(36, 180))
        self.ButtonReload.setObjectName("ButtonReload")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Recent Snake Score:"))
        self.label_2.setText(_translate("MainWindow", "N/A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
