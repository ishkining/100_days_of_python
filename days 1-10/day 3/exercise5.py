# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

total1 = (name1+name2).count('t') + (name1+name2).count('r') + \
    (name1+name2).count('u') + (name1+name2).count('e')

total2 = (name1+name2).count('l') + (name1+name2).count('o') + \
    (name1+name2).count('v') + (name1+name2).count('e')

total = int(str(total1) + str(total2))

first_line = f'Your score is **{total}**'
if total > 90 or total < 10:
    print(first_line + ', you go together like coke and mentos')
elif total >= 40 and total <= 50:
    print(first_line + ', you are alright together')
else:
    print(first_line + '.')
