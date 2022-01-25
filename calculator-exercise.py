import math
# import statistics
class Calculator:

	""" 
	Calculator module for in class assignment 
	"""

	def add(self,x,y):
		""" add's two numbers x,y together """
		return x + y
	
	def subtract(self,x,y):
		'''subtract's number y from number x'''
		return x - y
	
	def remainder(self, x, n):
		'''calculate the remainder using mod'''
		return x % n

	def multiplication(self, x, y):
		''' multiplies two numbers x,y together'''
		return x * y

	def sine(self,x):
		''' Finds the sine of the value passed in '''
		return math.sin(x)

	def cosine(self,x):
		''' Finds the cosine of the value passed in '''
		return math.cos(x)

	def tangent(self,x):
		''' Finds the tangent of the value passed in '''
		return math.tan(x)

	def division(self,x,y):
		''' divide's two numbers x,y together '''
		return (x / y) if y != 0 else None

	# def mean(self,x):
	# 	return statistics.mean(x)

	def round_up(self,x):
		""" round up a numbers """
		return round(x)

	def sqrt(self,x):
		''' Finds the squareroot of the value passed in '''
		return math.sqrt(x)


if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(2,3))
	print(calc.subtract(100000,20000))
	# print(calc.calc_remainder(7,3))
	print(calc.division(2,3))
	print(calc.sine(2))
	print(calc.cosine(2))
	print(calc.tangent(2))
	print(calc.subtract(100000,20000))
	randomList = [36, 42, 27, 32, 39]
	# print(calc.mean(randomList))
	print(calc.sqrt(7))