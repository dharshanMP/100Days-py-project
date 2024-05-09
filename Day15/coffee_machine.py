from details import MENU as menu
from details import resources 


profit = 0

def is_resource_sufficient(order_ingredients):
    
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(amt, drink_cost):
    if amt >= drink_cost:
        change = round(amt - drink_cost)
        print(f"here the {change} take it up!...")
        global profit
        profit += drink_cost
        return True
    else:
        print("insufficient amt.")
        return False

def coffee_making(drink_name, ingredients):
    for item in ingredients:
        resources[item] - ingredients[item]
    print(f"Here is your {drink_name} have it... ")

on = True

while on:
    user_need = input("What would you like to have? (espresso/ latte /cappuccino) ").lower()
    if user_need == "of":
        on = False
    elif user_need == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink =menu[user_need]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                coffee_making(user_need, drink["ingredients"])    