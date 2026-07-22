from art import logo

# print the logo for the calculator project
print(logo)

def list_operators():
    """This function just prints the available simple calculator options to the user"""
    print("+")
    print("-")
    print("*")
    print("/")


first_number = float(input("What is your first number?: "))
list_operators()
operator_choice = input("Pick an operation: ")
second_number = float(input("What's the second number: "))


def calc_function(calc_choice, fir_number, sec_number):
    """This function takes the user operator choice and performs the associated calculation"""

    calculation = float(0)

    if calc_choice == "+":
        calculation =  fir_number + sec_number
    elif calc_choice == "-":
        calculation = fir_number - sec_number
    elif calc_choice == "*":
        calculation = fir_number * sec_number
    elif calc_choice == "/":
        calculation = fir_number / sec_number

    return calculation


def calc_once(first_num, oper_choice, second_num):

    # input operator_choice from user and perform associated calculation from within calc_function
    calculated_result = float(calc_function(operator_choice, first_num, second_num))
    print(f"{first_num} {oper_choice} {second_num} = {calculated_result}")

    return calculated_result

my_calc = calc_once(first_number, operator_choice, second_number)


keep_calculating = input(f"Type 'y' to continue calculation with {my_calc}, or type 'n' to start a new calculator: ")

while keep_calculating != "n":
    list_operators()
    ongoing_operator_choice = input("Pick an operation: ")
    new_number = float(input("Whats the next number: "))
    new_result = calc_function(ongoing_operator_choice, my_calc,new_number)
    print(f"{my_calc} {ongoing_operator_choice} {new_number} = {new_result}")
    my_calc = new_result
    keep_calculating = input(
        f"Type 'y' to continue calculation with {my_calc}, or type 'n' to start a new calculator: ")

print("\n" * 20) # clear screen
first_number = float(input("What is your first number?: "))
list_operators()
operator_choice = input("Pick an operation: ")
second_number = float(input("What's the second number: "))

print(calc_once(first_number, operator_choice, second_number))










