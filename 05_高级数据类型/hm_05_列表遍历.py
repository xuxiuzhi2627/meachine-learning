name_list = ["张三","李四", "王五", "王小二"]

"""
顺序的从列表中依次获取数据，每次循环过程中，数据会保存在name
这个变量中，在循环体内部可以访问到当前这一次获取到的数据
for name in 列表变量:
    print("我的名字叫%s" % name)"""

for name in name_list:
    print("我的名字叫%s" % name)