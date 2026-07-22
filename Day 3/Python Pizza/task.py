# todo: work out how much they need to pay based on their size choice
# todo: work out how much to add to their bill based on their pepperoni choice
# todo: work out their final amount based on whether it they want extra cheese

# Example

# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.

print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S ($15), M ($20) or L ($25): ")
total = 0

if pizza_size == "S":
    total = 15
    print(f"Your total is {total} so far")

    add_pepp = input("Do you want pepperoni on your pizza for only $2 more? Y or N: ")
    if add_pepp == "Y":
        total += 2
    print(f"Your total is {total} so far")
elif pizza_size == "M":
    total = 20
    print(f"Your total is {total} so far")

    add_pepp = input("Do you want pepperoni on your pizza for only $3 more? Y or N: ")
    if add_pepp == "Y":
        total += 3

    print(f"Your total is {total} so far")
else: #pizza size is large
    total = 25
    print(f"Your total is {total} so far")

    add_pepp = input("Do you want pepperoni on your pizza for only $3 more? Y or N: ")
    if add_pepp == "Y":
        total += 3

    print(f"Your total is {total} so far")

# common and doesnt care about pizza size so can put at the end as it doesnt apply to above
add_extra_cheese = input("Do you want extra cheese for only $1 more? Y or N: ")
if add_extra_cheese == "Y":
    total += 1

print(f"Your final bill is {total}")
