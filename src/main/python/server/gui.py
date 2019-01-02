import sys
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import src.main.python.server.app as controller

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()

        self.initUI()


    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()


        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(len(controller.USERS))
        for i in range(0,len(controller.USERS)):
            self.tableWidget.setItem(0,i, QTableWidgetItem(controller.USERS[i]["username"]))
            self.tableWidget.setItem(1,i, QTableWidgetItem(controller.USERS[i]["email"]))
            self.tableWidget.setItem(2,i, QTableWidgetItem(controller.USERS[i]["photo"]))
            self.tableWidget.setItem(3,i, QTableWidgetItem("temp"))
            self.tableWidget.setItem(4,i, QTableWidgetItem("temp"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
