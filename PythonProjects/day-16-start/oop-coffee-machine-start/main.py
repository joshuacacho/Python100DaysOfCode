# import the supported files

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

# create objects from each class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
#   a. Check the user’s input to decide what to do next.
#   b. The prompt should show every time action has completed, e.g. once the drink is
#       # dispensed. The prompt should show again to serve the next customer.

def coffee_machine():

    machine_running = True

    while machine_running:

        what_to_do = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO 2 - # 2. Turn off the Coffee Machine by entering “off” to the prompt.
        #     a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        #         the machine. Your code should end execution when this happens.
        if what_to_do == "off":
            sys.exit()

        # TODO 3. Print report.
        #   a. When the user enters “report” to the prompt, a report should be generated that shows
        #       the current resource values. e.g.
        #       Water: 100ml
        #       Milk: 50ml
        #       Coffee: 76g
        #       Money: $2.5
        elif what_to_do == "report":
            coffee_maker.report() # using OOP
            #also print money
            money_machine.report()


        # TODO # 4. Check resources sufficient?
        #     a. When the user chooses a drink, the program should check if there are enough
        #         resources to make that drink.
        #     b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        #         not continue to make the drink but print: “Sorry there is not enough water.”
        #     c. The same should happen if another resource is depleted, e.g. milk or coffee.


        elif what_to_do in ("espresso", "latte", "cappuccino"):

            drink_choice = what_to_do


        # THIS WILL NOT WORK AS DRINK CHOICE IS A STRING currently and NOT AN OBJECT
            # will return Error AttributeError: 'str' object has no attribute 'ingredients'
                # enough_resources = coffee_maker.is_resource_sufficient(menu.find_drink(drink_choice))

        # coffee_maker.is_resource_sufficient
            # Parameter drink: (MenuItem) The MenuItem object to make.
            # Prints a message if ingredients are insufficient.
            # Returns True when the drink order can be made, False if ingredients are insufficient.

        # menu.find_drink
            # find_drink(order_name)
            # Parameter order_name: (str) The name of the drinks order.
            # Searches the menu for a particular drink by name.
                # Returns a MenuItem object if it exists, otherwise returns None.

        # OOP using coffee maker and menu class
            # 1 pass drink choice (str) to menu.find_drink(str) and returns an object
            # 2 pass returned object from menu.find_drink(str) into coffee_maker.is_resouce_sufficient(object)
            enough_resources = coffee_maker.is_resource_sufficient(menu.find_drink(drink_choice))

            print(f"Enough resources is {enough_resources}")

            # Make Coffee if we have enough resources in shop to do so
            if enough_resources:

                # TODO # 5. Process coins.
                #     # a. If there are sufficient resources to make the drink selected, then the program should
                #         # prompt the user to insert coins.
                #     # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
                #     # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
                #         # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

                # TODO 6. Check transaction successful?
                #   a. Check that the user has inserted enough money to purchase the drink they selected.
                #    #   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
                #    #   program should say “Sorry that's not enough money. Money refunded.”.
                #   b. But if the user has inserted enough money, then the cost of the drink gets added to the
                #    #   machine as the profit and this will be reflected the next time “report” is triggered. E.g.
                #    #   Water: 100ml
                #    #   Milk: 50ml
                #    #   Coffee: 76g
                #    #   Money: $2.5
                #   c. If the user has inserted too much money, the machine should offer change.
                #       # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

                # OOP to process coins from user
                    # use menu.find_drink(<drink>) first find the drink choice of the user THEN
                    # use money_machine.make_payment(<cost>) referencing the .cost attribute of the drink choice
                user_drink_selection = menu.find_drink(drink_choice)
                print(f"User drink choice information is {user_drink_selection.name}")
                is_enough_money = money_machine.make_payment(user_drink_selection.cost)
                print(f"Enough money is {is_enough_money}")

                # if there is enough money use the coffee_maker.make_coffee(<drink selected to be made>)
                    # to print out the drink selection made
                if is_enough_money:
                    print(coffee_maker.make_coffee(user_drink_selection)) # OOP
                # 4. Handle invalid inputs
        else:
            print("Incorrect selection. Please try again.")

coffee_machine()
