var1 = int(input("Please enter number of wins: "))
var2 = int(input("Please enter number of losses: "))
var3 = int(input("Please enter number of ties: "))
wins = var1 * 4
loss = var2
tie = var3 * 2

# points calculation
total_points = wins + tie
# output
print(f"Total points : {total_points}.")
