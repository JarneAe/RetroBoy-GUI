import GUI_Prototype
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
from PyQt5.QtWidgets import QMessageBox,QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime
import datetime
from datetime import date
import time
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt,QTimer
from GUI_Prototype import Ui_GUI
  
#BROKEN NEEDS TO BE FIXED!!!!
mainwindow = GUI_Prototype.Ui_GUI()


mainwindow.setupUi(object.GUI)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())