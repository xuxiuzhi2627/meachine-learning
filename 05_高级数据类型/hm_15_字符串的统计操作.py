hello_str = "hello hello"

# 1.统计字符串的长度
# print(len(hello_str))

# 2.统计小(子)字符串出现的次数
# print(hello_str.count("llo"))
# 若子字符串不存在,不会报错,统计次数为0
# print(hello_str.count("abc"))
# 从开始位置到结束位置,子字符串出现的次数
# print(hello_str.count("llo", 2, 6))

# 3.某一子字符串出现的位置
# 若子字符串不存在,会报错
# print(hello_str.index("BC"))
# 若子字符串不存在,会返回-1
print(hello_str.find("llp"))
# 从开始位置到结束位置,子字符串首次出现的位置
print(hello_str.index("llo", 1, 6))
# 若子字符串不存在,程序报错!
# print(hello_str.index("abc"))