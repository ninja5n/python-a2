"""
Q2.
Create a function named calSum() which takes 2 integers n1 and n2 as a argument.
Calculate the sum of all the numbers from n1 and n2 andRETURN THAT SUM.
Also make sure that n1 is smaller than n2. If it is not, then return
“n1 should be smaller”.
"""


def calsum(n1: int, n2: int):

    if n1 < n2:
        for i in range(n1, (n2 + 1)):
            i += i
        return i
    else:
        return str("Please enter n1 smaller than n2.")


print(calsum(1, 10))
