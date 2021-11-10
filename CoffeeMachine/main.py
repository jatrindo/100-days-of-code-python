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
        Money: ${money:.2f}\
    """))


def enough_money(drink, amount_given):
    return amount_given >= MENU[drink]['cost']


def enough_resources(required_ingredients):
    """
    Checks if we have enough resources to make the specified drink.

    :param required_ingredients: A dict representing the resources required to make the drink. Keys are ingredient
    names, values are ints
    :return: True if there are enough ingredients, otherwise print an error message and return False
    """
    for ingredient in required_ingredients:
        if required_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
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
    return n_quarters * 0.25 + n_dimes * 0.10 + n_nickels * 0.05 + n_pennies * 0.01


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

    drink_ingredients = MENU[drink]['ingredients']
    if not enough_resources(drink_ingredients):
        return

    amount_given = ask_coins()
    if not enough_money(drink, amount_given):
        print("Sorry, that's not enough money. Money refunded.")
        return

    # At this point we have both enough ingredients and money -- make the coffee

    # Subtract the ingredients from the machine
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]

    # Add the money to the machine
    cost = MENU[drink]['cost']
    change = amount_given - cost
    money += cost

    # Print response messages
    print(f"Here is ${change:.2f} in change.")
    print(f"Here is your {drink} ☕ Enjoy!")


while True:
    options = '/'.join(MENU.keys())
    response = input(f"What would you like? ({options}): ").lower()

    if MENU.get(response):
        make_coffee(response)
    elif response == 'report':
        print_report()
    elif response == 'off':
        break
    else:
        print("Please make a valid selection")