my_list = [34, 11, 90, 43, 15, -65, -54]

maxi = my_list[0]

for index in range(0, len(my_list)):
    if my_list[index] > maxi:
        maxi = my_list[index]

print(maxi)
