__author__ = 'zoulida'

import tools.tusharePro as tp
import tushare as ts
import traceback
import datetime
import DBO.mongodbO as mongodbO
mycol = mongodbO.getCollection()

from tools.LogTools import Logger
nowTime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logName = 'log-' + nowTime + '.txt'
logger = Logger(logName, logLevel="DEBUG", logger="monitor.py").getlog()




def is_open_day(date):
    #print(cal_dates[cal_dates['calendarDate'] == date])
    #if date in cal_dates['calendarDate'].values:
    #    return cal_dates[cal_dates['calendarDate'] == date].iat[0, 1] == 1
    strr = date.replace("-","")
    bl = tp.is_open_day(strr)
    return bl

def insert(dayStr, datafromStr):
    isopen = True
    if not is_open_day(dayStr):
        isopen = False

    mydict = {"date": "%s" % dayStr, "%s"%datafromStr: False, "isopen": isopen}
    x = mycol.insert_one(mydict)
    print(x)

def update(dayStr, datafromStr):
    myquery = {"date": '%s'%dayStr}
    newvalues = {"$set": {"%s"%datafromStr : True}}

    mycol.update_one(myquery, newvalues)

class MonitorSantai():
    def fetchSantaiStat(self):
        myquery = {"date": {"$gt": "2020-03-01"}}

        mydoc = mycol.find(myquery)
        #listdata =list(mydoc)
        #print( listdata)#pymongo.cursor.Cursor变数组
        dictHaveGet = {}
        dictIsOpenday = {}
        for x in mydoc:
            print(x)
            dictHaveGet[x['date']] = x['santai']
            dictIsOpenday[x['date']] = x['isopen']
        print(dictHaveGet)
        print(dictIsOpenday)

        return dictHaveGet, dictIsOpenday

    # 获取从起始日期到截止日期中间的的所有日期，前后都是封闭区间
    def get_date_list(self, begin_date, end_date):
        date_list = []
        while begin_date <= end_date:
            # date_str = str(begin_date)
            date_list.append(begin_date)
            begin_date += datetime.timedelta(days=1)
        return date_list

    def manageSantaiStatDays(self):
        today = datetime.date.today()
        yestoday = today + datetime.timedelta(days=-1)
        z30daysago = yestoday + datetime.timedelta(days=-7)  # 更改为两月了
        # dates = get_date_list(datetime.date(2018, 6, 30), datetime.date(2018, 7, 16))
        dates = self.get_date_list(z30daysago, yestoday)
        for date in dates:
            str_date = str(date)
            print('manageSantaiStatDays ', str_date)
            self.manageSantaiStatOneDay(str_date)




    def manageSantaiStatOneDay(self, dayStr = '2019-06-03'):
        #todaystr = '2020-03-13'

        myquery = {"date": "%s"%dayStr}
        x = mycol.find_one(myquery)
        #print(x['state'])

        if x is not None and x['santai'] == True:
            return

        if x is None:#如果空，先插入。这样就肯定是Flase了
            insert(dayStr, 'santai')

        if self.getStatSantaiOneDay(dayStr) == True:
            print('update')
            update(dayStr, 'santai')
        #print(x)



    def getStatSantaiOneDay(self, strday):
        stocklist = self.getHS300()
        #print(stocklist)

        i = 0
        for row in stocklist.itertuples(index=True, name='Pandas'):#防止停牌，要测试10个
            if i > 2:
                break
            code = getattr(row, "code")
            print('test ',code)
            if self.findoneSanti(strday, code):
                return True
            i = i + 1
        return False

    def getHS300(self):
        stock_info = ts.get_hs300s()
        return stock_info

    def findoneSanti(self, strday, symbol):
        from tools import connectMySQL
        cursor, db = connectMySQL.getTickCursorAndDB()  # getTickCursor()
        try:
            sqlSentence = "select * from tick_%s" % symbol + " where 日期 = '%s'" %strday
            #print(sqlSentence)
            logger.debug(sqlSentence)
            cursor.execute(sqlSentence)
            results = cursor.fetchone()
            if results is not None:
                #print(results)
                return True
        except Exception as e:
            print('traceback.print_exc():', traceback.print_exc())
            # 如果以上插入过程出错，跳过这条数据记录，继续往下进行
            #continue  # break
        finally:
            # 关闭游标，提交，关闭数据库连接
            cursor.close()
            db.commit()
            db.close()
        return False

if __name__ == '__main__':
    m = MonitorSantai()
    #m.findoneSanti( '2019-06-03', '000036')
    #bl = m.getStatSantaiOneDay('2019-06-03')
    #print(bl)
    m.manageSantaiStatDays()