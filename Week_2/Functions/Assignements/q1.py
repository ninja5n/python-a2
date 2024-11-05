# def max(num1: int = 0, num2: int = 0, num3: int = 0):
# if (num1 > num2) and (num1 > num3):
# print(f"Maximum number is {num1}")
# elif (num2 > num1) and (num2 > num3):
# print(f"Maximum number is {num2}")
# elif (num3 > num1) and num3 > num1:
# print(f"Maximum number is {num3}")
# else:
# print("Please enter different numbers.")


# def min(num1: int = 0, num2: int = 0, num3: int = 0):
# if (num1 < num2) and (num1 < num3):
# print(f"Maximum number is {num1}")
# elif (num2 < num1) and (num2 < num3):
# print(f"Maximum number is {num2}")
# elif (num3 < num1) and num3 < num1:
# print(f"Maximum number is {num3}")
# else:
# print("Please enter different numbers.")
#
#
# easier funtion:
def maxi(a: float, b: float, c: float):
    result = max(
        a, b, c
    )  # max() is an inbuilt function, so you need to name main functions name.
    print(f"{result} is the max number.")


def mini(a: float, b: float, c: float):
    result = min(a, b, c)
    print(f"{result} is the minimum number.")


maxi(1, 2, 3)
mini(2, 2, 23)
