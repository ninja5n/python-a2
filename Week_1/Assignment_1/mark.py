var1 = float(input("Please enter a score: "))

if var1 >= 91 and var1 <= 100:
    print("A")
elif var1 >= 81 and var1 <= 90:
    print("B")
elif var1 >= 71 and var1 <= 80:
    print("C")
elif var1 >= 61 and var1 <= 70:
    print("D")
elif var1 >= 0 and var1 <= 60:
    print("FAIL")
else:
    print("Please enter a score between valid range of 1 - 100.")
