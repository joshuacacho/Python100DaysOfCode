year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# 1. What is the above code doing?
    # for a year entered by the user it will tell you if you are millennial or Gen Z
# 2. When does each line of code do?
    # first if statement checks if you were born between 1980 and 1994 and NOT included those two value
# 3. What are your assumptions about the value of the bug?
    # it you were born in 1980 or 1994 you dont get any answer as
        # for 1984 - > and not >=
        # for 1994 - < and not <=
# 4. What is the fix?
    # include >= and <=
    # NOTE - we dont care if you were born before 1980 as you would not be a millennial or Gen Z
        # we may want to add it through to the user has an output


# fix
year2 = int(input("What's your year of birth? "))

if year2 >= 1980 and year2 <= 1994:
    print("You are a millennial.")
elif year2 > 1994:
    print("You are a Gen Z.")
else:
    print("You are neither a millennial or Gen Z")