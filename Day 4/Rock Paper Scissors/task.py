# Implementing the Rock, Paper and Scissors Game

# Core casting functions
# Function       Converts to             Example
# int()          Integer                 int("5") → 5
# float()        Floating-point number   float("3.14") → 3.14
# str()          String                  str(42) → "42"
# bool()         Boolean                 bool(0) → False
# complex()      Complex number          complex(2, 3) → (2+3j)

import random
from numbers import Number

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# test your code by uncommenting these lines
# print(rock)
# print(paper)
# print(scissors)

paper_rock_scissors = ["Rock", "Paper", "Scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))

# assert valid selection made and if not, continue to ask question until user enters valid value
while user_input not in (0,1,2): #value taken is as string
    print("invalid selection")
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))

user_choice = paper_rock_scissors[user_input] #when using index cant put string so cast user_input to int
print("User Choice is " + user_choice)
comp_input = random.choice(paper_rock_scissors)
print("Computer Choice is " + comp_input)


print("-----------------------------------")
print("-------------WINNER IS-------------")
print("-----------------------------------")

if user_choice == comp_input:
    print("No one wins, its a Draw!")

#rock logic
if user_choice == "Rock" and comp_input == "Scissors":
    print("User Wins with Rock " + rock)
elif user_choice == "Scissors" and comp_input == "Rock":
    print("Computer Wins with Rock " + rock)

#Scissors Logic
if user_choice == "Scissors" and comp_input == "Paper":
    print("User Wins with Scissors " + scissors)
elif user_choice == "Paper" and comp_input == "Scissors":
    print("Computer Wins with Scissors " + scissors)

#Paper Logic
if user_choice == "Paper" and comp_input == "Rock":
    print("User Wins with Paper " + paper)
elif user_choice == "Rock" and comp_input == "Paper":
    print("Computer Wins with Paper " + paper)


