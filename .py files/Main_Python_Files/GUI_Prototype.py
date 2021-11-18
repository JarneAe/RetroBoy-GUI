from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
from PyQt5.QtWidgets import QMessageBox

class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(773, 567)
        GUI.setAutoFillBackground(False)
        GUI.setStyleSheet("\n""")
        self.centralwidget = QtWidgets.QWidget(GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonRetro = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRetro.setGeometry(QtCore.QRect(40, 70, 191, 191))
        self.ButtonRetro.setAutoFillBackground(False)
        self.ButtonRetro.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\\retro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRetro.setIcon(icon)
        self.ButtonRetro.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRetro.setCheckable(False)
        self.ButtonRetro.setAutoExclusive(False)
        self.ButtonRetro.setObjectName("ButtonRetro")
        self.ButtonFire = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonFire.setGeometry(QtCore.QRect(270, 70, 191, 191))
        self.ButtonFire.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\\firefox.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonFire.setIcon(icon1)
        self.ButtonFire.setIconSize(QtCore.QSize(256, 256))
        self.ButtonFire.setObjectName("ButtonFire")
        self.ButtonRasp = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRasp.setGeometry(QtCore.QRect(510, 70, 191, 191))
        self.ButtonRasp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images\Raspi-PGB001.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRasp.setIcon(icon2)
        self.ButtonRasp.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRasp.setObjectName("ButtonRasp")
        self.ButtenNet = QtWidgets.QPushButton(self.centralwidget)
        self.ButtenNet.setGeometry(QtCore.QRect(40, 280, 191, 191))
        self.ButtenNet.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images\\netflix-png-icon-19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtenNet.setIcon(icon3)
        self.ButtenNet.setIconSize(QtCore.QSize(256, 256))
        self.ButtenNet.setObjectName("ButtenNet")
        self.ButtonDisney = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDisney.setGeometry(QtCore.QRect(270, 280, 191, 191))
        self.ButtonDisney.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images\\apps.9878.14495311847124170.294fed91-ba37-4b8a-83dc-b4098d97cebb.df2390ec-16fb-4849-a952-5f4780c309bd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonDisney.setIcon(icon4)
        self.ButtonDisney.setIconSize(QtCore.QSize(256, 256))
        self.ButtonDisney.setObjectName("ButtonDisney")
        self.ButtonYT = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonYT.setGeometry(QtCore.QRect(510, 280, 191, 191))
        self.ButtonYT.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images\\unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonYT.setIcon(icon5)
        self.ButtonYT.setIconSize(QtCore.QSize(256, 256))
        self.ButtonYT.setObjectName("ButtonYT")
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(700, 480, 51, 41))
        self.ButtonExit.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images\\31784.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonExit.setIcon(icon6)
        self.ButtonExit.setIconSize(QtCore.QSize(36, 180))
        self.ButtonExit.setObjectName("ButtonExit")
        GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        GUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI)
        self.statusbar.setObjectName("statusbar")
        GUI.setStatusBar(self.statusbar)

        self.ButtonRetro.clicked.connect(self.OpenRetro)
        self.ButtonRasp.clicked.connect(self.GoToDesktop)
        self.ButtonFire.clicked.connect(self.OpenFire)
        self.ButtenNet.clicked.connect(self.OpenNetflix)
        self.ButtonDisney.clicked.connect(self.OpenDisney)
        self.ButtonYT.clicked.connect(self.OpenYoutube)
        self.ButtonExit.clicked.connect(self.show_popup)
        
        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)


    def OpenRetro(self):
        os.startfile("C:\\Users\\JarneA408\\AppData\\Roaming\\RetroArch\\retroarch.exe")

    def OpenFire(self):
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

    def GoToDesktop(self):
        pass

    def OpenNetflix(self):
        webbrowser.open('https://Netflix.com')

    def OpenDisney(self):
        webbrowser.open('https://Disneyplus.com')

    def OpenYoutube(self):
        webbrowser.open('https://Youtube.com')

    def ShutdownDevice(self):
        os.system("shutdown /s /t 1")


    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "GUI"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirmation")
        msg.setText("Are you sure you want to shutdown?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    def popup_button(self,i):
        print(i.text())

        if i.text() == "&Yes":
            print("shutdown")
            self.ShutdownDevice()
        else:
            pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())
