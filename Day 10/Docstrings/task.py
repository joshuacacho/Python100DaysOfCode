# function to return name with title case
def format_name(f_name, l_name):
    title_name_case = f"{f_name} {l_name}"
    return title_name_case.title() # title case

# saving into variable
my_format_name = format_name("JOEY", "LORENZO")
print(my_format_name)

length = len(my_format_name)
print(length)



# Creating documentation using DocStrings for our project
def add_two_numbers(num1,num2):
    """This function adds two numbers together"""
    return int(num1)+int(num2)

add_two_numbers(5,4)


