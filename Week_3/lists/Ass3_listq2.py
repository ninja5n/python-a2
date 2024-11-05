my_list = [1, 2, 3, 4, 5, 6, 7, 8, 12, 24, 60]

for i in range(len(my_list)):
    if my_list[i] % 3 == 0 and my_list[i] % 4 == 0:
        print(my_list[i], end=" ")
