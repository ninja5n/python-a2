def display(lst: list):
    lst[0] = 100
    print(lst)
    print(id(lst))


my_list = [45, 33, 22, 11, 91]
display(my_list)
print(id(my_list))
print(my_list)
