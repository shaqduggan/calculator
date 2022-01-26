import math
import statistics
class Calculator:

    """ 
    Calculator module for in class assignment 
    """

    def add(self,x,y,z):
        """ add's two numbers x,y together """
        return x + y + z
    
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
        """ divide's two numbers x,y together """
        return (x / y) if y != 0 else 0
    
    def median(self, x):
        """finds the center most value"""
        x.sort()
        n = int(len(x)/2)
        return round((x[n]+x[n-1])/2, 2) if len(x)%2 == 0 else round(x[int((len(x)-1)/2)], 2)
        
    def isPrime(self,x):
        ''' This is a Prime Number Finder Function '''
        prime = False
        if x > 1:  
            prime = True
            for i in range(2,int(math.sqrt(x))+1):  
                if x % i == 0:  
                    prime = False
                    break
        return prime

    def mean(self,x):
        return statistics.mean(x)

    def mode(self, list):
        return statistics.mode(list)

    def sqrt(self, x):
    	return math.sqrt(x)

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(2,3))
    print(calc.subtract(100000,20000))
    print(calc.remainder(7,3))
    print(calc.division(2,3))
    print(calc.sine(2))
    print(calc.cosine(2))
    print(calc.tangent(2))
    print(calc.subtract(100000,20000))
    print(calc.median([1,1,9,7,5,1,3,2,6,4,8,9,4,2,3,1,5]))
    print(calc.isPrime(13))

    randomList = [36, 42, 27, 32, 39]
    print(calc.mean(randomList))
    print(calc.sqrt(7))
