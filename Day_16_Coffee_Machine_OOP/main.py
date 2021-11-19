from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Coffee Machine Program Requirements
# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# 2. Turn off the Coffee Machine by entering "off" to the prompt.
# 3. Print report of all coffee machine resources
# 4. Check resources are sufficient to make drink order
# 5. Process coins.
# 6. Check that the transaction is successful (i.e. enough resources + money)
# 7. Make the coffee if the transaction is successful

# Initialize Component
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

# Main Loop
while True:
    response = input(f"What would you like? ({menu.get_items()[:-1]}): ")

    if response == 'off':
        break
    elif response == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drinkItem = menu.find_drink(response)

        if not drinkItem:
            continue

        if not coffeeMaker.is_resource_sufficient(drinkItem):
            continue

        if not moneyMachine.make_payment(drinkItem.cost):
            continue

        coffeeMaker.make_coffee(drinkItem)
