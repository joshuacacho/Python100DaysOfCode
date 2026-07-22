# Creating random numbers

#import python random module
import random

#import my_module
import my_module

# using random module .randint method which will print random numbers between aand b
random_integer = random.randint(1, 10)
print(random_integer)

#using my module
print(my_module.my_favorite_number)

# using random module .random only which will generate random numbers between 0 and 1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)


# using random module .uniform which will
random_float = random.uniform(1, 10)
print(random_float)


# Challenge
    # Create a coin flip program using what you have learnt about randomization in Python.
    # It should randomly print "Heads" or "Tails" everytime it is run.

heads_or_tails = random.randint(0, 1) #there are only two options 0 or 1 for heads or tails
print(heads_or_tails)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")