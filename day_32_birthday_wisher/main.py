# #################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
birthday_data = pd.read_csv("birthdays.csv").to_dict(orient="records")
for data in birthday_data:
    if data["month"] == today.month and data["day"] == today.day:
        with open(f"./letter_templates/{random.choice(letters)}") as letter:
            letter_content = letter.readlines()
            final_draft = ""
            for line in letter_content:
                line = line.replace("[NAME]", data["name"])
                final_draft += line
        connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user="anirudhmounasamy@gmail.com", password="cskxzcmoescqpgkh")
        connection.sendmail(from_addr="anirudhmounasamy@gmail.com", to_addrs=data["email"],
                            msg=f"Subject:Happy Birthday\n\n{final_draft}")


