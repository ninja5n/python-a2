import random
from typing import List


class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name: ")
        self.balance = 0.0
        self.account_type = input("Enter account type: ")

    def display(self):
        print(f"\nAccount number = {self.account_number}")
        print(f"Account holder = {self.holder}")
        print(f"Account balance = {self.balance}")
        print(f"Account type = {self.account_type}\n")

    def withdraw(self, amt: float):
        # amt = float(input("Enter amount to withdraw: "))
        if amt < 0:
            print("invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(
                f"amount {amt} has been debited from {self.account_number}. updated balance: {self.balance}"
            )
        else:
            print("Insuffcient balance")

    def deposit(self, amt: float):
        # amt = float(input("Enter amount to deposit: "))
        if amt < 0:
            print("invalid amount")
            return
        else:
            self.balance += amt
            print(
                f"amount {amt} has been credited to {self.account_number}. updated balance: {self.balance}"
            )

    def getBalance(self):
        print(f"Your balance = {self.balance}")


# b1 = Bank()
# b1.display()
# b1.deposit()
# b1.display()
# b1.withdraw()
# b1.display()

accounts: List[Bank] = []

while True:
    print("\n1. Add account")
    print("2. Display all accounts.")
    print("3. Search accounts.")
    print("4. Deposit.")
    print("5. Withdraw.")
    print("6. Exit.\n")
    choice = int(input("Enter choice = "))

    if choice == 1:
        x = Bank()
        accounts.append(x)
        print(accounts)

    elif choice == 2:
        for obj in accounts:
            obj.display()

    elif choice == 3:
        acct_num = int(input("enter account number you want to search: "))
        valid_acc = False
        for i in accounts:
            if i.account_number == acct_num:
                valid_acc = True
                print(f"The account number you entered {acct_num} exists.")
        if not valid_acc:
            print("Account number you entered does not exist.")

    elif choice == 4:
        acct_num = int(
            input("Please enter account number you want to deposit amount to: ")
        )
        amt = float(input("Please enter amount you want to deposit: "))
        valid_acc = False
        for i in accounts:
            if i == acct_num:
                i.deposit(amt)
            valid_acc = True
        if not valid_acc:
            print("Please enter a valid account number.")

    elif choice == 5:
        acct_num = int(input("Please enter account number you want to withdraw"))
        amt = float(input("Please enter amount to Withdraw: "))
        valid_acc = False
        for i in accounts:
            if i == acct_num:
                i.withdraw(amt)
                valid_acc = True
        if not valid_acc:
            print("Please enter a valid account number.")

    elif choice == 6:
        account1 = int(input("enter yout account number: "))
        account2 = int(int("enter account no. to transfer amt: "))
        amt = float(input("enter amount to be tranferred: "))
        valid_acc = False
        for i in accounts:
            if i.account_number == account1:
                for j in accounts:
                    if j.account_number == account2:
                        if i.balance < amt:
                            print("Insufficient Balance.")
                            break
                        j.withdraw(amt)
                        j.deposit(amt)
                        valid_acc = True
                        print(f"Amt is successfully transfered to {j.account_number}")
        if not valid_acc:
            print("Enter valid details.")
    else:
        print("Invalid Choice!")
