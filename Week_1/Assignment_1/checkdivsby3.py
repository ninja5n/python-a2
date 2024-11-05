num1 = int((input("Please enter your number: ")))

# divisibility test, always use modulus for comparision
if num1 % 3 == 0:
    print("Number is divisible by 3.")
else:
    print("Sorry the number is not divisible by 3.")
