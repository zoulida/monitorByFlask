__author__ = 'zoulida'
from functools import lru_cache

def getPro():
    import tushare as ts
    pro = ts.pro_api('69d6b836725cd75df21b39873603b14fed58d101bc033b991b51eb41')
    return pro

@lru_cache()
def getCal_dates():#获取交易日历
    pro = getPro()

    cal_dates2 = pro.trade_cal(exchange='')
    #print(cal_dates2)

    return cal_dates2


def is_open_day(date):
    # print(cal_dates[cal_dates['calendarDate'] == date])
    cal_dates = getCal_dates()
    if date in cal_dates['cal_date'].values:
        return cal_dates[cal_dates['cal_date'] == date].iat[0, 2] == 1
    return False

if __name__ == '__main__':
    bl = is_open_day('20200308')
    print(bl)