# print 1 to 10


def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end=" ")
        i = i + 1
    print()


printPattern(20)
printPattern(23)
printPattern(33)
