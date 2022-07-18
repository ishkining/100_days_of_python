from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1: prompt user by asking "What would u like?"

is_coffee_machine_turning_on = True
coffee_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while is_coffee_machine_turning_on:
    client_choice = input(f'What would you like? ({ menu.get_items() }): ')

    # TODO: 2: Turn off the Coffee Machine by entering "off" to the prompt

    if client_choice == 'off':
        is_coffee_machine_turning_on = False
        continue

    # TODO: 3: Print Report

    elif client_choice == 'report':
        coffee_maker.report()
        money.report()

    # TODO: 4: Check resources sufficient

    elif menu.find_drink(client_choice):
        is_resources_enough = coffee_maker.is_resource_sufficient(menu.find_drink(client_choice))

        # TODO: 5: Proceess coins

        if is_resources_enough:

            # TODO: 6: Check transaction successful

            if money.make_payment((menu.find_drink(client_choice)).cost):
                coffee_maker.make_coffee(menu.find_drink(client_choice))

    else:
        print('Choose coffee correctly')