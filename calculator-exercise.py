
class Calculator:

	""" 
	Calculator module for in class assignment 
	"""

	def add(self,x,y):
		""" add's two numbers x,y together """
		return x + y
	
	def subtract(self,x,y):
		""" subtract's number y from number x  """
		return x - y
	
	def calc_remainder(x, n):
		return x % n


if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(2,3))
	print(calc.subtract(100000,20000))
	print(calc.calc_remainder(7,3))
	