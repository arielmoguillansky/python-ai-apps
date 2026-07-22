import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random
import pandas

load_dotenv()

data = pandas.read_csv("birthdays.csv")

today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

my_email = os.getenv("SENDER_GMAIL_EMAIL")
password = os.getenv("GMAIL_APP_PASSWORD")


if today in birthdays_dict:
    bday_person = birthdays_dict[today]
    filet_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filet_path) as f:
        contents = f.read()
        mod_contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=bday_person["email"],
                            msg=f"Subject:Happy B-day!!\n\n{mod_contents}")


