MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")

def sufficient_resources (beverage, machine):
    for ingredients in beverage:
        if (beverage['ingredients']['water'] > machine['water']):
            print("Water is depleted")
            return False
        if (beverage['ingredients']['milk'] > machine['milk']):
            print("Milk is depleted")
            return False
        if (beverage['ingredients']['coffee'] > machine['coffee']):
            print("Coffee is depleted")
            return False
    else:
        return True

def choice_selection():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'espresso':
        selection = MENU['espresso']
        selection_name = 'espresso'
    elif drink == 'latte':
        selection = MENU['latte']
        selection_name = 'latte'
    elif drink == 'cappuccino':
        selection = MENU['cappuccino']
        selection_name = 'cappuccino'
    elif drink == 'off':
        exit()
    #Print report that shows the current resources available in the machine
    elif drink == 'report':
        report()
        return choice_selection()
    return selection, selection_name

def handle_money():
    print("Please insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickles = int(input("How many nickles?: "))
    num_pennies = int(input("How many pennies?: "))
    total_money = float(num_quarters*0.25 + num_dimes*0.1 + num_nickles*0.05 + num_pennies*0.01)
    return total_money

def deduct_resources(beverage, machine):
    for ingredients in machine:
        machine['water'] -= beverage['ingredients']['water']
        machine['milk'] -= beverage['ingredients']['milk']
        machine['coffee'] -= beverage['ingredients']['coffee']


machine = 'on'

while machine == 'on':

    #Prompt user to see what beverage they want from the coffee machine
    recipe, drink_type = choice_selection()
    #Check user's input

    #Show prompt after each action has completed (ex. after drink is dispensed)

    #Secret key word off to shut off the coffee machine




    #Check if resources are sufficient to make the beverage of their choice
    check = sufficient_resources(recipe, resources)

    if check == True:

            #If there are insufficient resources print message stating which resource is depleted
            #Handled in sufficient_resources()

            #Process coins, prompt users to input quarters, dimes, nickles, pennies
        money_inputted = handle_money()
            #Calculate monetary amount

            #Check if money is sufficient
        if money_inputted == recipe['cost']:
            print(f"Here is your {drink_type}. Enjoy!")
                #If money is not sufficient, refund the customer.
            resources['money'] += recipe['cost']
            deduct_resources(recipe,resources)
        elif money_inputted > recipe['cost']:
            reimburse_amount = float(money_inputted - recipe['cost'])
            print(f"Here is ${reimburse_amount} in change.")
            print(f"Here is your {drink_type}. Enjoy!")
            resources['money'] += recipe['cost']
            deduct_resources(recipe, resources)
        else:
            print("Sorry, that's not enough money. Money refunded.")
                #If money exceeds price amount, refund the excess

                #Add money to the report

                #Deduct resources from the report

                # Print out message telling customer to enjoy their drink

