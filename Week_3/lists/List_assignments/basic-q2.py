my_list = [1, 2, 3, 4, 6, 8, 12, 14, 16, 18, 24, 32, 48]

from typing import List


def div34(lst: List[int]) -> List[int]:
    m = []
    for i in range(len(lst)):
        if lst[i] % 3 == 0 and lst[i] % 4 == 0:
            m.append(lst[i])
    return m


print(div34(my_list))
