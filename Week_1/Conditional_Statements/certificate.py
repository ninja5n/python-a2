"""
3 requirements to get a certificate
1. should be a part of C&D
2. minimum class attended should be 20
3. minimum assigment submitted = 45

pseudo logic:
Are you part of C&D = yes
    Enter class attended >= 20
        Enter assigment submitted >= 45
            you are eligible
else
    you are not
"""

var1 = input("Are you part of C%D? yes/no: ").upper
if var1 == "YES":
    var2 = float(input("Enter class attended:"))
    if var2 >= 20:
        var3 = float(input("Enter assigment submitted:"))
        if var3 >= 45:
            print("You are eligible for certificate.")
        else:
            print("You are not eligible.")
    else:
        print("You are not eligible.")
else:
    print("You are not eligible.")
