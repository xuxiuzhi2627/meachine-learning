# 计算0～100之间所有偶数的累加和的结果
# 开发步骤：
# 1.编写循环 确认 要计算的数字
# 2.添加 结果 变量，在循环体内部，处理计算结果
result = 0
i = 0
while i <= 100:
    # 1.判断偶数 i % 2 == 0:
    # 判断奇数 i % 2 != 0:
    if i % 2 == 0:
        # print(i)
        # 2.当i是偶数时，才进行累加
        result += i
    # 3.计数器累加,和while是配套使用的
    i += 1
print("0～100之间的偶数和为:%d" % result) #--->2550
# print("0～100之间的奇数和为:%d" % result)--->2500
