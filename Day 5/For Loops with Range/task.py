# using for loops with the range function

# notice how this does NOTHING
print(range(1,10))

# the range function must be used with a loop of some kind
    #range(a,b) includes a BUT NOT b
for number in range(1,10): #between 1 and 10 not including 10
    print(number)


# within the range function you can also specify a 3rd parameter
    # range(a,b) includes a BUT NOT b
    # this 3rd parameter is how far you want to space the values out
for number in range(1,11,3):  #3rd parameter is every 3 print out
    print(number)


# adding up all numbers from 1 to 100 using the range function
total_score = 0
for number in range(1,101):
    total_score = total_score + number

print(total_score)


# Coding Challenge Fizz Buzz

# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# These are the rules of the FizzBuzz game:
    # Your program should print each number from 1 to 100 in turn and include number 100.
    # But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
    # When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
    # And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print(str(number) + " FizzBuzz")
    elif number % 5  == 0:
        print(str(number) + " Buzz")
    elif number % 3  == 0:
        print(str(number)  + " Fizz")
    else:
        print(number)