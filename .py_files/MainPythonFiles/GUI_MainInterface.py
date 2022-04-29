from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from datetime import datetime
import sys
from PyQt5.QtCore import QTimer
from Main_Settings import Ui_Settings
from ToolBox import Ui_ToolBox
from SettingsSelector import SelectedColor,DateFormat,TimeFormat,SelectedButtonColor
from SnakeScoreGetter import SnakeScore



class Ui_Main_Interface(object):

    #link to the settings widget(other file)
    def openSettings(self):
       
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Settings()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def OpenToolbox(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ToolBox()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, GUI):
        global GUIRef
        GUIRef = GUI 


        #GUI frame setup
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
        icon.addPixmap(QtGui.QPixmap(r"Images\retro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRetro.setIcon(icon)
        self.ButtonRetro.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRetro.setCheckable(False)
        self.ButtonRetro.setAutoExclusive(False)
        self.ButtonRetro.setObjectName("ButtonRetro")

        #Button for firefox
        self.ButtonFire = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonFire.setGeometry(QtCore.QRect(270, 70, 191, 191))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"Images\firefox.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonFire.setIcon(icon1)
        self.ButtonFire.setIconSize(QtCore.QSize(256, 256))
        self.ButtonFire.setObjectName("ButtonFire")

        #Button for desktop
        self.ButtonRasp = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRasp.setGeometry(QtCore.QRect(510, 70, 191, 191))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"Images\Raspbian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRasp.setIcon(icon2)
        self.ButtonRasp.setIconSize(QtCore.QSize(256, 256))
        self.ButtonRasp.setObjectName("ButtonRasp")

        #Button for Netflix
        self.ButtenNet = QtWidgets.QPushButton(self.centralwidget)
        self.ButtenNet.setGeometry(QtCore.QRect(40, 280, 191, 191))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"Images\netflix-png-icon-19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtenNet.setIcon(icon3)
        self.ButtenNet.setIconSize(QtCore.QSize(256, 256))
        self.ButtenNet.setObjectName("ButtenNet")

        #Button for disney+
        self.ButtonDisney = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDisney.setGeometry(QtCore.QRect(270, 280, 191, 191))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"Images\\DisneyIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonDisney.setIcon(icon4)
        self.ButtonDisney.setIconSize(QtCore.QSize(256, 256))
        self.ButtonDisney.setObjectName("ButtonDisney")

        #Button for youtube
        self.ButtonYT = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonYT.setGeometry(QtCore.QRect(510, 280, 191, 191))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images\Youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonYT.setIcon(icon5)
        self.ButtonYT.setIconSize(QtCore.QSize(256, 256))
        self.ButtonYT.setObjectName("ButtonYT")

        #Button for shutdown
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(700, 480, 51, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images\\31784.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonExit.setIcon(icon6)
        self.ButtonExit.setIconSize(QtCore.QSize(36, 180))
        self.ButtonExit.setObjectName("ButtonExit")
        self.ButtonExit.setStyleSheet(SelectedButtonColor)

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
        self.ButtonSettings.setGeometry(QtCore.QRect(70, 480, 51, 41))
        self.ButtonSettings.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images\\SettingsIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSettings.setIcon(icon7)
        self.ButtonSettings.setIconSize(QtCore.QSize(36, 180))
        self.ButtonSettings.setObjectName("ButtonSettings")
        self.ButtonSettings.setStyleSheet(SelectedButtonColor)

        self.ButtonReload = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonReload.setGeometry(QtCore.QRect(10, 480, 51, 41))
        self.ButtonReload.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images\\ReloadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonReload.setIcon(icon8)
        self.ButtonReload.setIconSize(QtCore.QSize(36, 180))
        self.ButtonReload.setObjectName("ButtonReload")
        self.ButtonReload.setStyleSheet(SelectedButtonColor)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 150, 25))
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('Arial',12))
        self.label.adjustSize()

        self.GameToolbox = QtWidgets.QPushButton(self.centralwidget)
        self.GameToolbox.setGeometry(QtCore.QRect(130, 480, 51, 41))
        self.GameToolbox.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Images\\ToolBox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GameToolbox.setIcon(icon9)
        self.GameToolbox.setIconSize(QtCore.QSize(36, 180))
        self.GameToolbox.setStyleSheet(SelectedButtonColor)
        self.GameToolbox.setObjectName("GameToolbox")

        #connection setup
        self.ButtonRetro.clicked.connect(self.OpenRetro)
        self.ButtonRasp.clicked.connect(self.GoToDesktop)
        self.ButtonFire.clicked.connect(self.OpenFire)
        self.ButtenNet.clicked.connect(self.OpenNetflix)
        self.ButtonDisney.clicked.connect(self.OpenDisney)
        self.ButtonYT.clicked.connect(self.OpenYoutube)
        self.ButtonExit.clicked.connect(self.show_popup)
        self.ButtonSettings.clicked.connect(self.openSettings)
        self.ButtonReload.clicked.connect(self.ReloadProgram)
        self.GameToolbox.clicked.connect(self.OpenToolbox)
        
        #assigning widget
        GUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

        return SelectedColor
    
    def ReloadProgram(self):
        GUIRef.close()
        os.system('python ".py_files\MainPythonFiles\GUI_Launch.py"')


    def clock(self):
        while True:
            self.Time.setText(str(datetime.now().strftime(TimeFormat)))
            timetext = str(datetime.now().strftime(TimeFormat))
            return timetext
            
    def OpenRetro(self):
        os.startfile("C:\\Users\\JarneA408\\AppData\\Roaming\\RetroArch\\retroarch.exe")

    def OpenFire(self):
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

    def OpenNetflix(self):
        webbrowser.open('https://Netflix.com')

    def OpenDisney(self):
        webbrowser.open('https://Disneyplus.com')

    def OpenYoutube(self):
        webbrowser.open('https://Youtube.com')

    def ShutdownDevice(self):
        os.system("shutdown /s /t 1")

    def GoToDesktop(self):
        pass

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "GUI"))
        self.label.setText(_translate("MainWindow", f"Last Session High-Score: {SnakeScore} "))
        self.label.adjustSize()

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
    
    
#can be removed (needed for testing right now)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_Main_Interface()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())

    