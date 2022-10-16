
import time
from datetime import datetime   
# from zoneinfo import ZoneInfo

# def datetotimestamp(date):
#     time_tuple = date.timetuple()
#     timestamp = round(time.mktime(time_tuple))
#     return timestamp
# def datetotimestamp(date):     
#     date_time = datetime.datetime(year, month, day, 12, 0, 50)
#     return time.mktime(date_time.timetuple())

# def timestamptodate(timestamp):
#     return datetime.fromtimestamp(timestamp)
# end = datetotimestamp(datetime.today())
# # print(stra)
# # date_time = datetime.datetime(2022, 6, 3, 12, 0, 50)
# # print("Given Date:",date_time)
# # print("UNIX timestamp:",
# # (time.mktime(date_time.timetuple())))

# start_1_min = datetotimestamp(year=2022,month= 6,day= 3)
# print(start_1_min)

# print( datetime.utcfromtimestamp(datetime.today()).strftime('%H'))

# stra = datetime.utcfromtimestamp(end).strftime('%H:%M:%S')
# print(datetime.utcfromtimestamp(end).strftime('%H:%M'))
# print(datetime.datetime.strptime(given_date,"%m/%d/%Y, %H:%M:%S"))


def datetotimestamp(date):
    time_tuple = date.timetuple()
    timestamp = round(time.mktime(time_tuple))
    return timestamp

def timestamptodate(timestamp):
    return datetime.fromtimestamp(timestamp)


timestamp = datetime.now().strftime('%H:%M:%S')
year = datetime.now().strftime('%Y')
month =  datetime.now().strftime('%m')
day = datetime.now().strftime('%d')
hour = datetime.now().strftime('%H')
minute = datetime.now().strftime('%M')
second = datetime.now().strftime('%S')
print(datetime(int(year), int(month),int(day),int(hour),int(minute),int(second)))

start_1_min = datetotimestamp(datetime(int(year), int(month),int(day),int(hour),int(minute),int(second)))
print(start_1_min)
# dtobj = datetime.now(tz=ZoneInfo('Asia/Kolkata'))