def leapYear(year: int = 0):
    if year % 4 == 0 and year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 4 == 0 and year % 100 == 0:
        print(f"{year} is NOT a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")


leapYear(100)
leapYear(2000)
leapYear(500)
leapYear(4)
leapYear(5)
