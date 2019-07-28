# 引入pymysql
import pymysql
# 定义查询函数
def query(sql):
    ''' 调用这个方法时，传入一句sql，这个query就返回数据库的结果'''
    dbinfo = {
        "host":"127.0.0.1",
        "user":"root",
        "password":"123456",
        "db":"test_duhengixin"
    }
# 连接数据库
    de = pymysql.connect(**dbinfo)
# 获取查询窗口
    cursor1 = de.cursor()
# 执行sql语句
    cursor1.execute(sql)
# 获取返回值
    res = cursor1.fetchall()
    de.close()   
    return res
# 主函数
a = input('请输入sql语句：')
'''"select * from class;"'''
res = query(a)
reskit = []
resdict = {}
for i in res:
    reskit.append(i[1])
    resdict[i[1]] = i[6]
print(reskit)
print(resdict)
