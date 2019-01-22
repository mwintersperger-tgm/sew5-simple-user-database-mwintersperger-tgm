import pytestqt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.main.python.client.gui import App

def test_type_username(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.username.setText("Michael")
    assert window.username.text() == 'Michael'

def test_type_email(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.email.setText("mwintersperger@student.tgm.ac.at")
    assert window.email.text() == 'mwintersperger@student.tgm.ac.at'

def test_type_photo(qtbot):
    window = App()
    window.show()
    qtbot.addWidget(window)
    qtbot.waitForWindowShown(window)
    window.photo.setText("test.jpeg")
    assert window.photo.text() == 'test.jpeg'
