# 1 11 111 1111 11111... until n


def pattern(n: int) -> None:
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        number = (number * 10) + 1
        i += 1


pattern(10)
