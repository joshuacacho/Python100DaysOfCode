import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2 # breakpoint added
        # print(new_item)
        new_item += random.randint(1, 3)
        # print(new_item)
        new_item = maths.add(new_item, item)
        # print(new_item)
        b_list.append(new_item) # indented b_list to be in the scope of the for loop so new item appended each time
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# what is the bug in this code, why is it only printing out 1 item instead of 6


# Challenge
# Debugging Odd or Even
# - Read the code in exercise.py - Spot the problems 🐞.
# - Modify the code to fix the program. Fix the code so that it works and passes the tests when you submit.
# - You can copy and paste the code into PyCharm to help you debug.
def odd_or_even(number):
    if number % 2 == 0: # needed to add double equal sign here
        return "This is an even number."
    else:
        return "This is an odd number."


# Challenge 2

# Debugging Leap Year
# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program.
# Fix the code so that it works and when you hit submit it should pass all the tests.
# This is how you work out whether if a particular year is a leap year.
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder
# You can paste the code into PyCharm to help you debug.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
    else:
        return False


print(is_leap(2000)) # This is cleanly divisible by 100
print(is_leap(2032)) # This is NOT cleanly divisible by 100



#Challenge 3
#Debugging FizzBuzz
# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program.
# - No shortcuts
# - don't copy-paste to replace the code entirely with a previous working solution.
# The code needs to print the solution to the FizzBuzz game.
# - Your program should print each number from 1 to x where x is the input number.
# - However when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# - When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# - And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

print("FIZZ BUZZ GAME")
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(15)