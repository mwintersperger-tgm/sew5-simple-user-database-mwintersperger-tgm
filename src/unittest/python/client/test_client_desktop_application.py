
import pytestqt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.main.python.client.gui import App
from src.main.python.server.app import app as App


def test_type_textboxes(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    window.email.setText("mwintersperger@student.tgm.ac.at")
    window.photo.setText("test.jpeg")
    assert window.username.text() == 'Michael'
    assert window.email.text() == 'mwintersperger@student.tgm.ac.at'
    assert window.photo.text() == 'test.jpeg'

def test_add_valid_user(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    window.email.setText("mwintersperger@student.tgm.ac.at")
    window.photo.setText("test.jpeg")
    qtbot.mouseClick(window.addUserButton, Qt.LeftButton)
    assert window.tableWidget.columnCount() == 1
    assert window.tableWidget.item(0, 0).text() == "Michael"
    assert window.tableWidget.item(1, 0).text() == "mwintersperger@student.tgm.ac.at"
    assert window.tableWidget.item(2, 0).text() == "test.jpeg"
    assert window.tableWidget.item(3, 0).text() == "Delete User"
    assert window.tableWidget.item(4, 0).text() == "Update User"
    assert window.label.text() == "User added!"

def test_add_invalid_user_too_long_username(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore")
    window.email.setText("mwintersperger@student.tgm.ac.at")
    window.photo.setText("test.jpeg")
    qtbot.mouseClick(window.addUserButton, Qt.LeftButton)
    assert window.tableWidget.columnCount() == 1
    assert window.label.text() == "Username too long!"

def test_add_invalid_user_invalid_email(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    window.email.setText("mwinterspergerstudent.tgm.ac.at")
    window.photo.setText("test.jpeg")
    qtbot.mouseClick(window.addUserButton, Qt.LeftButton)
    assert window.tableWidget.columnCount() == 1
    assert window.label.text() == "Email is not valid!"

def test_add_invalid_user_invalid_photo(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    window.email.setText("mwintersperger@student.tgm.ac.at")
    window.photo.setText("bla.jpeg")
    qtbot.mouseClick(window.addUserButton, Qt.LeftButton)
    assert window.tableWidget.columnCount() == 1
    assert window.label.text() == "Image is not valid!"

def test_add_invalid_user_email_already_exists(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    window.email.setText("mwintersperger@student.tgm.ac.at")
    window.photo.setText("test.jpeg")
    qtbot.mouseClick(window.addUserButton, Qt.LeftButton)
    assert window.tableWidget.columnCount() == 1
    assert window.label.text() == "Email already exists!"

def test_update_valid_user(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael2")
    window.email.setText("mwintersperger2@student.tgm.ac.at")
    window.photo.setText("test2.jpeg")
    qtbot.stopForInteraction()
    #qtbot.mouseDClick(window.tableWidget.item(4, 0), Qt.LeftButton)
    assert window.tableWidget.item(0, 0).text() == "Michael2"
    assert window.tableWidget.item(1, 0).text() == "mwintersperger2@student.tgm.ac.at"
    assert window.tableWidget.item(2, 0).text() == "test2.jpeg"

def test_add_second_valid_user(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    window.email.setText("mwintersperger@student.tgm.ac.at")
    window.photo.setText("test.jpeg")
    qtbot.mouseClick(window.addUserButton, Qt.LeftButton)
    assert window.tableWidget.columnCount() == 2

def test_update_invalid_user_too_long_username(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore")
    qtbot.stopForInteraction()
    #qtbot.mouseDClick(window.tableWidget.item(4, 0), Qt.LeftButton)
    assert window.label.text() == "Username too long!"
#    qtbot.mouseClick(window.tableWidget.item(3, 0), Qt.LeftButton)
#    assert window.tableWidget.columnCount() == 0

