# List methods

# some functions only related to list and only can be used with lists.

a = [56, 32, "Ak", 47, False, 11.1112]

a.append(100)  # pass by reference, as there is a code written inbuilt in python
# memory is transported to the function and changes are made
# to view hit ctrl + click
a.append(122)
a.append("innin")
a.insert(3, 33333)  # index 3, insert 33333 before the written index.
a.insert(6, "Ninad")
a.insert(33, 322321212)  # you never get error that range out of
a.insert(0, -22)  ### always on the left side of the index by default.
print(a)

""" when is pass by reference usable? 
    -- not when printing
    -- but to update, or add something to the list
"""
