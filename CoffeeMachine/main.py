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

# Coffee Machine Program Requirements
# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
# TODO: 3. Print report of all coffee machine resources
# TODO: 4. Check resources are sufficient to make drink order
# TODO: 5. Process coins.
# TODO: 6. Check that the transaction is successful (i.e. enough resources + money)
# TODO: 7. Make the coffee if the transaction is successful
