from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True

coffee_maker = CoffeeMaker()
menu = Menu()
cashier = MoneyMachine()

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        coffee_maker.report()
    elif user_choice == "off":
        is_machine_on = False
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                print(f"Enjoy you {drink.name}!")
                
