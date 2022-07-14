# Write your code below this line 👇
def prime_checker(number):
    is_prime = True if number % 2 != 0 or number == 2 else False
    for checker in range(3, int(number / 2) + 1, 2):
        if number % checker == 0:
            is_prime = False

    if is_prime:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
