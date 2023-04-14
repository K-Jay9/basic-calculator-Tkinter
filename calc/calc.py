'''
This is the core functionality of the calculator
'''
from math import sqrt



class Calculator:

    def __init__(self, first_number, second_number) -> None:
        self.first_number = first_number
        self.second_number = second_number
        self.result = 0
        self.memory = []

    def equal(self, result):
        self.memory.append(result)

    def addition(self):
        self.result = self.first_number + self.second_number
        self.equal(self.result)
        

    def subtraction(self):
        self.result = self.first_number - self.second_number
        self.equal(self.result)

    def multiplication(self):
        self.result = self.first_number - self.second_number
        self.equal(self.result)

    def division(self):
        self.result = self.first_number / self.second_number
        self.equal(self.result)

    def square_root(self):
        self.result = sqrt(self.first_number)
        self.equal(self.result)

    def square(self):
        self.result = self.first_number*self.first_number
        self.equal(self.result)

    def reciprical(self):
        self.result = 1 / self.first_number
        self.equal(self.result)

    def modulo(self):
        self.result = self.first_number%self.second_number
        self.equal(self.result)

