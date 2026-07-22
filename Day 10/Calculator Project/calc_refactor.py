from art import logo

def list_operators():
    """This function just prints the available simple calculator options to the user"""
    print("+")
    print("-")
    print("*")
    print("/")


def calc_function(calc_choice, fir_number, sec_number):
    """This function takes the user operator choice and performs the associated calculation"""
    calculation = float(0)
    if calc_choice == "+":
        calculation = fir_number + sec_number
    elif calc_choice == "-":
        calculation = fir_number - sec_number
    elif calc_choice == "*":
        calculation = fir_number * sec_number
    elif calc_choice == "/":
        if sec_number == 0:
            return "Error: Division by zero" # terminate function
        calculation = fir_number / sec_number
    return calculation


# Wrap your game loop inside a main function
def calculator():

    # print the logo
    print(logo)

    # take the users first set of inputs
    first_number = float(input("What is your first number?: "))
    list_operators()
    operator_choice = input("Pick an operation: ")
    second_number = float(input("What's the second number: "))

    # Calculate the first result
    my_calc = calc_function(operator_choice, first_number, second_number)
    print(f"{first_number} {operator_choice} {second_number} = {my_calc}")

    # ask the user if they want to keep calculating or not
        # if y go to while loop, if n go to if statement
    keep_calculating = input(
        f"Type 'y' to continue calculation with {my_calc}, or type 'n' to start a new calculator: ")

    #With == "y", only an exact "y" continues the loop — anything else,
        # including typos, falls through to the restart/exit path
    while keep_calculating == "y":
        list_operators()
        ongoing_operator_choice = input("Pick an operation: ")
        next_num_to_include = float(input("What's the next number: "))

        new_result = calc_function(ongoing_operator_choice, my_calc, next_num_to_include)
        print(f"{my_calc} {ongoing_operator_choice} {next_num_to_include} = {new_result}")

        # update my_calc to new_result to keep
        my_calc = new_result
        keep_calculating = input(
            f"Type 'y' to continue calculation with {my_calc}, or type 'n' to start a new calculator: ")

    # If they typed 'n' (or anything else), clear and restart completely
    if keep_calculating == "n":
        print("\n" * 20)  # clear screen
        calculator()  # This is recursion! It starts a brand new calculator fresh.


# Start the calculator for the first time
calculator()