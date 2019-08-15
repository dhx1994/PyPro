# 1.引入第三方包
# 2.读取Excel数据
# 3.赋值
# 4.构造请求
# 5.断言
# 6.查询数据库

# 1.引入第三方包
import requests
import pymysql
from utils.dbtools import queey
from utils.exceltools import read_excel
# 2.读取Excel数据
testcases = []
testcases = read_excel('H:/Python/PyPro/REQUESTSTEST/testcases/接口测试用例模板.xlsx','Sheet1')
print(testcases)

for testcase in testcases:
# 3.赋值
    test_url = testcase[1]
    test_name = testcase[3]
    test_method = testcase[5]
    test_data = eval(testcase[7])
    # print(testcase[8])
    response_state = int(testcase[8])
    test_code = int(testcase[9])
    sql = testcase[10]
    try:
# 4.构造请求
        res = requests.request(test_method,url = test_url,json=test_data)
        print(res.status_code)
# 5.断言
        assert res.status_code == response_state
        print(res.json().get('code'))
        assert int(res.json().get('code')) == test_code
# 6.查询数据库
        a = queey(sql)
        #  print(a)
        if res.json().get('code') == 200:
            assert len(a) != 0
        else:
            assert len(a) == 0
        print('【{}】执行成功'.format(test_name))
    except:
        print('【{}】执行失败'.format(test_name))
