# coding=utf-8

"""项目实战：抓取纳斯达克股票数据"""
import datetime
import hashlib
import json
import logging
import os
import threading
import time
import urllib.request

from com.pkg1.db.db_access import insert_hisq_data

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

url = 'https://api.nasdaq.com/api/quote/AAPL/historical?assetclass=stocks&fromdate=2019-01-01&limit=18&todate=2019-12-20'


def validateUpdate(html):
    """验证数据是否更新，更新返回True，未更新返回False"""
    # 创建md5对象
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code = md5obj.hexdigest()

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):  # 如果文件存在读取文件内容
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        logger.info('数据没有更新')
        return False
    else:
        # 把新的md5码写入到文件中
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        logger.info('数据更新')
        return True


# 线程运行标志
isrunning = True
# 爬虫工作间隔
interval = 5


def controlthread_body():
    """控制线程体函数"""

    global interval, isrunning

    while isrunning:
        # 控制爬虫工作计划
        i = input('输入Bye终止爬虫，输入数字改变爬虫工作间隔，单位秒：')
        logger.info('控制输入{0}'.format(i))
        try:
            interval = int(i)
        except ValueError:
            if i.lower() == 'bye':
                isrunning = False


def istradtime():
    """判断交易时间"""
    # return False

    now = datetime.datetime.now()
    df = '%H%M%S'
    strnow = now.strftime(df)
    starttime = datetime.time(9, 30).strftime(df)
    endtime = datetime.time(15, 30).strftime(df)

    if now.weekday() == 5 \
            or now.weekday() == 6 \
            or (strnow < starttime or strnow > endtime):
        # 非工作时间
        return False
    # 工作时间
    return True


def validate_price(oriPrice):
    if oriPrice.find('$') >= 0:
        oriPrice = oriPrice.replace('$', '')
    return oriPrice


def workthread_body():
    """工作线程体函数"""

    global interval, isrunning

    while isrunning:

        if istradtime():
            # 交易时间内不工作
            logger.info('交易时间，爬虫休眠1小时...')
            time.sleep(60 * 60)
            continue

        logger.info('爬虫开始工作...')

        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:
            data = response.read()
            html = data.decode('gbk')
            print(html)

            py_dict = json.loads(html)

            divstring = html

            if validateUpdate(divstring):  # 数据更新
                # 分析数据
                trlist = py_dict['data']['tradesTable']['rows']

                data = []

                for tr in trlist:

                    rows = tr
                    fields = {}
                    try:
                        df = '%m/%d/%Y'
                        fields['Date'] = datetime.datetime.strptime(rows["date"], df)
                    except ValueError:
                        # 实时数据不分析（只有时间，如10:12）
                        continue
                    fields['Open'] = float(validate_price(rows["open"]))
                    fields['High'] = float(validate_price(rows["high"]))
                    fields['Low'] = float(validate_price(rows["low"]))
                    fields['Close'] = float(validate_price(rows["close"]))
                    fields['Volume'] = int(rows["volume"].replace(',', ''))
                    data.append(fields)

                # 保存数据到数据库
                for row in data:
                    row['Symbol'] = 'AAPL'
                    insert_hisq_data(row)

            # 爬虫休眠
            logger.info('爬虫休眠{0}秒...'.format(interval))
            time.sleep(interval)


def main():
    """主函数"""

    global interval, isrunning
    # 创建工作线程对象workthread
    workthread = threading.Thread(target=workthread_body, name='WorkThread')
    # 启动线程workthread
    workthread.start()

    # 创建控制线程对象controlthread
    controlthread = threading.Thread(target=controlthread_body, name='ControlThread')
    # 启动线程controlthread
    controlthread.start()


if __name__ == '__main__':
    main()
