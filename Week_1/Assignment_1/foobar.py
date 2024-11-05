var1 = float(input("Please enter a number to play foobar: "))

if var1 % 3 == 0 and var1 % 5 == 0:
    print("FOO_BAR!!")
elif var1 % 3 == 0:
    print("F00!")
elif var1 % 5 == 0:
    print("Bar!")
else:
    print("FOOFOOBARBAR!")
