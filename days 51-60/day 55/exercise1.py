# Create the logging_decorator() function 👇


def logging_decorator(function):
    def wrapper(*args):
        print(f'You\'ve called a function {function.__name__}({", ".join([str(number) for number in args])})')
        return f'It returned {function(*args)}'
    return wrapper


@logging_decorator
def example_function(*args):
    return sum(args)


# Use the decorator 👇

print(example_function(1, 2, 3))
