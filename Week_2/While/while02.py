"""
Ask M and N from user.
Print M to N.

"""

m: int = int(input("Enter M: "))
n: int = int(input("Enter N : "))

i: int = m  # never use m directly, it's a dataset recevied
# from the user, for future purpose, never touch that dataset.
while i <= n:
    print(f"M = {m},N = {n}", end=" ")
    i += 1
