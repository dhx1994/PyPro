# 引入pymysql
import pymysql
# 定义查询函数
def query(sql):
    ''' 调用这个方法时，传入一句sql，这个query就返回数据库的结果'''
#数据库连接账号信息    
    dbinfo = {
    "host":"118.24.29.59",
    "user":"vn",
    "password":"1qaz!QAZ123",
    "db":"lux"}

# 连接数据库
    de = pymysql.connect(**dbinfo)
# 获取查询窗口
    cursor1 = de.cursor()
# 执行sql语句
    cursor1.execute(sql)
# 获取返回值
    res = cursor1.fetchall()
#关闭数据库连接
    de.close()   
    return res
# 主函数
# a = input('请输入sql语句：')
# '''"select * from class;"'''
# res = query(a)
# reskit = []
# resdict = {}
# for i in res:   #遍历res中的元素，提取出来作为一个元组看待
#     reskit.append(i[1])    #添加新元组的元素至目标列表
#     resdict[i[1]] = i[6]    #生成新的字典
# print(reskit)
# print(resdict)
