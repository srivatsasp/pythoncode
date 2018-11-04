
import datetime
import pytz

tdate_now = datetime.datetime.now(pytz.timezone('US/Mountain'))
tdate_today = datetime.datetime.today()
# tdate_utc = datetime.datetime.utcnow()
# print(tdate_now)
# print(tdate_today)
# print(tdate_utc)

tz = pytz.timezone('US/Central')
tdate_ct = tdate_now.astimezone(tz)
print(tdate_ct)

tdate_et = tdate_now.astimezone(pytz.timezone('Asia/Kolkata'))
print(tdate_et)

print(tdate_now.strftime('%B %d, %Y'))
tdate_frmt = datetime.datetime.strftime(tdate_now, '%B %d, %Y')
print(tdate_frmt)

# for tzs in pytz.all_timezones:
# print tzs
