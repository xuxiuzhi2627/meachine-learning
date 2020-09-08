hello_str = "hello world"

# 1.判断是否以指定的字符串开头
# 返回True
# print(hello_str.startswith("h"))

# 2.判断是否以指定的字符串结尾
# print(hello_str.endswith("d"))

# 3.查找指定的字符串
# find()和index()都可以查找指定字符串在大字符串中的索引
# find()如果指定的字符串不存在,会返回-1
# print(hello_str.find("abc"))
# 返回从左数的下标索引-->6
# print(hello_str.rfind("w"))
# index()如果指定的字符串不存在,会报错!
# print(hello_str.index("abc"))

# 4.替换字符串
# replace方法执行完成后,会返回一个新的字符串
# 注意:不会修改原来字符串的内容
print(hello_str.replace("world", "python"))
# hello world
print(hello_str)