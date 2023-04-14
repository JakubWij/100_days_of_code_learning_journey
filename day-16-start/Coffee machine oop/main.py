from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

this_coffee_maker = CoffeeMaker()
current_menu = Menu()
current_money = MoneyMachine()


while True:
    choice = input(f"What would you like? {'/'.join(current_menu.get_items())}: ")
    if choice == "off":
        break
    elif choice == "report":
        this_coffee_maker.report()
        current_money.report()
    else:
        if current_menu.find_drink(choice) is not None:
            chosen_drink = current_menu.find_drink(choice)
            if this_coffee_maker.is_resource_sufficient(chosen_drink):
                if current_money.make_payment(chosen_drink.cost):
                    this_coffee_maker.make_coffee(chosen_drink)
