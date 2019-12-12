# coding=utf-8

import pymysql

# 1. 建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='wy123456',
                             database='MyDB',
                             charset='utf8')

try:
    # 2. 创建游标对象
    with connection.cursor() as cursor:

        # 3. 执行SQL操作
        # 3.1 通过元组绑定
        # sql = 'select name,userid from user where userid > %s'
        # cursor.execute(sql, [0])

        # 3.2 通过字典绑定
        sql = 'select max(userid) from user'
        cursor.execute(sql)

        # 4. 提取结果集
        row = cursor.fetchone()

        if row is not None:
            print('最大用户id:{0}'.format(row[0]))

        # cursor.close()

    # with代码块结束 5. 关闭游标

finally:
    # 6. 关闭数据连接
    connection.close()
