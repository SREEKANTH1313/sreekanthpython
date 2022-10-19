
from datetime import datetime
from datetime import date
import time
today = date.today()


def user_birthday():
    year = int(input('Please Enter your birth of day: '))
    month = int(input('Please Enter your birth of Month:  '))
    day = int(input('Please Enter your birth of year: '))
    birthday = datetime(day, month, year)
    return birthday

try:
    def calculate_dates(birthday):
       today = date.fromtimestamp(time.time())
       birthday = date(today.year, birthday.month, birthday.day)
       if birthday < today:
           birthday = birthday.replace(year=today.year + 1, day=birthday.day+1)
           return birthday
       elif birthday == today:
           print("Happy Birthday")
           birthday = birthday.replace(year=today.year, day=birthday.day)
           return birthday
       elif birthday > today:
            birthday = birthday.replace(year=today.year, day=birthday.day-1)
            return birthday

       else:
           return birthday


except:
     print("Happy bu")


Birthday = user_birthday()
t = calculate_dates(Birthday)
time_to_birthday = abs(t - today)
days = str(time_to_birthday.days)
current_time = datetime.now()
hours = 24 - current_time.hour
minutes = 60 - current_time.minute
seconds = 60 - current_time.second
print("Your Next Birthday comes within : " + days + " days", ",",  hours, "hours", ",", minutes, "minutes", "and",
      seconds, "Seconds")

#Outpu
# Please Enter your birth of day: 04
# Please Enter your birth of Month:  01
# Please Enter your birth of year: 2000
# Your Next Birthday comes within : 78 days , 3 hours , 28 minutes and 55 Seconds

