from PyQt5 import QtCore, QtGui, QtWidgets
from SettingsSelector import SelectedColor,SelectedButtonColor
from tictac import Tic_Tac_Toe
from Colors import root

class Ui_ToolBox(object):

    def LaunchTicTac(self):
            game_instance = Tic_Tac_Toe()
            game_instance.mainloop()

    def LaunchColor(self):
        print("test")
 

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 478)
        Form.setStyleSheet(SelectedColor)
        self.Game1 = QtWidgets.QPushButton(Form)
        self.Game1.setGeometry(QtCore.QRect(100, 200, 75, 61))
        self.Game1.setObjectName("Game1")
        self.Game1.setStyleSheet(SelectedButtonColor)

        self.Game2 = QtWidgets.QPushButton(Form)
        self.Game2.setGeometry(QtCore.QRect(250, 200, 75, 61))
        self.Game2.setObjectName("Game2")
        self.Game2.setStyleSheet(SelectedButtonColor)

        self.Game3 = QtWidgets.QPushButton(Form)
        self.Game3.setGeometry(QtCore.QRect(400, 200, 75, 61))
        self.Game3.setObjectName("Game3")
        self.Game3.setStyleSheet(SelectedButtonColor)
        self.Game4 = QtWidgets.QPushButton(Form)
        self.Game4.setGeometry(QtCore.QRect(550, 200, 75, 61))
        self.Game4.setObjectName("Game4")
        self.Game4.setStyleSheet(SelectedButtonColor)

        self.BackButton = QtWidgets.QPushButton(Form)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images\BackArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setIconSize(QtCore.QSize(36, 180))
        self.BackButton.setStyleSheet(SelectedButtonColor)
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")

        
        


        self.BackButton.clicked.connect(lambda: Form.close())
        self.Game2.clicked.connect(self.LaunchTicTac)
        self.Game4.clicked.connect(self.LaunchColor)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Game1.setText(_translate("Form", "Snake"))
        self.Game2.setText(_translate("Form", "OXO"))
        self.Game3.setText(_translate("Form", "Dots \'n Boxes"))
        self.Game4.setText(_translate("Form", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ToolBox()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
