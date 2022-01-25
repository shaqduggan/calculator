
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

	def multiplaction(self, x, y):
		''' multiplies two numbers x,y together'''
		return x * y


if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(2,3))
	print(calc.subtract(100000,20000))
	