# The Modulo Operator returns the remainder of a division operation
print(10 % 3) # returns remainder of 1

print(6 % 2) # returns remainder of 0 - clean division

print(6 % 5) # returns remainder of 1

print(6 % 4) # returns remainder of 2

# Challenge

# Write some code using what you have learnt about the modulo operator
# and conditional checks in Python to check
# if the number in the input area is odd or even.
# If it's odd, print out the word "Odd" otherwise print out "Even".

print("Welcome to the module game where i tell you if you number is odd or even")
modulo = int(input("Please enter a number: "))

if modulo%2 ==0:
    print("Your number is Even")
else:
    print("Your number is Odd")



