import copy

a = [56, 32, "akul", "ambani", [1, 3, 4, 1], False, 11.112]


b = a

print(a, id(a))
print(b, id(b))

# IDs are same, B is just referenced to the same memory location.


"""
copy - inbuilt module, shallow copy - sirf bahar wale elements ki value ....
"""

b = copy.copy(a)

print(b)
print(id(b))
print(id(a))

"""
deep copy -  
"""
print()
b = copy.deepcopy(a)
print(b)
print()
print(id(b))
b[4][2] = 1000
print()
print()
print(b)
