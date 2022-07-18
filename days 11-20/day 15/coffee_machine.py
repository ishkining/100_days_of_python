# TODO: 1: prompt user by asking "What would u like?"

from coffee_data import MENU, resources

is_coffee_machine_turning_on = True
money = 0

while is_coffee_machine_turning_on:
    client_choice = input(f'What would you like? ({ "/".join([coffee for coffee in MENU]) }): ')

    # TODO: 2: Turn off the Coffee Machine by entering "off" to the prompt

    if client_choice == 'off':
        is_coffee_machine_turning_on = False
        continue

    # TODO: 3: Print Report

    elif client_choice == 'report':
        for resource in resources:
            print(f'{resource}: {resources[resource]}')
        print(f'money: ${money}')

    # TODO: 4: Check resources sufficient

    elif client_choice in [coffee for coffee in MENU]:
        is_resources_enough = True
        for ingridient in MENU[client_choice]["ingredients"]:
            if MENU[client_choice]["ingredients"][ingridient] > resources[ingridient]:
                is_resources_enough = False
                print(f'Sorry there is not enough {ingridient}')

        # TODO: 5: Proceess coins

        if is_resources_enough:
            print('Please insert the money:')
            quarters = float(input('how many quarters? '))
            dimes = float(input('how many dimes? '))
            nickles = float(input('how many nickles? '))
            pennies = float(input('how many pennies? '))

            sum_was_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies

            # TODO: 6: Check transaction successful

            if sum_was_inserted > MENU[client_choice]["cost"]:
                for ingridient in MENU[client_choice]["ingredients"]:
                    resources[ingridient] -= MENU[client_choice]["ingredients"][ingridient]
                money += MENU[client_choice]["cost"]
                change = sum_was_inserted - MENU[client_choice]["cost"]
                print(f'Here is {change} in change')
                print(f'Enjoy your {client_choice}')
            else:
                print('Sorry that\'s not enough money. Money refunded.')


    else:
        print('Choose coffee correctly')