def pattern(num: int) -> None:
    m = 0
    while num >= 0:
        m += 10
        num -= 1
        print(m, end=" ")
    print(" ")


pattern(2)
pattern(5)
pattern(24)
