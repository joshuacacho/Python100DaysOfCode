capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nested list in above dictionary
travel_log = {
    # we cant do the below as a dictionary can only have 1 key and 1 pair value if its written like below
        # "France" : "Paris", "Niece"

    # to get around the above we can do the following
        # the value(s) in this care a list
    "France" : ["Paris","Lille","Dijon"],
    'Germany' : ["Berlin", "Munich"],
}

# Challenge
# See if you can figure out how to print out "Lille" from the nested List called travel_log.
print(travel_log["France"][1])


# Many layered nested list
# Challenge
# See if you can figure out how to print C from the nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

# Nested Dictionary with a Dictionary and containing a nested list
    # more complex with more key value pairs associated and much better away of organizing data
nested_dictionary = {
    "France" : {
        "num_times_visited" : 2,
        "cities_visited" : ["Paris", "Niece"]
    },
    "Germany" : ["Frankfurt", "Stuggart"],
    "USA" : {
        "num_times_visited" : 3,
        "cities_visited" : ["San Diego", "Los Angeles", "New York"]
    },
}

# Challenge
# See if you can figure out how to print San Diego from Germany cities_visited from within nested_dictionary
print(nested_dictionary["USA"]["cities_visited"][0])
