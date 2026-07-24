enemies = 1 # global scope


def increase_enemies():
    enemies = 2 # local scope
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# local scope
def drink_potion():
    position_strength = 2
    print(position_strength)

drink_potion()
# name error doesnt exist globally, only locally
    # print(portion_strength) #NameError: name 'portion_strength' is not defined


# global score
player_health = 10
def eat_healthy():
    print(player_health)

print(player_health)