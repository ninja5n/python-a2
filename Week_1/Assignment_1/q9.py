# update odd even, even numbers = 0, odd numbers =1.

my_list = [34, 11, 91, 59, 33, 22]


def updateOddEven(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] = 0
        else:
            my_list[i] = 1
    return my_list


print(updateOddEven(my_list))
