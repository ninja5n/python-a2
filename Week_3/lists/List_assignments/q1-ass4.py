from typing import List

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def oddEvenLists(lst: List) -> None:
    even = []
    odd = []
    for index in range(0, len(lst)):
        if lst[index] % 2 == 0:
            even.append(lst[index])
        else:
            odd.append(lst[index])
    print(even)
    print(odd)


oddEvenLists(my_list)
