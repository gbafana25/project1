import shapes.area as a
import shapes.perimeter as p
import sys
from logic import Logic
from PyQt5 import QtWidgets


def selection():
	print('----------------------')
	print('SELECT SHAPE')
	print('----------------------')
	print('1 - Circle')
	print('2 - Rectangle')
	print('3 - Square')
	print('4 - Triangle')

	# Code to check that a valid shape has been selected
	shape = int(input('Shape number: '))
	while shape < 1 or shape > 4:
		shape = int(input('Shape number (1-4): '))

	return shape

def get_rect_nums():
	s1 = float(input("Enter Rectangle Side 1: ").strip())
	s2 = float(input("Enter Rectangle Side 2: ").strip())
	return (s1, s2)

def get_circle_nums():
	r = float(input("Enter Circle Radius: ").strip())
	return r

def get_tri_nums(n):
	if n == 2:
		b = float(input("Enter Base: ").strip())
		h = float(input("Enter Height: ").strip())
		return (b, h)
	if n == 3:
		s1 = float(input("Enter Triangle Side 1: ").strip())
		s2 = float(input("Enter Triangle Side 2: ").strip())
		s3 = float(input("Enter Triangle Side 3: ").strip())
		return (s1, s2, s3)


def get_sqr_nums():
	s = float(input("Enter Square Side Length: ").strip())
	return s



def will_continue():
	z = str(input('Continue (y/n):').strip().lower())
	
	if z == 'y':
		return True
	elif z == 'n':
		return False
	else:
		print("Invalid Input")
		will_continue()



def main():
	app = QtWidgets.QApplication(sys.argv)
	win = Logic()
	app.exec_()
	"""
	is_running = True
	while is_running:
		
		sel = selection()

		print("Computation(Area = 1 or Perimeter = 2):")
		t = int(input("Select Computation Type: ").strip())
		while t < 1 or t > 2:
			t = int(input("Enter 1 or 2: ").strip())

		if sel == 1:
			d = get_circle_nums()
			if t == 1:
				print(f'{a.area_circle(d):.2f}')
			else:
				print(f'{p.perim_circle(d):.2f}')
		elif sel == 2:
			d = get_rect_nums()
			if t == 1:
				print(f'{a.area_rect(d):.2f}')
			else:
				print(f'{p.perim_rect(d):.2f}')
		elif sel == 3:
			d = get_sqr_nums()
			if t == 1:
				print(f'{a.area_sqr(d):.2f}')
			else:
				print(f'{p.perim_sqr(d):.2f}')
		elif sel == 4:
			if t == 1:
				d = get_tri_nums(2)
				print(f'{a.area_tri(d):.2f}')
			else:
				d = get_tri_nums(3)
				print(f'{p.perim_tri(d):.2f}')

		is_running = will_continue() 
	"""


if __name__ == '__main__':
	main()
