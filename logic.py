from PyQt5 import QtWidgets, QtCore
from gui import Gui
import math
import sys

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Logic(QtWidgets.QMainWindow, Gui):
	def __init__(self):
		self.checking = True
		super().__init__()
		self.load()
		#setting up gui
		self.square_button.setChecked(True)
		self.area_button.setChecked(True)
		self.p1label.setText('Side')
		self.p2label.setText('')
		self.p3label.setText('')
		self.p2label.setHidden(True)
		self.p3label.setHidden(True)
		self.parameter1.show()
		self.parameter2.setHidden(True)
		self.parameter3.setHidden(True)

		#checks for if a button is clicked to run functions, makes more efficient
		self.square_button.clicked.connect(self.get_options)
		self.circle_button.clicked.connect(self.get_options)
		self.triangle_button.clicked.connect(self.get_options)
		self.rectangle_button.clicked.connect(self.get_options)
		self.area_button.clicked.connect(self.get_options)
		self.perimeter_button.clicked.connect(self.get_options)
		self.calcgo.clicked.connect(self.get_numbers)

	def get_options(self):
		# uses buttons to change gui based on options selected

		if self.square_button.isChecked():
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
			if self.perimeter_button.isChecked() == True:
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

	def get_numbers(self):
	#pulls numbers from the text boxes, gives them variables, returns float values, then calculates values
			if self.area_button.isChecked():

				if self.triangle_button.isChecked():

					try:
						base = float(self.parameter1.text())
						height = float(self.parameter2.text())
					except ValueError:
						self.output.setText("Inputs must be Numeric Values")
						return
					final_output = base * height * .5
					self.output.setText(f"Area of a triangle: {final_output}")

				elif self.circle_button.isChecked():

					try:
						radius = float(self.parameter1.text())
					except ValueError:
						self.output.setText("Inputs must be Numeric Values")
						return
					final_output = (radius * radius) * math.pi
					self.output.setText(f"Area of a Circle: {final_output}")

				elif self.square_button.isChecked():

					try:
						side = float(self.parameter1.text())
					except ValueError:
						self.output.setText("Inputs must be Numeric Values")
						return
					final_output = (side * side)
					self.output.setText(f"Area of a Square: {final_output}")

				elif self.rectangle_button.isChecked():

					try:
						length = float(self.parameter1.text())
						width = float(self.parameter2.text())
					except ValueError:
						self.output.setText("Inputs must be Numeric Values")
						return
					final_output = (length * width)
					self.output.setText(f'Area of a Rectangle: {final_output}')


			if self.perimeter_button.isChecked():

				if self.triangle_button.isChecked():

					try:
						side1 = float(self.parameter1.text())
						side2 = float(self.parameter2.text())
						side3 = float(self.parameter3.text())
					except ValueError:
						self.output.setText('Inputs must be Numeric Values')
						return
					final_output = side1 + side2 + side3
					self.output.setText(f'Perimeter of a Triangle: {final_output}')

				elif self.circle_button.isChecked():

					try:
						radius = float(self.parameter1.text())
					except ValueError:
						self.output.setText('Inputs must be Numeric Values')
						return
					final_output = 2 * math.pi * radius
					self.output.setText(f'Circumference of a Circle: {final_output}')

				elif self.square_button.isChecked():

					try:
						side = float(self.parameter1.text())
					except ValueError:
						self.output.setText('Inputs must be Numeric Values')
						return
					final_output = side * 4 
					self.output.setText(f'Perimeter of a Square: {final_output}')

				elif self.rectangle_button.isChecked():
					try:
						length = float(self.parameter1.text())
						width = float(self.parameter2.text())
					except ValueError:
						self.output.setText('Inputs must be Numeric Values')
						return
					final_output = (length * 2) + (width * 2)
					self.output.setText(f'Perimeter of a Rectangle: {final_output}')
