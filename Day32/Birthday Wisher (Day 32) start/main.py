import datetime as dt
import random
import smtplib

with open("quotes.txt", "r") as data:
    quotes = data.readlines()
    quote = random.choice(quotes)

print(quote)

# email
# password

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
# Monday = 0

if day_of_week == 0:
    print("Today is Monday")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="wzicha@gmail.com", msg=f"Subject: Happy Monday\n\n{quote}")
        connection.close()
