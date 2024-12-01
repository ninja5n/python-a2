def count_digits(num: int) -> int:
    count = 0
    n = num
    while n > 0:
        count += 1
        n = n // 10
    return count


print(count_digits(12345))
