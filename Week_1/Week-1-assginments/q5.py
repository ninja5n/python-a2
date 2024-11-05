"""
Progam to calculate bill. 
"""

# taking input from user for the bill
var1 = float(input("Please enter final bill amount: "))

# discount calculation logic
if var1 >= 1:
    if var1 >= 50000:
        final_amount = var1 * 0.30
        print(f"Entered bill amt: {var1}")
        print(f"You got 30% discount.")
        print(f"Your final bill is {final_amount}.")
    elif 40000 <= var1 <= 49999:
        final_amount = var1 * 0.25
        print(f"Entered bill amt: {var1}")
        print(f"You got 25% discount.")
        print(f"Your final bill is {final_amount}.")
    elif 30000 <= var1 <= 39999:
        final_amount = var1 * 0.20
        print(f"Entered bill amt: {var1}")
        print(f"You got 20% discount.")
        print(f"Your final bill is {final_amount}.")
    elif 10000 <= var1 <= 29999:
        final_amount = var1 * 0.10
        print(f"Entered bill amt: {var1}")
        print(f"You got 10% discount.")
        print(f"Your final bill is {final_amount}.")
    elif 1 <= var1 <= 9999:
        final_amount = var1
        print(f"Entered bill amt: {var1}")
        print(f"You got 0% discount.")
        print(f"Your final bill is {final_amount}.")
else:
    print("Please enter a valid bill amount>0. ")
