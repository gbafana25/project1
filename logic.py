from PyQt5 import QtWidgets, QtCore
from gui import Gui
import sys

class Logic(QtWidgets.QMainWindow, Gui):
	def __init__(self):
		super().__init__()
		self.load()
