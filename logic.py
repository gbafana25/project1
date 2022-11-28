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
			self.p1label.setText('Side')
			self.p2label.setText('')
			self.p3label.setText('')
			self.p2label.setHidden(True)
			self.p3label.setHidden(True)
			self.parameter1.show()
			self.parameter2.setHidden(True)
			self.parameter3.setHidden(True)
		elif self.rectangle_button.isChecked():
			self.p1label.setText('Length')
			self.p2label.setText('Width')
			self.p1label.show()
			self.p2label.show()
			self.p3label.setText('')
			self.p3label.setHidden(True)
			self.parameter1.show()
			self.parameter2.show()
			self.parameter3.setHidden(True)
		elif self.circle_button.isChecked():
			self.p1label.setText('Radius')
			self.p2label.setHidden(True)
			self.p3label.setHidden(True)
			self.parameter1.show()
			self.parameter2.setHidden(True)
			self.parameter3.setHidden(True)
		elif self.triangle_button.isChecked():
			if c == 0:
				self.p1label.setText('Side 1')
				self.p2label.setText('Side 2')
				self.p3label.setText('Side 3')
				self.parameter1.show()
				self.parameter2.show()
				self.parameter3.show()
				self.p1label.show()
				self.p2label.show()
				self.p3label.show()
			else:
				self.p1label.setText('Base')
				self.p2label.setText('Height')
				self.p3label.setText('')
				self.p3label.setHidden(True)
				self.parameter3.setHidden(True)
				self.parameter1.show()
				self.parameter2.show()
				self.p1label.show()
				self.p2label.show()
