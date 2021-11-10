from textwrap import dedent

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

# Coffee Machine Program Requirements
# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# 2. Turn off the Coffee Machine by entering "off" to the prompt.
# 3. Print report of all coffee machine resources
# 4. Check resources are sufficient to make drink order
# 5. Process coins.
# 6. Check that the transaction is successful (i.e. enough resources + money)
# 7. Make the coffee if the transaction is successful


def print_report():
    print(dedent(f"""\
        Water: {resources['water']}ml
        Milk: {resources['milk']}ml
        Coffee: {resources['coffee']}g
        Money: ${money}\
    """))


def enough_money(drink, amount_given):
    return amount_given >= MENU[drink]['cost']


def enough_water(drink):
    return resources['water'] >= MENU[drink]['ingredients']['water']


def enough_milk(drink):
    return resources['milk'] >= MENU[drink]['ingredients']['milk']


def enough_coffee(drink):
    return resources['coffee'] >= MENU[drink]['ingredients']['coffee']


def enough_resources(drink):
    """
    Checks if we have enough resources to make the specified drink.

    :param drink: The coffee we want to check whether we have enough ingredients for
    :return: True if there are enough ingredients, otherwise print an error message and return False
    """
    if not enough_water(drink):
        print("Sorry, there is not enough water.")
        return False

    if not enough_milk(drink):
        print("Sorry, there is not enough milk.")
        return False

    if not enough_coffee(drink):
        print("Sorry, there is not enough coffee.")
        return False

    return True


def ask_coins():
    """
    Asks the user the amount of quarters, dimes, nickels, and pennies they want to insert, in that order.

    :return: Float representing the total amount given, in dollars and cents.
    """
    n_quarters = int(input("How many quarters?: "))
    n_dimes = int(input("How many dimes?: "))
    n_nickels = int(input("How many nickels?: "))
    n_pennies = int(input("How many pennies?: "))
    return n_quarters * 0.25 + n_dimes * 0.10 + n_nickels * 0.5 + n_pennies * 0.01


def make_coffee(drink):
    """
    Attempts to make the specified drink.

    Succeeds if there are enough ingredients are present and if enough money is given.

    If successful, the required ingredients are subtracted from the coffee machine's resources, and the cost of the
    drink is added to the coffee machine.

    If not successful, an error message is printed, no ingredients are removed, and no money is added.

    :param drink: The drink to make (assumes valid drink)
    :return: None (but affects the state of the coffee machine)
    """
    global resources, money

    if not enough_resources(drink):
        return

    amount_given = ask_coins()
    if not enough_money(drink, amount_given):
        print("Sorry, that's not enough money. Money refunded.")
        return

    # At this point we have both enough ingredients and money -- make the coffee

    # Subtract the ingredients from the machine
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']

    # Add the money to the machine
    cost = MENU[drink]['cost']
    money += cost

    # Print response messages
    print(f"Here is ${cost} in change.")
    print(f"Here is your {drink} ☕ Enjoy!")


while True:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if response == 'espresso' or response == 'latte' or response == 'cappuccino':
        make_coffee(response)
    elif response == 'report':
        print_report()
    elif response == 'off':
        break
    else:
        print("Please make a valid selection")