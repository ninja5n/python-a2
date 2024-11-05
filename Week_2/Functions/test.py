"""
Make a function name checkOddEven
which take 1 integer as an argument

If integer is Even, then return True
else return False
"""


def oddEven(num1: int = 0) -> bool:
    if num1 % 2 == 0:
        return True
    return False


# answer = checkOddEven(21)
# print(answer)
# print(type(answer))


def checkOddEven(num1: int = 0) -> bool:
    return num1 % 2 == 0


print(checkOddEven(22))
print(checkOddEven(21))
