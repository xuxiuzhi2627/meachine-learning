# 计算0-100之间所有数字的累计求和结果
# 0.定义一个变量，记录最终结果
result = 0
# 1.定义一个整数变量,记录循环次数
i = 0
# 2.开始循环
while i <= 100:
    # print(i)
    # 2.每一次循环，都让result这个变量和i计数器进行相加
    result += i
    # print(result)
    # 3.处理计数器
    i += 1
print("1~100的累加和是：%d" % result)