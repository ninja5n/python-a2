# Membership operator

a = [43, 67, 11, 80, 54]

x = a.count(43)  # =1 meaning count by value
print(x)

num: int = int(input("Enter a number = "))
if a.count(num) > 0:
    print("Yes")
else:
    print("No")
