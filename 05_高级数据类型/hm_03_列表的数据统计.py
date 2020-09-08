name_list = ["张三", "李四", "王五", "王小二", "张三"]

# len(列表名)  统计列表中的元素总数，列表的长度
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

# count统计列表中某一元素出现的次数
count = name_list.count("张三")
print("张三在列表中出现了%d次" % count)

# 会删除列表中第一次出现的数据
# ['李四', '王五', '王小二', '张三']
name_list.remove("张三")
print(name_list)
# 若数据不存在，程序会报错！
name_list.remove("张三123")
print(name_list)