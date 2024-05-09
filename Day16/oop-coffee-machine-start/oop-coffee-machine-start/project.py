from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee_making = CoffeeMaker()
menu = Menu()

on = True

while on:
    option = menu.get_items()
    user_need = input("What would you like to have? (espresso/ latte /cappuccino) : ").lower()
    if user_need == "of":
        on = False
    elif user_need == "report":
        coffee_making.report()
        money.report()
    else:
        drink = menu.find_drink(user_need)
        if coffee_making.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_making.make_coffee(drink)

