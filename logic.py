from PyQt5 import QtWidgets, QtCore
from gui import Gui
import sys

class Logic(QtWidgets.QMainWindow, Gui):
	def __init__(self):
		super().__init__()
		self.load()
		self.square_button.setChecked(True)
		self.area_button.setChecked(True)
		self.options.clicked.connect(self.get_options)

	def get_calc(self):
		if self.area_button.isChecked():
			return 1
		else:
			return 0

	def get_options(self):
		# TODO: create text boxes, grab input
		# use existing functions to calculate

		# use to decide area/perimeter
		c = self.get_calc()
		if self.square_button.isChecked():
			# compute square (area, perim.)
			print('square')
		elif self.rectangle_button.isChecked():
			print('rectangle')	
		elif self.circle_button.isChecked():
			print('circle')
		elif self.triangle_button.isChecked():
			print('triangle')
