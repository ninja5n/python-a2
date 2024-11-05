my_list = [45, 31, 76, 54, 11, 32, 100]


# result = my_list[0 : len(my_list)] #using lenght, coz we don't want to count
#
# result = my_list[0:6:2]
# result = my_list[0:6:4]  # sirf 45 ayega and then [start:end:step]
# step is also used to define the direction

result = my_list[0::2]
print(result)
