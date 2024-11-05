"""
Code 4 functions to perform add, sub, div, mult
"""


def add():
    output = num1 + num2
    print(f"Addition output is :  {output}")
    pass


def subtract():
    output = num1 - num2
    print(f"Substraction output is :  {output}")
    pass


def div():
    output = num1 / num2
    print(f"Division output is :  {output}")
    pass


def multiply():
    output = num1 * num2
    print(f"Multiplication output is :  {output}")


num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))
add()
subtract()
div()
multiply()
