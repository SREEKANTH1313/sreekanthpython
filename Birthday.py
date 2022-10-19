# # import datetime
# # birthday_year = int(input("Enter Your year: \n ,Enter Your Month: \n ,Enter Your Day:"))
# # age = datetime.datetime.now().year - birthday_year
# # print("Your age is :", age)
#
# import datetime
# currentDate = datetime.datetime.now()
# # Input details
# Birth = input('Plz enter your date of birth (mm/dd/yyyy): ')
# Date = datetime.datetime.strptime(Birth, '%m/%d/%Y')
# print(Date)
# completed_days = currentDate - Date
# print(completed_days)
# # calculate years
# years = ((completed_days.total_seconds()) / (365 * 24 * 60 * 60))
# yearsInt = int(years)
# # calculate Months
# months = (years-yearsInt) * 12
# monthsInt = int(months)
# # calculate Days
# Days = (months - monthsInt) * (365 / 12)
# daysInt = int(Days)
# # calculate In Hours
# Hours = (Days - daysInt) * 24
# hoursInt = int(Hours)
# # calculate in Minutes
# In_Minutes = (Hours - hoursInt) * 60
# minutesInt = int(In_Minutes)
# # calculate In Seconds
# In_Seconds = (In_Minutes - minutesInt) * 60
# secondsInt = int(In_Seconds)
# print('You are {0:d} Years, {1:d}  Months, {2:d}  Days, {3:d}  Hours, {4:d} \
#  Minutes, {5:d} Seconds old.'.format(yearsInt, monthsInt, daysInt, hoursInt, minutesInt, secondsInt))

from datetime import datetime
from datetime import date
import time
today = date.today()


def user_birthday():
    year = int(input('Please Enter your birth of year: '))
    month = int(input('Please Enter your birth of Month:  '))
    day = int(input('Please Enter your birth of date: '))
    birthday = datetime(year, month, day)
    return birthday


def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday


Birthday = user_birthday()
t = calculate_dates(Birthday)
time_to_birthday = abs(t - today)
days = str(time_to_birthday.days)
hours = str(time_to_birthday.days * 24)
minutes = str(time_to_birthday.days * 24 * 60)
seconds = str(time_to_birthday.days * 24 * 60 * 60)
print("Your Next Birthday comes within : " + days + " days", ",",  hours, "hours", ",", minutes, "minutes", "and", seconds,
      "Seconds")
