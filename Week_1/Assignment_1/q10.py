my_list = [34, 11, 91, 59, 33, 22]


def updateOddEven(my_list: list[int]) -> list[int]:
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] += 1
        else:
            my_list[i] -= 1
    return my_list


print(updateOddEven(my_list))
