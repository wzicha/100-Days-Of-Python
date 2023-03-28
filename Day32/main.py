##################### Hard Starting Project ######################

import datetime as dt
import random
import smtplib
import pandas

#email
#password

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

birthdays_dict_new = {}
# Create a dictionary from the dataframe with (month, day) tuples as keys
# and data rows as values
birthdays_dict = {}
for i, row in birthdays_df.iterrows():
    month = int(row["month"])
    day = int(row["day"])
    birthdays_dict[(month, day)] = row.to_dict()

# Get the current date
now = dt.datetime.now()

# Extract the month and day from the current date
current_month = now.month
current_day = now.day

# Check if today's date matches a birthday in the birthdays dictionary
if (current_month, current_day) in birthdays_dict:
    print("Today is a birthday! Data:", birthdays_dict[(current_month, current_day)])
else:
    print("No birthdays today.")

# HINT 1: Only the month and day matter.

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="wzicha@gmail.com", msg=f"Subject: Happy Birthday\n\n")
    connection.close()