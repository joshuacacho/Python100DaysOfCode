# Lists

# previously we have defined all states, 1 per variable
    # california = CA
    # texas = TX


# we can define a list of states
    # lists data structures
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
                     "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# pulling item from front of list using variable[indexValue]
    # the first item is at index 0 because it starts at 0
print(states_of_america[0])

# pulling item from END of list using variable[-indexValue]
    # the last item is at index -1 because you cant put -0
print(states_of_america[-1])


# Altering list items
states_of_america[0] = "Delware" # updating the spelling
print(states_of_america[0])
states_of_america[0] = "Delaware" # putting it back to its correct spelling
print(states_of_america[0])

# Adding items to the end of a list
states_of_america.append("Purity")
print(states_of_america) # purity is added to the end of the list

# remove items from a list
states_of_america.remove("Purity") #remove Purity from the list
print(states_of_america)


