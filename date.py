import datetime
import pytz


now = datetime.datetime.today()

print(now)

for tz in pytz.all_timezones:
    print(tz)


print(len(pytz.all_timezones))

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_nigeria = datetime_today.astimezone(pytz.timezone("Africa/Lagos"))


print(datetime_nigeria.strftime("%B %d, %Y"))


print(repr(datetime.datetime.strptime("August 06, 2020", "%B %d, %Y")))





