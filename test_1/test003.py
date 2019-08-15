import pymysql
 # 连接数据库
def queey(sql):
     dbinfo = {
         'host':'127.0.0.1',
         'user':'root',
         'password':'123456',
         'db':'test_duhengixin'
     }
     db = pymysql.connect(**dbinfo)
     curcor = db.cursor()
     curcor.execute(sql)
     res = curcor.fetchall()
     db.close()
     return res
sql = input('请输入sql语句')
res = queey(sql)
print(res)