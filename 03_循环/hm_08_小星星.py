# 控制台输出五行*,每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****
# 定义一个计数器变量
row = 1
# 开始循环
while row <= 5:
    print("*" * row)
    # 注意：计数器变化
    row += 1