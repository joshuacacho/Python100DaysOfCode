print(len("hello"))

# how would be know what data type of hello
    # we can use the type() function
print(type("hello")) # <class 'str'>


# PAUSE 2. Write out 4 type checks to print all 4 data types
# Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>
#

print(type("hello")) #<class 'str'>
print(type(123)) #<class 'int'>
print(type(True)) #<class 'bool'>
print(type(123.42)) #<class 'float'>


# what if we want to convert a string to an integer?
    # we can use casting for this
convert_me = "123"
print(convert_me + "456") # two strings should be added together
print(int(convert_me) + 234) # int cast & two numbers should be added together


# Core casting functions
# Function       Converts to             Example
# int()          Integer                 int("5") → 5
# float()        Floating-point number   float("3.14") → 3.14
# str()          String                  str(42) → "42"
# bool()         Boolean                 bool(0) → False
# complex()      Complex number          complex(2, 3) → (2+3j)

# practical example

#TypeError: can only concatenate str (not "int") to str
    # print("Number of letters in your name " + len(input("Enter your name?")))

#value error
    # print(int("abc") + int("123"))

#Challenge

#Make this line of code run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " + str(len(input("Enter your name"))))
