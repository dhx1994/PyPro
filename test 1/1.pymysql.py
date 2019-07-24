# 引入pymysql
import pymysql
# 定义查询函数
def query(sql):
    dbinfo = {
        "host":"127.0.0.1",
        "user":"root",
        "password":"123456",
        "db":"test_duhengixin"
    }
# 连接数据库
    db = pymysql.connect(**dbinfo)
# 获取查询窗口
    cursor = db.cursor()
# 执行sql语句
    cursor.execute(sql)
# 获取返回值
    res = cursor.fetchall()   
    return res

a ="select * from class;"
res = query(a)
print(res)
