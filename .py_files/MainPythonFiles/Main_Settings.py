from tkinter.tix import Select
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *
from cv2 import Formatter_FMT_C 
from SettingsSelector import SelectedColor,DateFormat,TimeFormat,SelectedButtonColor
from datetime import datetime
from PushToJson import PushBColor,PushTimeFormat,PushDateFormat,PushButtonColor
import random
from getbcolor import recognize_color
import re 

class Ui_Settings(object):

    def setupUi(self, Form):
        Form.setStyleSheet(SelectedColor)
        Form.setObjectName("Form")
        Form.resize(661, 500)

        self.ColorLabel = QtWidgets.QLabel(Form)
        self.ColorLabel.setGeometry(QtCore.QRect(230, 140, 61, 16))
        self.ColorLabel.setObjectName("ColorLabel")

        self.ColorBox = QtWidgets.QComboBox(Form)
        self.ColorBox.setGeometry(QtCore.QRect(310, 140, 101, 22))
        self.ColorBox.setObjectName("ColorBox")
        self.ColorBox.addItem("")
        self.ColorBox.addItem("")
        self.ColorBox.addItem("")
        self.ColorBox.addItem("")

        self.DateLabel = QtWidgets.QLabel(Form)
        self.DateLabel.setGeometry(QtCore.QRect(230, 190, 61, 16))
        self.DateLabel.setObjectName("DateLabel")

        self.DateBox = QtWidgets.QComboBox(Form)
        self.DateBox.setGeometry(QtCore.QRect(310, 190, 101, 22))
        self.DateBox.setObjectName("DateBox")
        self.DateBox.addItem("")
        self.DateBox.addItem("")

        self.HourLabel = QtWidgets.QLabel(Form)
        self.HourLabel.setGeometry(QtCore.QRect(230, 240, 61, 16))
        self.HourLabel.setObjectName("HourLabel")


        self.HourBox = QtWidgets.QComboBox(Form)
        self.HourBox.setGeometry(QtCore.QRect(310, 240, 101, 22))
        self.HourBox.setObjectName("HourBox")
        self.HourBox.addItem("")
        self.HourBox.addItem("")

        self.BackButton = QtWidgets.QPushButton(Form)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setIconSize(QtCore.QSize(36, 180))
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")
        self.BackButton.setStyleSheet(SelectedButtonColor)

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(220, 170, 201, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(220, 220, 201, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.UpdateButton = QtWidgets.QPushButton(Form)
        self.UpdateButton.setGeometry(QtCore.QRect(250, 460, 111, 23))
        self.UpdateButton.setObjectName("UpdateButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 50, 47, 13))
        self.label.setObjectName("label")

        self.pickerButton = QtWidgets.QPushButton(Form)
        self.pickerButton.setGeometry(QtCore.QRect(440, 140, 171, 23))
        self.pickerButton.setObjectName("pickerButton")
        
        self.RandomBColor = QtWidgets.QPushButton(Form)
        self.RandomBColor.setGeometry(QtCore.QRect(480, 170, 75, 23))
        self.RandomBColor.setObjectName("RandomBColor")

        self.ButtonColor = QtWidgets.QPushButton(Form)
        self.ButtonColor.setGeometry(QtCore.QRect(230, 320, 171, 23))
        self.ButtonColor.setObjectName("ButtonColor")

        self.colorshow1 = QtWidgets.QLabel(Form)
        self.colorshow1.setGeometry(QtCore.QRect(230, 440, 101, 16))
        self.colorshow1.setStyleSheet("QLabel {color: black;}")
        self.colorshow1.setObjectName("colorshow1")
        self.colorshow2 = QtWidgets.QLabel(Form)
        self.colorshow2.setGeometry(QtCore.QRect(350, 440, 181, 16))
        self.colorshow2.setObjectName("colorshow2")

        self.ResetDefault = QtWidgets.QPushButton(Form)
        self.ResetDefault.setGeometry(QtCore.QRect(544, 460, 101, 23))
        self.ResetDefault.setObjectName("ResetDefault")

        self.BackButton.clicked.connect(lambda: Form.close())
        self.UpdateButton.clicked.connect(self.UpdateSettings)
        self.pickerButton.clicked.connect(self.Color_Picker)
        self.RandomBColor.clicked.connect(self.Random_Color)
        self.ButtonColor.clicked.connect(self.Color_Picker_Button)
        self.ResetDefault.clicked.connect(self.Reset_Default)


        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label.setText((""))
    
        now = datetime.now()

        if DateFormat == now.strftime("%d-%m-%y"):
            self.DateBox.setCurrentIndex(0)
        else:
            self.DateBox.setCurrentIndex(1)
            
        if TimeFormat == "%I:%M %p":
            self.HourBox.setCurrentIndex(0)
        else:
            self.HourBox.setCurrentIndex(1)

        if SelectedColor == "background-color:rgb(71, 82, 99);":
            self.ColorBox.setCurrentIndex(0)
        elif SelectedColor == "background-color:rgb(215, 227, 245);":
            self.ColorBox.setCurrentIndex(1)
        elif SelectedColor == "background-color:rgb(220,20,60);":
            self.ColorBox.setCurrentIndex(2)
        else:
            self.ColorBox.setCurrentIndex(3)
    
    def Reset_Default(self):
        PushBColor("Dark")
        PushButtonColor("Default")
        PushTimeFormat("24 Hours")
        PushDateFormat("Day/Month/Year")
        self.label.setText(("Changes will be applied after the app has been restarted."))
        self.label.adjustSize()


    def Color_Picker_Button(self):
        color = QColorDialog.getColor()
        ColorGet = color.getRgb()
        FinalColor = ColorGet[0:3]

        PushButtonColor(FinalColor)

        self.label.setText(("Changes will be applied after the app has been restarted."))
        self.label.adjustSize()
        return FinalColor




    def Random_Color(self):
        RGB = f'{random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)}'
        PushBColor(RGB)
        RGB = f'{random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)}'
        PushButtonColor(RGB)
        self.label.setText(("Changes will be applied after the app has been restarted."))
        self.label.adjustSize()

        
    def Color_Picker(self):
        color = QColorDialog.getColor()
        ColorGet = color.getRgb()
        FinalColor = ColorGet[0:3]

        PushBColor(FinalColor)

        self.label.setText(("Changes will be applied after the app has been restarted."))
        self.label.adjustSize()
        return FinalColor

        
    def UpdateSettings(self):

        if self.ColorBox.currentText() != 'Custom':
            BColor = self.ColorBox.currentText()
            PushBColor(BColor)
            
        DateFormat = self.DateBox.currentText()
        TimeFormat = self.HourBox.currentText()
        
        PushTimeFormat(TimeFormat)       
        PushDateFormat(DateFormat)

        self.label.setText(("Changes will be applied after the app has been restarted."))
        self.label.adjustSize()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.ColorLabel.setText(_translate("Form1", "Color mode"))
        self.ColorBox.setItemText(0, _translate("Form2", "Dark"))
        self.ColorBox.setItemText(1, _translate("Form3", "Light"))
        self.ColorBox.setItemText(2, _translate("Form4", "Pink"))
        self.ColorBox.setItemText(3, _translate("Form5", "Custom"))

        self.DateLabel.setText(_translate("Form6", "Date Format"))
        self.DateBox.setItemText(0, _translate("Form7", "Day/Month/Year"))
        self.DateBox.setItemText(1, _translate("Form8", "Month/Day/Year"))

        self.HourLabel.setText(_translate("Form9", "Hour Format"))
        self.HourBox.setItemText(0, _translate("Form10", "AM/PM"))
        self.HourBox.setItemText(1, _translate("Form11", "24 Hours"))

        self.UpdateButton.setText(_translate("Form12", "Update Settings"))
        self.label.setText(_translate("Form13", ""))
        self.label.setText(_translate("Form14", "TextLabel"))
        self.pickerButton.setText(_translate("Form15", "Press Here For Custom Color"))
        self.RandomBColor.setText(_translate("Form16", "Surprise me!"))
        self.ResetDefault.setText(_translate("Form", "Reset To Default"))
        self.ButtonColor.setText(_translate("form17","Click here for custom button color"))
        regexednumbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', SelectedColor)]
        self.colorshow1.setText(_translate("Form", "The selected color is: "))
        self.colorshow2.setText(_translate("Form", recognize_color(int(regexednumbers[0]),int(regexednumbers[1]),int(regexednumbers[2]))))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Settings()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())