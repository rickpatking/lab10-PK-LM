"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    try:
        x = math.log(b, a)
        return x
    except ValueError:
        print("Can't do this")

def exponent(a, b):
    try:
        x = math.pow(a, b)
        return x
    except ValueError:
        print("Can't do this")