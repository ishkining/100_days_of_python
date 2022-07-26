##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib

EMAIL = 'testertesttester2008@gmail.com'
PASSWORD = 'euotbkohfhwkewfq'

# 1. Update the birthdays.csv

birthdays_data = pandas.read_csv('birthdays.csv')
birthdays_dict = birthdays_data.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv

now = datetime.datetime.now()
who_has_birthday_today = [item for item in birthdays_dict if item['month'] == now.month and item['day'] == now.day]

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv

if who_has_birthday_today:
    wish_templates = [f'letter_templates/letter_{number}.txt' for number in range(1, 4)]
    for happy_person in who_has_birthday_today:
        with open(random.choice(wish_templates)) as templates_file:
            message = templates_file.read().replace('[NAME]', happy_person['name'])

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=happy_person['email'], msg=message)


