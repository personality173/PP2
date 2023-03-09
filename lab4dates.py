import datetime
#1-exercise
date_next = datetime.date.today() + datetime.timedelta(days=5)
print(date_next)
#2-exercise
date_yesterday = datetime.date.today() - datetime.timedelta(days=1)
date_tommorow = datetime.date.today() + datetime.timedelta(days=1)
print("Yesterday:", date_yesterday)
print("Today:", datetime.date.today())
print("Tommorow:", date_tommorow)
#3-exercise
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)
#4-exercise
dt1 = input()
dt2 = input()
dit1 = datetime.datetime.strptime(dt1, '%m %d %Y %H %M %S')
dit2 = datetime.datetime.strptime(dt2, '%m %d %Y %H %M %S')
print((dit2 - dit1).total_seconds())