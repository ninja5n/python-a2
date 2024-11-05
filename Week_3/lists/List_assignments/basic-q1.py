from typing import List

my_list = [1, 2, 3, 4, 6, 8, 12, 14, 16, 18, 24, 32, 48]


def revrs(lst: List[int]) -> List[int]:
    new_lst = []
    for i in range((len(lst) - 1), -1, -1):
        new_lst.append(lst[i])
    return new_lst


print(revrs(my_list))
