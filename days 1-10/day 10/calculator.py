from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)


def calculator():
    num1 = float(input('What\'s the first number: '))

    for symbol in operations:
        print(symbol)

    continue_loop = True
    while continue_loop:
        operation_symbol = input('Pick ops: ')
        num2 = float(input('What\'s the first number: '))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        if input(f'type \'y\' to continue wiht {answer}, or \'n\' to exit') == 'y':
            num1 = int(input('What\'s the first number: '))
        else:
            continue_loop = False
            calculator()


calculator()
