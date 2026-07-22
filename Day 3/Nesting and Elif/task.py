print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    # NEW where we check if they are over 18 or not
    age = int(input("What is your age? "))
    if age > 18:
        print("Please pay the $12 adult fare")
    else:
        print("Please pay the $7 child fare")
else:
    print("Sorry you have to grow taller before you can ride.")


# with new addition of more payment options
height2 = int(input("What is your height in cm? "))

if height2 >= 120:
    print("You can ride the rollercoaster")

    # NEW where we check if they are over 18, less than 12 or between 12 and 18
    age2 = int(input("What is your age? "))
    if age2 > 18:
        print("Please pay the $12 adult fare")
    elif age2 < 12:
        print("Please pay the $5 kid fare")
    else:
        print("Please pay the $7 teen fare")
else:
    print("Sorry you have to grow taller before you can ride.")


# Coding Challenge

# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
# Refer to this graphic for help:

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")
