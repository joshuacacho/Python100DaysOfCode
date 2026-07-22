#CHALLENGE
# The objective is to take the inputs from the user to these questions and then generate a random password.
# Use your knowledge about Python lists and loops to complete the challenge.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# easy version is outputting the letters, symbols and numbers in sequence
    # the output would be abc#$%45
    # used random.choices which
        # Returnd a k sized list of elements chosen from the population with replacement.
            # If the population is empty, raises IndexError.

rand_letters = random.choices(letters, k=nr_letters)
print(rand_letters)
rand_symbols = random.choices(symbols, k=nr_symbols)
rand_numbers = random.choices(numbers, k=nr_numbers)

#combining all lists in 1
password_combined = [rand_letters, rand_symbols, rand_numbers]

print(password_combined)

#convert lists into one string using for loops
password_string = ""

for sublist in password_combined:  # for all 3 lists rand_letters, rand_symbols, rand_numbers
    for char in sublist: # for all characters in all sub lists rand_letters, rand_symbols, rand_numbers
        #going back from list to string
        password_string = password_string + char # concatenate the strings of all sub lists rand_letters, rand_symbols, rand_numbers

print(password_string)

# hard version it outputting letter, symbols and numbers in random order
    # the output could be
        # abc#$%45
        # 45abc%^&
        # $%^45abc
        # .....
        # so on

# using the easy version we can now shuffle our string using random.shuffle
    # random.shuffle Shuffles the sequence x in place.
    #  To shuffle an immutable sequence and return a new shuffled list
password_list = list(password_string)   # convert string to list of characters
print(password_list)
random.shuffle(password_list)  # shuffle now that string has been converted to list, RETURNS NONE so CANT print

# use same logic above when brining multiple lists together with string BUT do it for the shuffled_password
    # going back from list to string
shuffled_password = ""
for char in password_list:
    shuffled_password = shuffled_password + char

print("Your password is " + shuffled_password)

