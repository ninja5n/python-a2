import random

options = ["rock", "paper", "scissors"]
computers_choice = random.choice(options)

user_choice = input(("Please pick your option rock/paper/scissors: ").lower())

if user_choice not in options:
    print("Invalid!")
elif user_choice == computers_choice:
    print("It's a Tie!")
elif (
    (user_choice == "paper" and computers_choice == "rock")
    or (user_choice == "scissors" and computers_choice == "rock")
    or (user_choice == "rock" and computers_choice == "paper")
):
    print("You win!")
else:
    print(f"The Computer wins as it's choose {computers_choice}!")
