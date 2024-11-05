"""
Ask M and N from user.
Print M to N.
for M <= N
or N <=M
"""

#
# m: int = int(input("Enter M: "))
# n: int = int(input("Enter N : "))
#
# if m < n:
# i: int = m  # never use m directly, it's a dataset recevied
#   from the user, for future purpose, never touch that dataset.
# while i <= n:
# print(f"{i}", end=" ")
# i += 1
# else:
# i: int = n
# while i <= m:
# print(f"{i}", end=" ")
# i += 1
#

# same code in function


def mTon(m: int, n: int) -> None:
    o: int = m
    while o <= n:
        print(o, end=" ")
        o += 1


m: int = int(input("Enter M= "))
n: int = int(input("Enter N= "))

if m > n:
    mTon(n, m)
else:
    mTon(m, n)
