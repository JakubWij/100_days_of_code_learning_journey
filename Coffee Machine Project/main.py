from data import MENU
from data import resources


# Print report.
def resources_report():
    print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${machine_money}""")


def enough_money(coffee_type, money):
    if money >= MENU[f"{coffee_type}"]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Check resources sufficient?
def sufficiency_of_resources(coffee_type, resource):
    # prints and if returns true then we can keep going but maybe another variable for this...
    if coffee_type != "espresso" and resource != "milk":
        if MENU[f"{coffee_type}"]["ingredients"][resource] >= resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


# Process coins.
def total_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    dollars = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return dollars


# Make Coffee.
def coffee_maker(coffee_type, coins_inserted):
    global machine_money
    change = round(coins_inserted - MENU[f"{coffee_type}"]["cost"], 2)
    machine_money += MENU[f"{coffee_type}"]["cost"]
    resources["water"] = resources["water"] - MENU[f"{coffee_type}"]["ingredients"]["water"]
    if coffee_type != "espresso":
        resources["milk"] = resources["milk"] - MENU[f"{coffee_type}"]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[f"{coffee_type}"]["ingredients"]["coffee"]
    print(f"Here is your {change} in change.")
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


machine_money = 0
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off the Coffee Machine by entering “ off ” to the prompt. break to quit program for maintenance
    if choice == "off":
        break
    elif choice == "report":
        resources_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resource_list = ["milk", "coffee", "water"]
        choice_list = [choice, choice, choice]
        # map działa tak że zwraca z mojej funkcji false/true, zmieniam to na listę i sprawdzam czy w tej liśćie nie ma
        # False
        if False not in list(map(sufficiency_of_resources, choice_list, resource_list)):
            user_money = total_coins()
            if enough_money(choice, user_money):
                coffee_maker(choice, user_money)
    else:
        print("We dont have that in MENU :<")
