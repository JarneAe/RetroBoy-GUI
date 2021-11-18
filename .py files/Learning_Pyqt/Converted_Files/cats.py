from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(280, 150, 281, 191))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("RetroBoy-GUI\Images\images.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 440, 841, 111))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Cat2Button = QtWidgets.QPushButton(self.splitter)
        self.Cat2Button.setObjectName("Cat2Button")
        self.Cat1Button = QtWidgets.QPushButton(self.splitter)
        self.Cat1Button.setObjectName("Cat1Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Cat1Button.clicked.connect(self.show_cat)
        self.Cat2Button.clicked.connect(self.show_cat2)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("RetroBoy-GUI\Images\images.jpg"))

    def show_cat2(self):
        self.photo.setPixmap(QtGui.QPixmap("RetroBoy-GUI\Images\index.jpg"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Cat2Button.setText(_translate("MainWindow", "Cat 1 "))
        self.Cat1Button.setText(_translate("MainWindow", "Cat 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
