var1 = int(input("Please enter a valid number: "))

if var1 % 2 == 0 and var1 % 3 == 0 and not var1 % 8 == 0:
    print("The number is correct!, divisible by 2 and 3 but not 8.")
else:
    print("Please pick a different number.")
