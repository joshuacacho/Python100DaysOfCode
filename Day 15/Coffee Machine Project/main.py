# coffee machine program

#Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is
        # dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        # the machine. Your code should end execution when this happens.
# 3. Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows
        # the current resource values. e.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
# 4. Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
        # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        # not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
        # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
    # a. Check that the user has inserted enough money to purchase the drink they selected.
        # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        # program should say “Sorry that's not enough money. Money refunded.”.
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the
        # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change.
        # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
# 7. Make Coffee.
    # a. If the transaction is successful and there are enough resources to make the drink the
        # user selected, then the ingredients to make the drink should be deducted from the
            # coffee machine resources.
                # E.g. report before purchasing latte:
                # Water: 300ml
                # Milk: 200ml
                # Coffee: 100g
                # Money: $0
                # Report after purchasing latte:
                # Water: 100ml
                # Milk: 50ml
                # Coffee: 76g
                # Money: $2.5
    # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
        # latte was their choice of drink.

from coffee_data import MENU, resources
import sys


def resource_check(drink_choice,drink_choice_dictionary):
    """This function return True or False based on if there are enough ingredients to make the coffee choice"""

    ingredients = drink_choice_dictionary[drink_choice]["ingredients"]
    can_make_drink = True

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item} ")
            can_make_drink = False

    return can_make_drink

def calculate_user_payment(number_of_quarters, number_of_dimes, number_of_nickles, number_of_pennies):
    """This functions calculates the total user payment"""

    user_total_money = float((0.25 * number_of_quarters) + (.10 * number_of_dimes)
                             + (.05 * number_of_nickles) + (.01 * number_of_pennies))

    return user_total_money

def calculate_user_change(user_payment, drink_cost):
    """This function calculates the user change"""

    # calculate change amount
    user_change = float(round(user_payment - drink_cost, 2))

    return user_change


def no_yes_change_message(user_change):
    """This function takes into account the users change and determines which message to print"""

    if user_change == 0:
        user_change_message = f"Thanks for paying with exact change"
    else:
        user_change_message = f"Here is your ${user_change} in change"

    return user_change_message


# calculate money and update in resources
    # override cost with new money_in_business_account sale
def update_business_funds(current_money_in_account, drink_cost):
    business_account = float(current_money_in_account + drink_cost)
    resources["money"] = business_account
    print(resources["money"])

def update_inventory(drink_selection, drink_choice_dictionary):
    """This function updates the inventory anytime a sale is made and ingredients have been used"""

    # LEAVING HERE TO SHOW MY ERROR
        # I was subtracting the wrong values which would give me a negative number
            # left_over_item = inventory_list[item] - resources[item]
            # which resulted in inventory_list[item] = left_over_item also being incorrect because
                # WE NEED TO UPDATE our menu_item

    # inventory_list = coffee_ingredients[drink_selection]["ingredients"]
    # print(inventory_list)
    #
    #
    # for item in inventory_list:
    #     if resources[item]  in inventory_list[item]:
    #         left_over_item = inventory_list[item] - resources[item]
    #         print(f"You have {resources[item]} left over  {left_over_item}.")
    #         inventory_list[item] = left_over_item

    inventory_list = drink_choice_dictionary[drink_selection]["ingredients"]

    for item in inventory_list:
        if resources[item] > inventory_list[item]:
            left_over_item =  resources[item] - inventory_list[item]
            resources[item] = left_over_item


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
        if what_to_do == "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}")


        # TODO # 4. Check resources sufficient?
        #     a. When the user chooses a drink, the program should check if there are enough
        #         resources to make that drink.
        #     b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        #         not continue to make the drink but print: “Sorry there is not enough water.”
        #     c. The same should happen if another resource is depleted, e.g. milk or coffee.

        drink_choice = what_to_do
        while drink_choice not in ("espresso","latte","cappuccino","report", "off"):
            drink_choice = input("Incorrect selection, please choose one of your drinks? (espresso/latte/cappuccino): ").lower()

        enough_resources = False

        if drink_choice == "espresso":
            print("espresso")
            # print(resources["water"], MENU["espresso"]["ingredients"]["water"])
            enough_resources = resource_check(drink_choice, MENU)

        if drink_choice == "latte":
            print("latte")
            enough_resources = resource_check(drink_choice, MENU)

        if drink_choice == "cappuccino":
            print("cappuccino")
            enough_resources = resource_check(drink_choice, MENU)

        print(enough_resources)

        #Make Coffee if we have enough resources in shop to do so
        if enough_resources == True:
            print("yes")

            # TODO # 5. Process coins.
            #     # a. If there are sufficient resources to make the drink selected, then the program should
            #         # prompt the user to insert coins.
            #     # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            #     # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
            #         # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


            print("Please input your coins...")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))


            user_payment_total = calculate_user_payment(quarters, dimes, nickles, pennies)
            print(user_payment_total)

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

            espresso_cost = MENU["espresso"]["cost"]
            latte_cost =  MENU["latte"]["cost"]
            cappuccino_cost = MENU["cappuccino"]["cost"]
            money_in_business_account = resources["money"]

            if user_payment_total >= espresso_cost:

                print(espresso_cost)

                # user_change = float(round(money_in_business_account - user_payment_total,2))
                user_total_change = round(calculate_user_change(user_payment_total, espresso_cost),2)
                print(no_yes_change_message(user_total_change))

                # update business account funds
                update_business_funds(money_in_business_account, espresso_cost)

            elif user_payment_total >= latte_cost:

                # user_change = float(round(money_in_business_account - user_payment_total,2))
                user_total_change = round(calculate_user_change(user_payment_total, latte_cost), 2)
                print(no_yes_change_message(user_total_change))

                # update business account funds
                update_business_funds(money_in_business_account, latte_cost)

            elif user_payment_total >= cappuccino_cost:

                # user_change = float(round(money_in_business_account - user_payment_total,2))
                user_total_change = round(calculate_user_change(user_payment_total, cappuccino_cost), 2)
                print(no_yes_change_message(user_total_change))

                # update business account funds
                update_business_funds(money_in_business_account, cappuccino_cost)

            else:
                print("Sorry that's not enough money. Money refunded")
                coffee_machine() #recursion to start new coffee machine


        # print out enjoy latte message
        if enough_resources == True:
            # Update inventory now that item has been sold
            update_inventory(drink_choice, MENU)
            print(f"Here is your {drink_choice} ☕️, enjoy!")


coffee_machine()



