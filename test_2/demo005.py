import requests
from demo001 import query
url = 'http://118.24.29.59:5000/userRegist/'
headers = {'Content-Type':'application/json'}
data = {"username":"langjin0011","password":"123456", "nickname":"浪晋"}
res = requests.post(url,headers = headers,json = data)

print(res.text)
hdict = res.json()
sql = "select * from tbl_user where username = 'langjin0011';"
res = query(sql)
if hdict['msg'] == '注册成功!':
    if res[0][1] == 'langjin0011':
        print('注册接口测试通过!')
    else:
        print('账号写入数据库失败!')
else:
    print('测试失败！')

