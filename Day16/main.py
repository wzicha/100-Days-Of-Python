from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize coffee maker
coffee_maker = CoffeeMaker()

# Initialize money machine
money_machine = MoneyMachine()

# Initialize Menu and menu contents.
Coffee_menu = Menu()
menu_contents = Coffee_menu.get_items()
machine_running = True
while machine_running == True:

    # Prompt user to make a selection
    user_selection = input(f"What would you like? {menu_contents}: ")
    if user_selection == 'report':
        # Initialize report log
        report_log = coffee_maker.report()
        money_report = money_machine.report()
    # Shut machine off if user wants to
    elif user_selection == 'off':
        machine_running = False
    # Find the drink that the user selected
    else:
        drink = Coffee_menu.find_drink(user_selection)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
