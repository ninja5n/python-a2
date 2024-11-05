# 1 2 4 6 8 16 32 64...


def pattern(n: int):
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        number = number * 2
        i += 1


pattern(2)
