
class Calculator:

	""" 
	Calculator module for in class assignment 
	"""

	def add(self,x,y):
		""" add's two numbers x,y together """
		return x + y

	def multiplaction(self, x, y, z):
		''' multiplies two numbers x,y together'''
		return x * y * z


if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(2,3))
	