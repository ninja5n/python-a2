my_list = [34, 11, 91, 59, 33, 22]


def findLargest(my_list: list[int]) -> int:
    lrg_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > lrg_num:
            lrg_num = my_list[i]
    return lrg_num


print(findLargest(my_list))
