# 1 to 100... how many even numbers are there?

i = 1
count = 0

while i <= 100:
    if i % 2 == 0:
        count = count + 1
    i += 1
print(count)
