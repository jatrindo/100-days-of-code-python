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
# TODO: 5. Process coins.
# TODO: 6. Check that the transaction is successful (i.e. enough resources + money)
# TODO: 7. Make the coffee if the transaction is successful


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


while True:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if response == 'espresso' or response == 'latte' or response == 'cappuccino':
        pass
    elif response == 'report':
        print_report()
    elif response == 'off':
        break
    else:
        print("Please make a valid selection")

