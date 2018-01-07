# -*- coding: utf-8 -*-


import redis
import MySQLdb
import json

def main():
    #创建redis数据库链接
    rediscli = redis.Redis(host = '127.0.0.1', port = 6379, db = 0)

    # 创建mysql数据库链接
    mysqlcli = MySQLdb.connect(host = '127.0.0.1', user = 'root', passwd='密码', db = 'tencentjob', port=3306, use_unicode=True)

    offset = 0

    while True:
        # 将数据从redis里pop出来
        source, data = rediscli.blpop(["tt:items"])
        item = json.loads(data)
        try:
            # 创建mysql操作游标对象，可以执行mysql语句
            cursor = mysqlcli.cursor()

            cursor.execute('insert into tencentjob (position_name, position_link, position_type, position_num,work_location, publish_time) values (%s, %s, %s, %s, %s, %s)' % [item["position_name"], item["position_link"], item["position_type"], item["position_num"],item["work_location"], item["publish_time"]])
            #提交事务
            mysqlcli.commit()
            #关闭游标
            cursor.close()
            offset += 1
            print offset
        except:
            pass

if __name__ == '__main__':
    main()