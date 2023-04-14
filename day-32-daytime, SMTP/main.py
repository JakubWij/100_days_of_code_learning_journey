import smtplib
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

my_email = config['DEFAULT']['my_email']
password = config['DEFAULT']['password']


#
connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
# way of securing email
connection.starttls()
# login, remember to make msg as string and then encode it to .encode("utf8")
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Dzieki \n\nDziala")
connection.close()
print("done")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4, minute=20)
# print(date_of_birth)

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    with open("quotes.txt") as quote_file:
        main_file = quote_file.readlines()
        random_quote = random.choice(main_file)
# in theory we can now send random quote to ourself once a week but we cant because you cant accest gmail/yahoo
# mail from python
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(my_email, my_email)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs=my_email,
#                             msg=f"Subject:Monday Motivation\n\n{random_quote}")


