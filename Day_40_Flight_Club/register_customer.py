"""
Script to add a new customer to the database
"""
from data_manager import DataManager

data_sheet = DataManager()


def ask_customer_info():
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")

    while True:
        email = input("What is your email?\n")
        retyped_email = input("Type your email again.\n")

        if email == retyped_email:
            data_sheet.add_customer(first_name, last_name, email)
            print("You're in the club!")
            break

        print("Emails didn't match. Try again")


print("Welcome to Flight Club!\nWe find the best flight deals and email you.")
ask_customer_info()
