import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y") #str= string, f= format, time

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1) #1st datetime= the module and the 2nd= the class
current_datetime = datetime.datetime.now()                 #1st datetime= the module and the 2nd= the class

print(now)

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")