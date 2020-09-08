# encoding:utf-8
# 数据类型 int, float,str,bool
# 查看数据类型
a = "string"
print(type(a))
# 判断是否为某一已知的数据类型
print(isinstance(a, str))
print(isinstance(a, int))
print(isinstance(a, (int,bool,str)))  #是其中一个数据类型