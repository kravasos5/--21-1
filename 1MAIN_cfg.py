import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from register_cfg import Ui_RegisterWindow
from mainwindow_cfg import Ui_MainWindow
from actwindow_cfg import Ui_ActWindow
from kuratorwindow_cfg import Ui_KuratorWindow

app = QtWidgets.QApplication(sys.argv)

RegisterWindow = QtWidgets.QWidget()
ui = Ui_RegisterWindow()
ui.setupUi(RegisterWindow)
RegisterWindow.show()

def openMainWindow():
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    RegisterWindow.close()
    MainWindow.show()

    def openActWindow():
        global ActWindow
        ainWindow.close()
        ActWindow = QtWidgets.QMainWindow()
        ui = Ui_ActWindow()
        ui.setupUi(ActWindow)
        ActWindow.show()

    ui.pushButton_4.clicked.connect(openActWindow)

ui.pushButton_2.clicked.connect(openMainWindow)


sys.exit(app.exec_())
