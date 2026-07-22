print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total = 0

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    if age > 18:
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
