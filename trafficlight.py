'''import time
i = 1
while i :
    print('红灯')
    time.sleep(5)   
    print('绿灯')
    time.sleep(5)
    print('黄灯')
    time.sleep(5)'''
from time import sleep

light = {
    '红灯':30,
    '绿灯':30,
    '黄灯':3
}
while True:              #死循环
    for i in light:
        t = light.get(i)
        while t != 0:
            print('{}倒计时{}秒'.format(i,t))
            sleep(1)
            t = t - 1