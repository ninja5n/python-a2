"""
Whenever you ask for numbers make sure you always add "float" to the code.
Otherwise, if a decimal number is entered, it breaks the code.
"""

sidevalue = float(input("Please enter a side value: "))

area = sidevalue**2

print(f"The area of the square for which your entered a side value is {area}")
print(f"The area of the square for which your entered a side value is {area:.2f}")
