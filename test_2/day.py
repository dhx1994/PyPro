list1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
list2 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
year = input('请输入年份')
month = input('请输入月份')
data = input('请输入日')

if year%4 == 0:
    for i in range(month):
        j = list2.get(i)
        t = j + t
else:
    for i in range(month): 
        j = list1.get(i)
        t = j + t
print('今天是今年的第{}天'.format(t))