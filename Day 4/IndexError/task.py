states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

# print hawaii which is at index 49 or the 50th state
print(states_of_america[49])

# gives us IndexError: list index out of range
    # print(states_of_america[50])

# to get around IndexError: list index out of range
    # create length of states_of_america which is 50 and then minus offset to get the index you want
num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])


# Dirty Dozen List
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]

# Using the Dirty Dozen List how can we create a list of fruits and vegetables?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen_combined = [fruits, vegetables]
print(dirty_dozen_combined)

# to print item from a specific nested list within a list data structure made up of multiple lists
print(dirty_dozen_combined[1][1]) # first list is vegetables and first item is Kale



