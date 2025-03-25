import smtplib
import random
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")

with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()


todays_quote = random.choice(quotes_list)


with open("email_list.txt", "r") as emails:
    emails_list = emails.readlines()



for email in emails_list:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=(f"Subject:Daily Motivation\n\n {todays_quote} \n Yes you will get this everyday")
        )
