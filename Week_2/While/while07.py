"""
ask for a number continiously

until they enter 0
when they enter 0, print sum of all previously entered numbers.

"""

m = 0
while True:
    n = int(input("Please enter a number: "))
    #
    # if n != 0:
    # m += n
    # else:
    # break
    # print(f"Total : {m}")

    if n == 0:
        break
    else:
        m += n
print(f"Total : {m}")
