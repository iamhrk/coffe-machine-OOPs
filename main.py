from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
menu_item = menu.get_items()

while True:
    user_input = input(f"What would you like? ({menu_item}):")
    if user_input == "off":
        break
    elif user_input == "report":
        coffee.report()
        money.report()
    elif user_input == "espresso" or "latte" or "cappuccino":
        drink = menu.find_drink(user_input)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
