from datetime import datetime, date

now = datetime.now()

print("Date & Time: ",now)
print("Date: ",now.date()) #extract date only
print("Year: ",now.year)
print("Month: ",now.month)
print("Day: ",now.day)
print("Hour: ",now.hour)
print("Minute: ",now.minute)

print(date.today())# just give date

myday= date(2023,12,25)
print(f"Specific Date: {myday}")

print("Default Date and time: ",now)
print(f"Format: {now.strftime("%d-%m-%Y %H:%M:%S")}")
# strftime format strings and convert it from date to string type

## How to convert string to date again
## using parse : strptime

date_str="2025-05-03"
date_ob= datetime.strptime(date_str,"%Y-%m-%d")
print(date_ob)