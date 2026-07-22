# Logical Operators

# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total = 0
is_senior = False

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    # special case for seniors
    if age >=45 and age <=55:
        print("Have a ride on US, Seniors ride for free")
        total = 0
    elif age > 18 and not is_senior:
        print("Adult tickets are $12")
        total = 12
    elif age < 12:
        print("Child tickets are $5")
        total = 5
    else:
        print("Teen tickets are $7")
        total = 7

    want_photo = input("Do you want a photo taken? Y (for Yes) or N (for No) for only $3 more? ")
    if want_photo == "Y":
        total += 3

    print(f"Your total for everything is ${total}")

else:
    print("Sorry you have to grow taller before you can ride.")
