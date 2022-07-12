# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / (height ** 2), 2)
first_line = f'Your BMI is {bmi}, you are '
if bmi > 35:
    print(first_line + 'clinically obese')
elif bmi > 30:
    print(first_line + 'obese')
elif bmi > 25:
    print(first_line + 'slightly overweight')
elif bmi > 18.5:
    print(first_line + 'normal weight')
else:
    print(first_line + 'underweight')
