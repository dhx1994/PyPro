""""jine = input("请输入金额：")  # 获取输入金额，赋值给jine这个变量
print("输入的金额为：",jine)   # 打印jine

num = jine.count(".")  #  统计jine这个字符串中，有多少个小数点
if num == 0 or num == 1:  # 判断小数的个数，只有小数点为0或者为1个的情况，才认为是正常的数字
    hstr = "0123456789."
    for i in jine:    # 便利jine 给i
        if i not in hstr:  # 判断jine这个字符串中，是否存在非数字和小数点的值
            print("输入的值不合法，请输入数字！")
            exit()
    jine = float(jine)  # 强制转换数据类型为float
    if jine >= 0.01 and jine <= 200:
        print("发送红包成功！")
    else:
        print("金额超出范围！")
else:
    print("输入的金额不合法，只能输入数字！")"""
while True:
    try:
        x = float(input('Please input a number: '))
        break
    except TypeError:
        print('Oops! invalid number.Try again...')

if x >= 0.01 and x <= 200:
            print("success!")
else:
            print('please try again')


