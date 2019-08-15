# 引入pymysql
import pymysql
# 定义查询函数
def query(sql):
    ''' 调用这个方法时，传入一句sql，这个query就返回数据库的结果'''
#数据库连接账号信息    
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
    try:
# 执行sql语句
        cursor1.execute(sql)
# 提交数据即应用
        de.commit()
#关闭数据库连接
        de.close() 
        return True
    except:
        return False 
def ressery(sql):
    ''' 调用这个方法时，传入一句sql，这个query就返回数据库的结果'''
#数据库连接账号信息    
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
    try:
# 执行sql语句
        cursor1.execute(sql)
# 获取返回值
        res = cursor1.fetchall()
#关闭数据库连接
        de.close()   
        return res
    except:
        print('sql语句输入错误')
        return False 
# 主函数
# 插入数据库
a = input('请输入sql语句：')
ed = query(a)
print(ed)

'''
提取数据库表中的元素以字典的形式显示

reskit = []
resdict = {}
for i in res:   #遍历res中的元素，提取出来作为一个元组看待
    reskit.append(i[1])    #添加新元组的元素至目标列表
    resdict[i[1]] = i[6]    #生成新的字典
print(reskit)
print(resdict)'''
# 查询数据库
b = input('请输入sql语句：')
res = ressery(b)
print(res)