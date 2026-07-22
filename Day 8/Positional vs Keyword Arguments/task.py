# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")



# Function with more than 1 input
def greet_with(name, location):
    print(f"Any please welcome {name} coming all the way from {location}")

greet_with("Joey Lorenzo", "San Francisco, California")


# Keyword Argument function assignment with more than 1 input
def key_arg_mult(a,b,c):
    print(a,b,c)

key_arg_mult(a=1,b=2,c=3)
key_arg_mult(c=4,b=2,a=1)


# Love Calculator
# 💪 This is a difficult challenge! 💪
#
# You are going to write a function called calculate_love_score() that tests the compatibility between
    #  two names.  To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.
# e.g.
#
# name1 = "Angela Yu" name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#

# Example Input
#
# calculate_love_score("Kanye West", "Kim Kardashian")
#
# Example Output
#
# 42

# name_1 = "hello"
# print(name_1.upper())



def calculate_love_score(name_1, name_2):

    #combine the names together
    combined_upper = (name_1 + " " + name_2).upper()
    print(combined_upper)

    true= "TRUE"
    love = "LOVE"
    in_true_count = 0
    in_love_count = 0

    # determine "TRUE" for name 1
    for letter in combined_upper:
        if letter in true: #if letter from combined_upper exists in TRUE add to its count
            in_true_count +=1

    # determine "LOVE" for name 1
    for letter in combined_upper:
        if letter in love:  #if letter from combined_upper exists in LOVE add to its count
            in_love_count += 1


    # Name 1 + Name 2 Count
    print(f"Love Score is {in_true_count}{in_love_count}")


calculate_love_score("Angela Yu","Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")

