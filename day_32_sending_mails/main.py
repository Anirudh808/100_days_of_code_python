import datetime as dt
import random
import smtplib

today = dt.datetime.now().weekday()

if today == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
    today_quote = random.choice(quotes)
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user="anirudhmounasamy@gmail.com", password="cskxzcmoescqpgkh")
    connection.sendmail(from_addr="anirudhmounasamy@gmail.com", to_addrs="anirudhmounasamy@gmail.com",
                        msg=f"Subject:Monday Motivational Quote\n\n{today_quote.strip()}")
