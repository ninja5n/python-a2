# 1 to 10 total
# variable ask  = start, variable ask =  end | start < end
# start, end ---- total


start: int = int(input("Please enter start: "))
end: int = int(input("Please enter end: "))

i: int = start
total = 0
while start <= end:
    total = total + i
    i += 1
print(total)
