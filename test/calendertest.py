__author__ = 'zoulida'


import calendar
mmm = calendar.monthcalendar(2020,8)
print(mmm)
n = '2'
s = n.zfill(2)
print(s)

from datetime import datetime

thisyear = datetime.now().year
print(thisyear)