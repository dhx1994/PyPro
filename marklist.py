list1 = [23,76,88,78,59,100,66,98,34,88,99,68]
listl = []
liste = []
listh = []
for i in list1:
    if i < 60:
        listl.append(i)
    elif i == 60:
        liste.append(i)
    else:
        listl.append(i)
print("小于60的成绩{}".format(listl))
print("等于60的成绩{}".format(liste))
print("大于60的成绩{}".format(listh))
