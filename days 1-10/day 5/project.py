# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
result = ''
for index in range(0, nr_letters):
    result += letters[random.randint(0, len(letters) - 1)]

for index in range(0, nr_symbols):
    result += symbols[random.randint(0, len(symbols) - 1)]

for index in range(0, nr_numbers):
    result += numbers[random.randint(0, len(numbers) - 1)]

print(result)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

array_of_result = [character for character in result]  # or list(result)

for index in range(0, len(result)):
    random_index1 = random.randint(0, len(result) - 1)
    random_index2 = random.randint(0, len(result) - 1)
    if random_index1 != random_index2:
        holder = array_of_result[random_index1]
        array_of_result[random_index1] = array_of_result[random_index2]
        array_of_result[random_index2] = holder

result = ''.join(array_of_result)
print(result)
