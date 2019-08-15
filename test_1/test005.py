# class Car():
#     color = 'white'
#     wheel = 4
#     price  = 688888
#     xishu = 0.8
#     def __init__(self,c,w,p,x):
#         self.color = c
#         self.wheel = w
#         self.price = p
#         self.xishu = x
#     def run(self):
#         print('宝马可以跑')
#     def comfort(self):
#         print('宝马的舒适系数为{}'.format(self.xishu))
# p = Car()
# print(p.color)
# p.comfort()
# ========================================
class Bird():
    wing = 2
    eye = 2
    month = 2
    high = '200m'
    def fly(self):
        print('鸟有{}眼睛，{}张嘴，{}只翅膀，可以飞到{}'.format(self.eye,self.month,self.wing,self.high))
    def __init__(self,w,e,m,f):
        self.wing = w
        self.eye = e
        self.month = m
        self.high = f
        self.fly()
f = Bird(4,3,3,"20000m")
