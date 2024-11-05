# used to create a list
"""
Not manipute, but to create a new list
"""

# create a list with number from 1 to 10

# without using list comprehension
# my_list = []
# for i in range(1, 11):
# my_list.append(i)
# print(my_list)

# with using list comprehension, its efficient.
# when the list size becomes large, it is faster.
# for loop takes a long time

my_list = [i for i in range(1, 11)]
my_list = [i for i in range(-10, -1, 1)]
my_list = [i % 2 == 0 for i in range(1, 11)]
print(my_list)


# using ternary, list comprehension using ----
my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
# [(what to add) (loop)]
my_list = [f"{i} = even" if i % 2 == 0 else f"{i} = odd" for i in range(1, 11)]
print(my_list)
print()
print()

"""
List = [what to add, loop, when to add]
"""

my_list_c = [i for i in range(0, 11, 2) if i % 2 == 0]
# what to add                    #when to add

print(my_list_c)
