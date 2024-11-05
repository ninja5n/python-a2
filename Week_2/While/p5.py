# 1 3 6 8 11 13 ...
# seems like +3


def pattern(n: int) -> None:
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        if i % 2 == 0:
            number = number + 3
        else:
            number = number + 2
        i += 1


pattern(20)
