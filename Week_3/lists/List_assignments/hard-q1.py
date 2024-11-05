from typing import List

my_list = [1, 5, 25, 21, 12, 44, 13]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def ascendOrder(num: List) -> bool:
    for i in range(0, len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True


print(ascendOrder(my_list))
print(ascendOrder(list_2))
