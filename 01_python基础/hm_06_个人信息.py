"""
姓名:小明
年龄:18
性别:是男生
身高:1.75米
体重:75.0公斤
"""
# 在pyhon中,定义变量时不需要制定变量的类型
# 在运行时,python解释器会根据赋值语句等号右侧的数据
# 自动推导出变量中保存的数据类型

name = "小明"   # str表示字符串类型
age = 18       # int表示整型
gender = True  # bool表示布尔类型  True False
height = 1.75  # float类型 小数类型
weight = 75
print(name)
print(type(name))
