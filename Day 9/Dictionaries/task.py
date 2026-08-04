#Defining a Dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again"
}


# Pulling information from a dictionary
    # dictionary_name[key]
print(programming_dictionary["Bug"])

# Adding information to a dictionary
programming_dictionary["While Loop"] = "Do something over and over until the logic is no longer true/false"

print(programming_dictionary["While Loop"])

# tips
# 1 - Best to start out with empty dictionary sometimes when coding and add on as needed
empty_dictionary = {}

# emptying a dictionary
programming_dictionary = {}
print(programming_dictionary)

# adding something again to the dictionary and then editing the item
programming_dictionary["While Loop"] = "Do something over and over until the logic is no longer true/false"
programming_dictionary["While Loop"] = "This is an update to the existing value above"
print(programming_dictionary["While Loop"])


# looping through a dictionary
test_dictionary = {
    "Dog": "Barks",
    "Cat": "Meows",
    "Panther" : "Growls"
}

# this only prints the key, NOT THE VALUE
for key in test_dictionary:
    print(key)

# this only prints the value, NOT THE KEY
for key in test_dictionary:
    print(test_dictionary[key])

# this prints the key and value
for key in test_dictionary:
    print(key, test_dictionary[key] )



# Coding Challenge
# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
    # The keys in student_scores are the names of the students and the values are their exam scores.

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.
    # Traditional key:pair values
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain
    # student names as keys and their assessed grades for values.

# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"
student_grades = {

}

for key in student_scores: # key is the name of the students
    if student_scores[key] >= 91:
        print("Outstanding")
        # # Adding information to a dictionary
        # programming_dictionary["While Loop"] = "Do something over and over until the logic is no longer true/false"
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <=90:
        print("Exceeds Expectations")
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        print("Acceptable")
        student_grades[key] = "Acceptable"
    else:  # Scores 70 or lower: Grade = "Fail"
        print("Fail")
        student_grades[key] = "Fail"

print(student_grades)