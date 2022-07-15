#from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)
are_all_people_in = False
list_of_bidders = []

while not are_all_people_in:
    name = input('Input your name: \n')
    money = input('Inpuy your bid: $\n')
    continue_loop = input(
        'Is there someone else who wants to bid? yes or no? \n')

    list_of_bidders.append({
        'name': name,
        'money': money
    })

    if continue_loop == 'no':
        are_all_people_in = True

    # clear()

max_bid = list_of_bidders[0]["money"]
max_index = 0
for item in range(1, len(list_of_bidders)):
    if list_of_bidders[item]["money"] > max_bid:
        max_bid = list_of_bidders[item]["money"]
        max_index = item

print(
    f'Winner name: {list_of_bidders[max_index]["name"]}, his/her bid: ${max_bid}')
