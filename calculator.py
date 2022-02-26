"""
Calculator module for in class assignment
"""
import math

class Calculator:
    """
    Calculator module for in class assignment
    """

    def __init__(self, args):
        self.args = args
        self.list_len = len(self.args)

    def add(self):
        """ adds two numbers """
        return sum(self.args)

    def subtract(self):
        ''' subtracts second number from first number '''
        return self.args[0] - self.args[1]

    def multiplication(self):
        ''' multiplies two numbers '''
        return math.prod(self.args)

    def division(self):
        """ divides two numbers """
        return (self.args[0] / self.args[1]) if self.args[1] != 0 else "Error Try again"

    def remainder(self):
        ''' finds the remainder using modulus operator '''
        return self.args[0] % self.args[1] if self.args[1] != 0 else "Error Try again"

    def sine(self):
        ''' Finds the sine of the value passed in '''
        return math.sin(self.args[0])

    def cosine(self):
        ''' Finds the cosine of the value passed in '''
        return math.cos(self.args[0])

    def tangent(self):
        ''' Finds the tangent of the value passed in '''
        return math.tan(self.args[0])

    def is_prime(self):
        ''' This is a Prime Number Finder Function '''
        prime = False
        if self.args[0] > 1:
            prime = True
            for i in range(2,int(math.sqrt(self.args[0]))+1):
                if self.args[0] % i == 0:
                    prime = False
                    break
        return prime

    def median(self):
        """ finds the center value """

        self.args.sort()
        if self.list_len % 2 == 0:
            median1 = self.args[self.list_len//2]
            median2 = self.args[self.list_len//2 - 1]
            median = (median1 + median2)/2
        else:
            median = self.args[self.list_len//2]
        print(f"Median of:{self.args}")
        return median

    def mean(self):
        """ finds the average """
        if self.list_len > 0:
            mean = round(sum(self.args)/self.list_len,2)
            return mean

    def mode(self):
        """ finds the value(s) that appears most often """
        mode = None
        temp_mode = {}
        for num in self.args:
            if num not in temp_mode:
                temp_mode[num] = 0
            temp_mode[num] += 1
        # print(temp_mode)
        ans_sort = sorted(temp_mode.items(),key = lambda kv: kv[1] , reverse = True)
        # print(ans_sort)

        # Step 1 - Get the max number
        max_num = ans_sort[0][1]

        # Use the value to get all of the keys with that value using list comprehension
        if max_num > 1:
            mode = [num[0] for num in ans_sort if num[1] == max_num]
        return mode

    def sqrt(self):
        """ finds the square root """
        return math.sqrt(self.args[0])

    def round_up(self):
        """ round up a numbers """
        return round(self.args[0], self.args[1])