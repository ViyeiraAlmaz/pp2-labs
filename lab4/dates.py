#Ex 1

from datetime import datetime, timedelta

currentDate = datetime.now()
fiveDaysAgo = currentDate - timedelta(days=5)

print('Current date: ', currentDate.strftime("%Y - %m - %d"), "\n")
print("Five days ago: ", fiveDaysAgo.strftime('%Y - %m - %d'))


#Ex 2

from datetime import datetime, timedelta

currentDate = datetime.now()
yesterday = currentDate - timedelta(days=1)
tomorrow = currentDate + timedelta(days=1)

print("Yesterday: ", yesterday.strftime("%A"))
print("Today: ", currentDate.strftime("%A"))
print("Tomorrow: ", tomorrow.strftime("%A"))

#Ex 3

from datetime import datetime, timedelta

currentDate = datetime.now()
t = currentDate.replace(microsecond=0)

print(t)

#Ex 4

from datetime import datetime, timedelta

currentDate = datetime.now()
birthDate = datetime(2005, 11, 29, 0, 0)

difference = currentDate - birthDate

differenceInSeconds = difference.total_seconds()

print("Difference between the date of my birth and today in seconds: ",differenceInSeconds)