# writing hangman from scratch and understanding why

# modules needed
from hangman_art import stages, logo
from hangman_words import word_list
import random #from random better to import the entire thing otherwise you will right chpice(random_word)


#generate hangman logo from hangman_art
print(logo)
print("Welcome to Hangman\n")

#generate random word from module hangman_words
chosen_word = random.choice(word_list)
print(chosen_word)

#generate as many blank spaces as words
placeholder = ""
for letter in chosen_word:
    placeholder = placeholder + "_"
print(placeholder)


#logic for tracking guessed word and result of game
guessed_letter = [] # keep track of guesses

# placeholder will always initialize to ____, etc.. so display will be our live display
    # the live display will be to track the guess being correct or not and show the letter or not
display = placeholder

#we keep looping while there is a "_" in work meaning the user has NOT guessed the letter
lives = 6
game_running = True


while "_" in display:

    #ask the user for a letter
    guess = input("Please guess a letter: ")
    print(guess)

    #the ORDER here is important where this APPEARS BEFORE appending the guessed letter below
    #check if guessed letter has already been guessed and continue
    if guess in guessed_letter:
        print(f"The letter {guess} has already been tried, please guess another letter")
        continue

    #check
        # if guessed letter is not in chosen word and remove life
        # if all 6 lives out game over
            # show chosen word
        # else append letter to guessed_letter array

    if guess not in chosen_word:
        lives = lives - 1
        print(f"The guessed letter {guess} is not in the Hangman word")
        print(f"You have {lives} lives left")
        print(stages[lives])

        if lives == 0:
            game_running = False #game over
            print("Game Over")
            print(f"You lose, your hangman word was {chosen_word}")
    else:
        # append the letter in guessed_letter if doesnt already exist
        guessed_letter.append(guess)
        print(guessed_letter)

    #build logic for displaying or not displaying letter if found in guessed_word

    #set display to blank and create structure below based on each guess
        # since check was passed and letter is indeed in chosen_word
    display = ""
    for letter in chosen_word:
        if letter in guessed_letter: #guaranteed to be true based on if/else logic for including or not
            display = display + letter #replace "_" with letter
        else:
            display = display + "_" #dont replace and keep "_" for all remaining letter

    print(f"\nOutput of hangman guesses so far: {display}\n")  # keep "-" for all other letters not guessed yet

if game_running:
    print(f"You win! The hangman word {chosen_word} was guessed correctly with {lives} lives remaining!")
