name_list = ["张三", "李四", "王五"]

# del 关键字(delete)删除列表中的元素
del name_list[1]

# del本质上是用来将一个变量从内存中删除的
name = "小明"
del name

# 注意:如果使用del关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了,
# 报错!
print(name)

print(name_list)