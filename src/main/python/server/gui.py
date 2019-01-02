import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import requests

import src.main.python.server.app as controller

class App(QWidget):

    def __init__(self):
        self.usernameValue = None
        self.emailValue = None
        self.photoValue = None

        super().__init__()
        self.title = 'Simple User Database'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()


    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()
        self.username = QLineEdit(self)
        self.username.textChanged.connect(self.usernameEntered)
        self.email = QLineEdit(self)
        self.email.textChanged.connect(self.emailEntered)
        self.photo = QLineEdit(self)
        self.photo.textChanged.connect(self.photoEntered)

        self.addUserButton = QPushButton('Add User', self)
        self.addUserButton.clicked.connect(self.addUser)

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.email)
        self.layout.addWidget(self.photo)
        self.layout.addWidget(self.addUserButton)
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

    @pyqtSlot()
    def addUser(self):
        allEntered = True
        if self.usernameValue is None:
            #error popup
            allEntered = False
        if self.emailValue is  None:
            #error popup
            allEntered = False
        if self.photoValue is  None:
            #error popup
            allEntered = False
        if allEntered:
            r = requests.post('http://localhost:5000/users', json={"username": self.usernameValue, "email": self.emailValue, "photo": self.photoValue})
        self.repaint()

    def usernameEntered(self,text):
        self.usernameValue = text


    def emailEntered(self,text):
        self.emailValue = text

    def photoEntered(self,text):
        self.photoValue = text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
