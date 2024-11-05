my_list = [1, 3, 5, 10, 25, 22, 1, 21, 55, 50, 75, 199, 100]

for i in range(len(my_list)):
    if my_list[i] % 5 == 0:
        print(my_list[i], end=" ")
