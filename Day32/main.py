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

# Create a dictionary from birthdays.csv
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
# Only the month and day matter.

current_month = now.month
current_day = now.day

# Check if today's date matches a birthday in the birthdays dictionary
if (current_month, current_day) in birthdays_dict:
    print("Today is a birthday!")
    name = birthdays_dict[(current_month, current_day)]["name"]
    email = birthdays_dict[(current_month, current_day)]["email"]
    # Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    variation = random.randint(1, 3)
    with open(f'letter_templates/letter_{variation}.txt', 'r') as file:
        text = file.read()
        new_string = text.replace("[NAME]", f"{name}").replace("Angela", "Capy")
        print(new_string)
else:
    print("No birthdays today.")


# Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs={email}, msg=f"Subject: Happy Birthday\n\n{new_string}")
    connection.close()
