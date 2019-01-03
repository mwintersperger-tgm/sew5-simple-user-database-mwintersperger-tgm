import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests

#import src.main.python.server.app as controller

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

        self.label = QLabel('',self)

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
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.email)
        self.layout.addWidget(self.photo)
        self.layout.addWidget(self.addUserButton)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        r = requests.get('http://localhost:5000/users')
        self.USERS = r.json()["users"]

        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(len(self.USERS))
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers )
        for i in range(0,len(self.USERS)):
            self.tableWidget.setItem(0,i, QTableWidgetItem(self.USERS[i]["username"]))
            self.tableWidget.setItem(1,i, QTableWidgetItem(self.USERS[i]["email"]))
            self.tableWidget.setItem(2,i, QTableWidgetItem(self.USERS[i]["photo"]))
            self.tableWidget.setItem(3,i, QTableWidgetItem("Delete User"))
            self.tableWidget.setItem(4,i, QTableWidgetItem("temp"))
        self.tableWidget.itemDoubleClicked.connect(self.pushedTableButton)

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
            self.label.setText(r.json()["message"])
            r = requests.get('http://localhost:5000/users')
            self.USERS = r.json()["users"]
            self.tableWidget.setColumnCount(len(self.USERS))
            for i in range(0,len(self.USERS)):
                self.tableWidget.setItem(0,i, QTableWidgetItem(self.USERS[i]["username"]))
                self.tableWidget.setItem(1,i, QTableWidgetItem(self.USERS[i]["email"]))
                self.tableWidget.setItem(2,i, QTableWidgetItem(self.USERS[i]["photo"]))
                self.tableWidget.setItem(3,i, QTableWidgetItem("Delete User"))
                self.tableWidget.setItem(4,i, QTableWidgetItem("temp"))

    def usernameEntered(self,text):
        self.usernameValue = text

    def emailEntered(self,text):
        self.emailValue = text

    def photoEntered(self,text):
        self.photoValue = text

    def pushedTableButton(self,clicked):
        if clicked.row() == 3:
            r = requests.delete('http://localhost:5000/users/%s' % self.USERS[clicked.column()]['id'])
            self.label.setText(r.json()["message"])
            r = requests.get('http://localhost:5000/users')
            self.USERS = r.json()["users"]
            self.tableWidget.setColumnCount(len(self.USERS))
            for i in range(0,len(self.USERS)):
                self.tableWidget.setItem(0,i, QTableWidgetItem(self.USERS[i]["username"]))
                self.tableWidget.setItem(1,i, QTableWidgetItem(self.USERS[i]["email"]))
                self.tableWidget.setItem(2,i, QTableWidgetItem(self.USERS[i]["photo"]))
                self.tableWidget.setItem(3,i, QTableWidgetItem("Delete User"))
                self.tableWidget.setItem(4,i, QTableWidgetItem("temp"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
