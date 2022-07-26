# import smtplib
#
# my_email = 'testertesttester2008@gmail.com'
# password = 'euotbkohfhwkewfq'
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='ishkining@gmail.com', msg='Hello')


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
# date_of_birth = dt.datetime(year=1999, month=11, day=3)

# TODO 1: challenge send quote via email on the current weekday

import datetime
import smtplib
import random
import codecs

if datetime.datetime.now().weekday() == 1:
    my_email = 'testertesttester2008@gmail.com'
    password = 'euotbkohfhwkewfq'

    fileObj = codecs.open("quotes.txt", "r", "utf_8_sig")
    quotes = [str(quote).replace('”', '\"').replace('“', '\"').replace('–', '-') for quote in fileObj.read().split('\n')]
    fileObj.close()

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='ishkining@gmail.com',
                            msg=f'Subject: Hello\n\n{random.choice(quotes)}')
