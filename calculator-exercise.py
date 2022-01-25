
class Calculator:

	""" 
	Calculator module for in class assignment 
	"""

	def add(self,x,y):
		""" add's two numbers x,y together """
		return x + y

	
	def division(self,x,y):
		""" divide's two numbers x,y together """
		return (x / y) if y != 0 else 0


if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(2,3))
	print(calc.division(2,3))
	