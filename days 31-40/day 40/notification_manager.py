import smtplib


class NotificationManager:

    def __init__(self):
        self.email = 'testertesttester2008@gmail.com'
        self.password = 'euotbkohfhwkewfq'

    def send_message(self, data_about_flight, data_about_users):
        message_subject = 'Subject: News from cheapest airlines!'
        message_flight = f'Departure Aita: {data_about_flight["departure_aita"]}\n' \
                         f'Destination Aita: {data_about_flight["destination_aita"]}\n' \
                         f'Departure City: {data_about_flight["departure_city"]}\n' \
                         f'Destination City: {data_about_flight["destination_city"]}\n' \
                         f'Departure Date: {data_about_flight["departure_date"]}\n' \
                         f'Arrival Date: {data_about_flight["arrival_date"]}\n' \
                         f'Price: ${data_about_flight["price"]}\n'
        for user in data_about_users:
            message_user = f'Dear, {user["lastName"]} {user["firstName"]}.\n' \
                           f'We have some good news about cheapest airlines:'
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(from_addr=self.email, to_addrs=user['email'],
                                    msg=f'{message_subject}\n\n{message_user}\n{message_flight}')
