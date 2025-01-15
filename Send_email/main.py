# import smtplib
#
# my_email = ""
# password = ""
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="",msg="Subject:Hello\n\n This is the body of the email")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# dob = dt.datetime(year=2003, month=3 , day=5)
# print(dob )
#
# with open("quotes.txt") as data:
#


import smtplib
import datetime as dt
import random


my_email = ""
password = ""


now = dt.datetime.now()

weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        print(quote)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="",
                                msg=f"Subject:Monday Motivation \n\n{quote}"
                                )

