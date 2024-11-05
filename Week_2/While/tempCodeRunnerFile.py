# 1 11 101 1001 10001 100001


def pattern(n: int) -> None:
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        number = number * 10
        number += 1-11
        i += 1


pattern(10)
