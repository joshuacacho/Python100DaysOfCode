# number guessing game

from art import logo
import random
import sys


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
  41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
  61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
  81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

print(logo)

start_range = 1
end_range = 100
number_to_guess = random.choice(numbers)
already_guessed = []

print("Welcome to the Number guessing game!")
print(f"Im thinking of a number between {start_range} and {end_range}")
you_lose_message = "You've run out of guesses. Refresh the page to run again."
guess_to_high_message = "Too High, Guess Again"
guess_to_low_message = "Too Low, Guess Again"
guess_correct_message = f"You guessed correctly, the number was {number_to_guess}"

def correct_number_guess_or_not(user_guessed_number, number_to_chose, guess_count):
    """This function determines if the user guessed correct number taking into guess amount"""
    if user_guessed_number > number_to_chose:
        print(guess_to_high_message)
        guess_count -= 1
    elif user_guessed_number < number_to_chose:
        print(guess_to_low_message)
        guess_count -= 1
    elif user_guessed_number == number_to_chose:
        print(guess_correct_message)
        sys.exit() # game over so end game
    else:
        print("Logic is busted")

    return guess_count

def number_already_guessed(current_guess, guess_list):
   """Function to check if the number was already guessed"""
   guessed_value = False

   if current_guess in guess_list:
       print(f"The number {current_guess} has already been tried, please guess another number")
       guessed_value = True

   return guessed_value

def game_over(guess_count):
    """This function takes in the guess count and if 0 returns True, otherwise returns False"""
    stop_game = False
    if guess_count == 0:
        print(you_lose_message)
        stop_game = True

    return stop_game

def guessing_game():

    easy_guesses = 10
    hard_guesses = 5
    guessed_num = False
    print(number_to_guess)

    easy_message = f"You have {easy_guesses} attempts remaining to guess the number."
    hard_message = f"You have {hard_guesses} attempts remaining to guess the number."
    retry_message = "Incorrect selection. Please choose a difficulty. Type 'easy' or 'hard': "


    game_level = input("Please Choose a difficulty by typing 'easy' or 'hard': ").lower()

    while game_level != "easy" and game_level != "hard":
        game_level = input(retry_message).lower()

    if game_level == 'easy':
        print(easy_message)

        while not guessed_num:

            # end game if we ran out of guesses not asking user to enter another
            if game_over(easy_guesses) == True:
                break

            # take in user guess
            user_guess = int(input("Make a guess: "))

            # check if number already guessed
            number_tried = number_already_guessed(user_guess, already_guessed)
            if number_tried == True:
                continue

            # check if user guesses number correct and has guesses left
                # update easy_guesses count which is returned from function
            easy_guesses = correct_number_guess_or_not(user_guess, number_to_guess, easy_guesses)
            # add number to already guessed list
            already_guessed.append(user_guess)
    else:
        print(hard_message)

        while not guessed_num:

            # end game if we ran out of guesses not asking user to enter another
            if game_over(hard_guesses) == True:
                break

            # take in user guess
            user_guess = int(input("Make a guess: "))

            # check if number already guessed
            number_tried = number_already_guessed(user_guess, already_guessed)
            if number_tried == True:
                continue

            # check if user guesses number correct and has guesses left
                # update hard_guesses count which is returned from function
            hard_guesses = correct_number_guess_or_not(user_guess, number_to_guess, hard_guesses)
            # add number to already guessed list
            already_guessed.append(user_guess)

guessing_game()