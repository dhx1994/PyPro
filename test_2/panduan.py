b={"name":"张三",
"sex":"男",
"age":26,
"high":173}
if b.get("name") == "张三":
    print("张三的年龄是",b["age"])
else:
    print("字典里没有张三！")
    