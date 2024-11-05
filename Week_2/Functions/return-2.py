"""
2 function
add() - take 3 integers and return addition
evenodd() - take 1 integer and check if even or odd
"""


def add(num1: int, num2: int, num3: int) -> int:
    total = num1 + num2 + num3
    return total


def checkOddEven(num1: int) -> None:
    if num1 % 2 == 0:
        even = num1
        print(f"{even} is even")
    else:
        odd = num1
        print(f"{odd} is odd.")


nums = add(1, 3, 4)
print(nums)
checkOddEven(nums)
