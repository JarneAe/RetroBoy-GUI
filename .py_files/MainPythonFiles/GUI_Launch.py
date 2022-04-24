import sys
from PyQt5 import QtWidgets
from GUI_MainInterface import Ui_Main_Interface




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_Main_Interface()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())

    
