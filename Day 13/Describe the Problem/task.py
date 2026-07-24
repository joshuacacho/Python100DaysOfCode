def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
    # the for loop is attempting to go through a range of numbers 1 to 20 and
        # if i == 20 print out "You got it"
# 2. When is the function meant to print "You got it"?
    # when i == 20
# 3. What are your assumptions about the value of i?
    # i never reaches 20 because range only includes the first value (1) BUT NOT the last value (20)
# 4. What is the fix?
    # the bug in this case is to update 20 to 21 to ensure 20 is included in the range
        # otherwise the print value will never get executed

# updated code

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("Fix! You got it")


my_function()

