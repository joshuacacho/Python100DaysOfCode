import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# using the random.choice() function to select a random person from the list
random_person = random.choice(friends)
print(random_person)
print(random_person + " pays the bill")

# using the random.randint() function to select a random number between 0 and 4
random_number_index = random.randint(0, len(friends)-1) #-1 since lists are indexed / get out of bounds exception id dont -1
print(random_number_index)
print(friends[random_number_index] + " pays the bill")