from PyQt5 import QtCore, QtGui, QtWidgets
from GUI_Prototype import Ui_GUI
global SelectedColor 



class Ui_Form(object):
    def setupUi(self, Form):

        Form.setStyleSheet("background-color:rgb(71, 82, 99);")
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
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")

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


        self.BackButton.clicked.connect(lambda: Form.close())
        self.UpdateButton.clicked.connect(self.UpdateSettings)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

    def UpdateSettings(self):
        SelectedColor = self.ColorBox.currentText()
        if self.ColorBox.currentText() == "Dark":
            SelectedColor = "background-color:rgb(71, 82, 99);"
            print("Dark")
        else:
            SelectedColor = "background-color:rgb(232, 230, 223);"
            print("Light")

        SelectedDateFormat = self.DateBox.currentText()
        print(SelectedDateFormat)
        SelectedHour = self.HourBox.currentText()
        print(SelectedHour)
        Ui_GUI.RefreshGUI(self)
        return SelectedColor,SelectedDateFormat,SelectedHour
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.ColorLabel.setText(_translate("Form", "Color mode"))
        self.ColorBox.setItemText(0, _translate("Form", "Dark"))
        self.ColorBox.setItemText(1, _translate("Form", "Light"))
    

        self.DateLabel.setText(_translate("Form", "Date Format"))
        self.DateBox.setItemText(0, _translate("Form", "Day/Month/Year"))
        self.DateBox.setItemText(1, _translate("Form", "Month/Day/Year"))

        self.HourLabel.setText(_translate("Form", "Hour Format"))
        self.HourBox.setItemText(0, _translate("Form", "AM/PM"))
        self.HourBox.setItemText(1, _translate("Form", "24 Hours"))

        self.UpdateButton.setText(_translate("Form", "Update Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())