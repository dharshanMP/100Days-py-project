

import smtplib
import datetime as dtm 
import random
import pandas


EMAIL = "shand3649@gmail.com"
PASSWORD = "qhtw jqqj uadc epif"

today = (dtm.datetime.now())
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv") 

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=file_path) as letter:
        content = letter.read()
        x = content.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=person["email"], msg=f"Happy Birthday\n\n{x}")





