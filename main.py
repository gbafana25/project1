import shapes.area as a
import shapes.perimeter as p
import sys
from logic import Logic
from PyQt5 import QtWidgets





def main():
	app = QtWidgets.QApplication(sys.argv)
	win = Logic()
	app.exec_()


if __name__ == '__main__':
	main()
