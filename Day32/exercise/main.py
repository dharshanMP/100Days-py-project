import smtplib
import datetime as dtm
import random 

EMAIL = "shand3649@gmail.com"
PASSWORD = "qhtw jqqj uadc epif"

current = dtm.datetime.now()
weekday = current.weekday()
if weekday == 6:  # Sunday is represented by 6
    with open(file="quotes.txt") as quote_file:
        line_by_line = quote_file.readlines()
        quote_note = random.choice(line_by_line)         
        print(quote_note)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: Sunday Quotes\n\n{quote_note}"
        )
