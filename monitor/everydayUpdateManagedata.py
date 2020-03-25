#coding=utf-8


import datetime
#import schedule #pip install schedule
import threading
import time

#前置必备代码
import sys
import os
print( "当前工作路径",os.getcwd())
sys.path.append(os.getcwd())
#sys.path.append('/volume/pythonworkspace/santai3')

from tools.LogTools import Logger
logger = Logger(logName='everydayManageTDXdata.out', logLevel="DEBUG", logger="everydayManageTDXdata").getlog()


logger.debug(sys.path)



def job1():
    print("I'm working for quantaxis.config.update_x.update_task()")
    time.sleep(2)
    print("job1:", datetime.datetime.now())
    #import tools.LogCut as lc
    #lg = lc.Logger(logName='santailog.out', logLevel="DEBUG", logger="santai3").getlog()

    import monitor.monitor.Monitor as Monitor
    mObj = Monitor()
    mObj.manageAll()





def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())
    #import data163ToMySQL.Tick.downTickCVS7 as tk
    #tk.main()

def job3():
    print("I'm working for job3")
    time.sleep(2)
    print("job3:", datetime.datetime.now())
    #import data163ToMySQL.getIndexDaily as gi
    #gi.download_indexSets()

def job4():
    print("I'm working for job4:涨跌停数据收集")
    time.sleep(2)
    print("job4:", datetime.datetime.now())
    #import data163ToMySQL.wenduj3 as wenduj3
    #obj = wenduj3.GetZDT()
    #obj.zdtStock5Days()

def job1_task():
    threading.Thread(target=job1).start()


def job2_task():
    threading.Thread(target=job2).start()

def job3_task():
    threading.Thread(target=job3).start()

def job4_task():
    threading.Thread(target=job4).start()

def run():

    #schedule.every(10).seconds.do(job1_task)
    #schedule.every(10).seconds.do(job2_task)


    while True:
        #schedule.run_pending()
        #time.sleep(1)
        #job2_task()
        while True:
            # 不到时间就等20秒之后再次检测
            time.sleep(5)
            now = datetime.datetime.now()

            # 到达设定时间，结束内循环
            h = 7
            m = 8
            # s = 10
            # if now.second <= s:
            #     break
            if now.hour == h and now.minute == m:

                break

            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            strDebug = 'Wait for running at %s:%s every day. Now time is %s' %(h, m, nowTime)
            logger.debug(strDebug)

        job1_task()
        time.sleep(60)
        # job2_task()
        # time.sleep(7000)
        # job1_task()
        # time.sleep(60)
        # job3_task()
        # time.sleep(60)
        # job4_task()
        # time.sleep(60)
if __name__ == '__main__':
    run()
    #job1()
