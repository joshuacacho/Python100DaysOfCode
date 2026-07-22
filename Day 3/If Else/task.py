print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You CAN ride the rollercoaster") #block of code
else:
    print("YOU CANT ride the rollercoaster until you are taller") #block of code


magicRideGoAgainNum = int(input("Guess the right number to ride again: "))

if magicRideGoAgainNum == 120:
    print("You guessed correctly! Ride again for FREE") #block of code
else:
    print("YOU CANT ride the rollercoaster until you are taller") #block of code
