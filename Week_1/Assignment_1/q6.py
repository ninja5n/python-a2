my_list = [34, 11, 91, 59, 33, 22]


def countOddEven(my_list: list) -> None:
    even_total = 0
    odd_total = 0
    for i in my_list:
        if i % 2 == 0:
            even_total += i

        else:
            odd_total += i

    print(f"Total even numbers = {even_total}")
    print(f"Total odd numbers = {odd_total}")


countOddEven(my_list)
