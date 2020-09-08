name_list = ["zhangsan", "lisi", "wangwu"]
# 1.取值-----列表名[下标]
# print(name_list[2])

# list index out of range---列表索引超出范围
# print(name_list[3])


# 2. 取索引 --列表名.index(元素名)
# 知道数据的内容,想确定数据在列表中的位置
# print(name_list.index("wangwu"))

# 'wangwu123' is not in list
# 使用index方法需要注意,如果传递的数据不在列表中,程序会报错!
# print(name_list.index("wangwu123"))


# 3.修改
# 直接重新赋值
# name_list[2] = "王五"

# list assignment index out of range
# 列表指定的索引超出范围,程序会报错!
# name_list[3] = "王小二"
# print(name_list)


# 4. 增加
# append方法向列表的末尾追加元素
# name_list.append("小徐")

# insert方法可以在列表的指定索引位置插入元素
# name_list.insert(1, "小兵")

# extend方法将指定列表中的元素拆分成单个元素追加到列表后面
# ['zhangsan', 'lisi', 'wangwu', '孙悟空', '猪八戒', '沙和尚']
# temp_list = ["孙悟空","猪八戒","沙和尚"]
# name_list.extend(temp_list)


# 5.删除数据
# 1. 列表名.remove(元素), 删除列表中第一次出现的指定元素
# name_list.remove("wangwu")
# 2. 列表名.pop(索引),
# 默认删除列表中最后一个元素
# name_list.pop()
# 删除指定位置的元素
# name_list.pop(1)
# 3. clear-->[]  清空列表
# name_list.clear()

print(name_list)