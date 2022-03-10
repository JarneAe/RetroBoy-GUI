from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
from PyQt5.QtWidgets import QMessageBox,QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime
import datetime
from datetime import date, datetime

import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt,QTimer
from Main_Settings import *
import json

#Reads json file and loads it to something readable
with open(".py_files\MainPythonFiles\Settings.json") as json_file:
    data = json.load(json_file)

class Ui_GUI(object):

    def openSettings(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, GUI):
        
        if data["BColor"] == 'Dark':
            print('Dark color found')
            SelectedColor = "background-color:rgb(71, 82, 99);"
        elif(data["BColor"] == 'Light'):
            SelectedColor = "background-color:rgb(215, 227, 245);"
        elif(data["BColor"] == 'Pink'):
            SelectedColor = "background-color:rgb(220,20,60);"
        else:
            SelectedColor = "background-color:rgb(71, 82, 99);"
        
        now = datetime.now()

        if data["Date"] == 'Day/Month/Year':
            DateFormat = now.strftime("%d-%m-%y")
        else:
            DateFormat = now.strftime("%m-%d-%y")

        GUI.setObjectName("GUI")
        GUI.resize(773, 567)
        GUI.setAutoFillBackground(False)
        GUI.setStyleSheet(SelectedColor)
        self.centralwidget = QtWidgets.QWidget(GUI)
        self.centralwidget.setObjectName("centralwidget")
        
        #Button for emulator
        self.ButtonRetro = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRetro.setGeometry(QtCore.QRect(40, 70, 191, 191))
        self.ButtonRetro.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\JarneA408\Documents\2021-2022\GIP\repo\RetroBoy-GUI\Images\retro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRetro.setIcon(icon)
        self.ButtonRetro.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRetro.setCheckable(False)
        self.ButtonRetro.setAutoExclusive(False)
        self.ButtonRetro.setObjectName("ButtonRetro")

        #Button for firefox
        self.ButtonFire = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonFire.setGeometry(QtCore.QRect(270, 70, 191, 191))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"C:\Users\JarneA408\Documents\2021-2022\GIP\repo\RetroBoy-GUI\Images\firefox.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonFire.setIcon(icon1)
        self.ButtonFire.setIconSize(QtCore.QSize(256, 256))
        self.ButtonFire.setObjectName("ButtonFire")

        #Button for desktop
        self.ButtonRasp = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRasp.setGeometry(QtCore.QRect(510, 70, 191, 191))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"C:\Users\JarneA408\Documents\2021-2022\GIP\repo\RetroBoy-GUI\Images\Raspbian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRasp.setIcon(icon2)
        self.ButtonRasp.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRasp.setObjectName("ButtonRasp")

        #Button for Netflix
        self.ButtenNet = QtWidgets.QPushButton(self.centralwidget)
        self.ButtenNet.setGeometry(QtCore.QRect(40, 280, 191, 191))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\JarneA408\\Documents\\2021-2022\\GIP\\repo\\RetroBoy-GUI\\Images\\netflix-png-icon-19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtenNet.setIcon(icon3)
        self.ButtenNet.setIconSize(QtCore.QSize(256, 256))
        self.ButtenNet.setObjectName("ButtenNet")

        #Button for disney+
        self.ButtonDisney = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDisney.setGeometry(QtCore.QRect(270, 280, 191, 191))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"C:\Users\JarneA408\Documents\2021-2022\GIP\repo\RetroBoy-GUI\Images\DisneyIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonDisney.setIcon(icon4)
        self.ButtonDisney.setIconSize(QtCore.QSize(256, 256))
        self.ButtonDisney.setObjectName("ButtonDisney")

        #Button for youtube
        self.ButtonYT = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonYT.setGeometry(QtCore.QRect(510, 280, 191, 191))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\JarneA408\\Documents\\2021-2022\\GIP\\repo\\RetroBoy-GUI\\Images\\Youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonYT.setIcon(icon5)
        self.ButtonYT.setIconSize(QtCore.QSize(256, 256))
        self.ButtonYT.setObjectName("ButtonYT")

        #Button for shutdown
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(700, 480, 51, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\JarneA408\\Documents\\2021-2022\\GIP\\repo\\RetroBoy-GUI\\Images\\31784.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonExit.setIcon(icon6)
        self.ButtonExit.setIconSize(QtCore.QSize(36, 180))
        self.ButtonExit.setObjectName("ButtonExit")
        self.ButtonExit.setStyleSheet("background-color: white")

        #Time display
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(700, 0, 47, 13))
        self.Time.setText(self.clock())
        self.Time.setFont(QtGui.QFont('Arial',12))
        self.Time.adjustSize()
        self.Time.setObjectName("Time")
        self.timer=QTimer()
        self.timer.start(200)
        self.timer.timeout.connect(self.clock)


        #Date display
        self.Date = QtWidgets.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(600, 0, 47, 13))
        self.Date.setText(DateFormat)
        self.Date.setObjectName("Date")
        self.Date.setFont(QtGui.QFont('Arial',12))
        self.Date.adjustSize()

        #Button settings
        self.ButtonSettings = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSettings.setGeometry(QtCore.QRect(630, 480, 51, 41))
        self.ButtonSettings.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images\\SettingsIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSettings.setIcon(icon7)
        self.ButtonSettings.setIconSize(QtCore.QSize(36, 180))
        self.ButtonSettings.setObjectName("ButtonSettings")

        #assigning widget
        GUI.setCentralWidget(self.centralwidget)

        #connection setup
        self.ButtonRetro.clicked.connect(self.OpenRetro)
        self.ButtonRasp.clicked.connect(self.GoToDesktop)
        self.ButtonFire.clicked.connect(self.OpenFire)
        self.ButtenNet.clicked.connect(self.OpenNetflix)
        self.ButtonDisney.clicked.connect(self.OpenDisney)
        self.ButtonYT.clicked.connect(self.OpenYoutube)
        self.ButtonExit.clicked.connect(self.show_popup)
        self.ButtonSettings.clicked.connect(self.openSettings)
        
        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def clock(self):
        while True:
            self.Time.setText(str(datetime.now().strftime("%H:%M:%S")))
            timetext = str(datetime.now().strftime("%H:%M:%S"))
            return timetext
            
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