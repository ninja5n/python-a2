"""
Program that asks 4 numbers from user, compares them makes sure they are different
and prints out the smallest number.
"""

# requesting input from the user

num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))
num3 = float(input("Please enter third number: "))
num4 = float(input("Please enter fourth number: "))

if (
    (num1 == num2 or num1 == num3 or num1 == num4)
    or (num2 == num3 or num2 == num4)
    or (num3 == num4)
):
    print("Please enter different numbers.")

# if nested loop method
elif num1 < num2:
    if num1 < num3:
        if num1 < num4:
            print(f"The smallest numeber is {num1}.")
elif num2 < num1:
    if num2 < num3:
        if num2 < num4:
            print(f"The smallest number is {num2}.")

# and comparision logic:
elif (num3 < num1) and (num3 < num2) and (num3 < num4):
    print(f"The smallest number is {num3}.")
elif (num4 < num1) and (num4 < num2) and (num4 < num3):
    print(f"The smallest number is {num4}.")

else:
    print("Please type a valid entry.")
