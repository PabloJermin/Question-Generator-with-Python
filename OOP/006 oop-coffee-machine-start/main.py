from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()
menu = Menu()
machine_on = True
coffee_maker = CoffeeMaker()
coffee_maker.report()

# geting the request
while machine_on:
    options = menu.get_items()
    choice = input(f"what is do you want to order? ({options}):")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker = CoffeeMaker()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)




