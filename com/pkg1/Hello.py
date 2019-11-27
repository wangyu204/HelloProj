# coding=utf-8


import datetime as dt


def read_date(in_date):
    try:
        tmpDate = dt.datetime.strptime(str_date, '%Y-%m-%d')
        return tmpDate
    except ValueError as e:
        print('处理ValueError异常')
        print(e)


# 非法时间 直接调用会报异常
str_date = '2011-13-18'
print('日期 = {0}'.format(read_date(str_date)))
