# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: bids}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# extra - just import the logo
from art import logo

# print logo
print(logo)

# empty dictionary
bids = {}

print("Welcome to the secret auction program")

# TODO-1: Ask the user for input
user_name = input("Whats your name?: ")
user_bid = input("What is your bid?: $")

# TODO-2: Save data into dictionary {name: bids}
# Adding information to a dictionary
    # programming_dictionary["While Loop"] = "Do something over and over until the logic is no longer true/false"
bids[user_name] = user_bid # output of {'John': '50'}

# TODO-3: Whether if new bids need to be added
more_bidders = input("Are there any other bidders besides you? Type 'yes' or 'no': ").lower()

while more_bidders != "yes" and more_bidders != "no":
    more_bidders = input("Incorrect response, please try again! "
                         "Are there any other bidders besides you? Type 'yes' or 'no': ").lower()

while more_bidders != "no":
    print("\n" * 20) # clear screen
    user_name = input("Whats your name?: ")
    user_bid = input("What is your bid?: $")
    bids[user_name] = user_bid
    more_bidders = input("Are there any other bidders besides you? Type 'yes' or 'no': ").lower()

# TODO-4: Compare bids in dictionary and print out biggest one
# this only prints the value, NOT THE KEY
    # for key in test_dictionary:
    #     print(test_dictionary[key])
highest_bid = 0
highest_key = None
for key in bids:
    if int(bids[key]) > int(highest_bid):
        highest_bid = bids[key]
        highest_key = key

print("\n" * 20) # clear screen
print(bids)
print(f"The winning bidder is {highest_key} with a bid of ${highest_bid}")



