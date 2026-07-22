# function to return name with title case
def format_name(f_name, l_name):
    title_name_case = f"{f_name} {l_name}"
    return title_name_case.title() # title case

# not saving into variable
print(format_name("JOEY", "LORENZO"))

# saving into variable
output_format_name = format_name("anGOLa", "yU")
print(output_format_name)

# scope for functions
    # the return keyword ends the function
        # notice the print statement never gets executed
def add(num1, num2):
    return num1 + num2
    print("This will never execute")

addition = add(5,4)
print(addition)

# functions with inputs where inputs are taken
def add_inputs(num1,num2):
    return int(num1) + int(num2)

addition_inputs = add_inputs(input("What is the first number: "), input("What is the second number: "))
print(addition_inputs)

# functions with multiple returns based on user input
    # initial return terminates function early
    # second return returns first name and second name
def format_name_multiple_returns(f_name, l_name):
    if f_name == "" or l_name == "":
        return

    title_name_case = f"{f_name} {l_name}"
    return title_name_case.title() # title case

# not saving into variable
return_or_terminate = format_name_multiple_returns(input("What is the first name: "), input("What is the last name "))
print(return_or_terminate)


