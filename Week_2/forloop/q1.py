"""
Create a function named
div_by_3_and_5
which takes 2 integers as a arguments
(n1,n2)
, and print all the numbers divisible by 3 and 5 between n1 and n2.

"""


def checkDiv(n1: int, n2: int) -> None:
    for i in range(n1, n2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")


checkDiv(1, 60)
