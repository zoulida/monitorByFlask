# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/2 20:59
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : index.py

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import calendar
from datetime import datetime
from monitor.monitor import Monitor

calendar.setfirstweekday(firstweekday=6)
app = Flask(__name__)

week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


def monthToNumstr(shortMonth):
    dictmoon = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }
    return dictmoon[shortMonth]

def calc_calender(date):
    year = date.year
    yearInfo = dict()
    for month in range(1, 13):
        days = calendar.monthcalendar(year, month)
        if len(days) != 6:
            days.append([0 for _ in range(7)])
        #month_addr = calendar.month_abbr[month]
        #month_str = monthToNumstr(month_addr)
        n = str(month)
        month_str = n.zfill(2)
        yearInfo[month_str] = days
    return yearInfo


@app.route('/', methods=["GET", "POST"])
def index():
    updateState = False
    if request.method == "GET":
        date = datetime.today()
        #this_month = calendar.month_abbr[date.month]
        monitor = Monitor()
        dictHaveGetSantai, dictHaveGetTDX, dictIsOpenday, dictHaveGetWenduji = monitor.fetchStat()
        #dictHaveGet = {'2020-03-06': True, '2020-03-07': False, '2020-03-08': True, '2020-03-09': False, '2020-03-10': False,
        # '2020-03-11': True, '2020-03-12': True, '2020-03-13': False}
        #print(dictHaveGet)
        #print(calc_calender(date))
        context = {'this_month': str(date.month).zfill(2), 'date': date, 'content': calc_calender(date),\
                   'dictHaveGetSantai': dictHaveGetSantai, 'dictHaveGetTDX': dictHaveGetTDX, 'dictIsOpenday': dictIsOpenday, \
                   'dictHaveGetWenduji':dictHaveGetWenduji}
        return render_template('index2.html', **context)
        #return render_template('index2.html', this_month=this_month, date=date, content=calc_calender(date), updateState = updateState, listJson = listdata )


@app.route('/sendDate', methods=['GET', 'POST'])
def form_data():
    # 从request中获取表单请求的参数信息
    title = request.form['title']
    datetime = request.form['datetime']
    quiz = request.form['quiz']

    # 此处逻辑代码已经省略...................

    return jsonify({'status': '0', 'errmsg': '登录成功！'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
