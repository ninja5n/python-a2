var1 = float(input("No. of Classes held: "))
var2 = float(input("No. of Classes attended: "))

threshold = var1 * 0.75

if var1 > 0 and var2 <= threshold and var2 <= var1:
    attendence = var1 * (var2 / 100)
    print(f"Attendance is {attendence}%.")
    print("Student is not allowed to sit for the exam.")
elif var1 <= 0 or var2 <= 0:
    print("Please enter valid numbers.")
else:
    print("Student is allowed to sit for the exam!")
