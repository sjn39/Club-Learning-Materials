import random

# Rock, Paper, Scissors
print("Rock, Paper, Scissors")
print("Choose one of the following: (rock, paper, scissors)")
choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

userChoice = input("Enter your choice: ")


if userChoice == computer:
    print("Tie!")
elif (userChoice == "rock" and computer == "scissors") or (userChoice == "paper" and computer == "rock") or (userChoice == "scissors" and computer == "paper"):
    print("You won!")
else:
    print("You lost!")
