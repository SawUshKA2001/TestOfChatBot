import pymysql
sqlconnect = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='test_base',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
