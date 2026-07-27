#The goal is to build a game that asks the user to guess who has more followers on Instagram.

# import Python libraries needed to complete
from art import logo, vs
from game_data import data
import random


# DO THIS PROJECT AGAIN TOMORROW


def compare_a_to_b(dict1, dict2):
    """function to determine who has more followers"""
    winner_is = ""

    if dict1 > dict2:
        winner_is = "A"
    if dict1 < dict2:
        winner_is = "B"

    return winner_is

print(logo)

def higher_lower():

    score = 0
    game_running = True

    while game_running:

        a_compare = random.choice(data)
        # Compare A: {'name': 'Virat Kohli', 'follower_count': 55, 'description': 'Cricketer', 'country': 'India'}
        print(f"Compare A: {a_compare["name"]}, a {a_compare["description"]}, from {a_compare["country"]}, {a_compare["follower_count"]} ")

        print(vs)

        b_compare = random.choice(data)
        print(f"Compare A: {b_compare["name"]}, a {b_compare["description"]}, from {b_compare["country"]}, {b_compare["follower_count"]} ")

        # check if follower_count is equal and redraw b_compare as both follower_counts cant be equal
        while a_compare["follower_count"] == b_compare["follower_count"]:
            b_compare = random.choice(data)

        # take user guess and ensure its A or B
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        while user_guess != 'A' and user_guess != 'B':
            user_guess = input("Incorrect option. Who has more followers? Type 'A' or 'B':")

        # compute who has more followers
        more_follower_result = compare_a_to_b(a_compare["follower_count"], b_compare["follower_count"])

        # compare result from followers count vs user guess
        if more_follower_result == user_guess:
            score  = score + 1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry, that is wrong. Final ccore: {score}")
            game_running = False


higher_lower()