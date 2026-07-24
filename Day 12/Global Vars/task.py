# Modifying Global Scope

enemies = 1

# example of using local enemies value where we have to initialize it within the function
    # local scope
def increase_enemies():
    enemies = 0
    enemies += 1
    print(f"enemies inside function: {enemies}") # 1


increase_enemies()
print(f"enemies outside function: {enemies}") # 1


# example of using same concept from above but calling the function to
    # EXPLICITLY USE the   work global within the function

friends = 1

if friends == 1:
    print("you only have one friend")

def increase_friends():
    global friends # this means use the global friends value above
    friends = friends + 1
    print(f"friends inside function {friends}")

increase_friends()

# its not good practice to use the global keyword
    # to get around above statement as within Python just pass a value and return it

randoms = 1

def increase_randoms(random):
    print(f"Random people met so far today is {randoms}")
    random = random + 1

    return random

# set variable to function and then print it
random_people_met_today = increase_randoms(5)
print(f"Random people at end of day is {random_people_met_today}")



