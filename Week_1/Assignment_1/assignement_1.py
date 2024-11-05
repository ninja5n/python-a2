a = 5
b = 10

# a > 5 and b >= 10 -------->  False How? - False and True = False
# a >= 5 or not b > 10 ------>
# not ( a > 5 and b > 5)
# not ( a < 10 or not b < 10)
# not ( not a <= 5 or not b >= 10)


print(a > 5 and b >= 10)  # false
print(a >= 5 or not b > 10)  # True
print(not (a > 5 and b > 5))  # True
print(not (a < 10 or not b < 10))
