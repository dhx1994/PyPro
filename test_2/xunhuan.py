list1 = ["张三","李四","王二麻子"]

for i in list1:
    print(list1)

b={"name":"张三",
"sex":"男",
"age":26,
"high":173} 

for i in b:
    print(i)

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,"\t",end="")
    print("")
hlist = [8,56,23,87,72,88,99,19,44,99]
lowlist = []
highlist = []
for i in hlist:
    if i > 60:
        highlist.append(i)
    else:
        lowlist.append(i)
print(hlist)
print(lowlist)
print(highlist)


