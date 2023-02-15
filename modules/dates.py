import datetime

print(datetime.datetime.now()) # 2023-02-14 12:30:59.407944

print(datetime.datetime.now().year) # 2023

print(datetime.datetime(2023, 12, 18)) # 2023-12-18 00:00:00

# .str f time = formatting date objects into readable strings

print(datetime.datetime.now().strftime("%A")) # Tuesday
# Weekday, full version

print(datetime.datetime.now().strftime("%B")) # February
# Month name, full version

print(datetime.datetime.now().strftime("%C %W %j %I %p")) # 20 century, 07 week, 045 day number, 12 PM
