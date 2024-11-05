my_list = [1, 2, 3, 4, 5, 10, 20, 25, 30, 6, 8, 12, 14, 16, 18, 24, 32, 48]


def dv5(lst):
    i = 0
    while i <= len(lst):
        count = 0
        if lst[i] % 5 == 0:
            count += 1
            print(count)


dv5(my_list)
