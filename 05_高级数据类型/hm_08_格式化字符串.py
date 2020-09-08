info_tuple = ("小明", 18, 1.85)

# 格式化字符串后面的()本质上是元组
# print("%s的年龄是%d岁,身高是%.2f米" % ("小明", 18, 1.85))
print("%s的年龄是%d岁,身高是%.2f米" % info_tuple)

info_str = "%s的年龄是%d岁,身高是%.2f米" % info_tuple
# <class 'str'>
print(type(info_str))
print(info_str)

