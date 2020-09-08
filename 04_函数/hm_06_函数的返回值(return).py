def sum_2_num(num1, num2):
    """对两个数字求和"""
    result = num1 + num2
    # 可以使用返回值,告诉调用函数一方计算的结果
    return result
# 可以使用变量,来接收函数的执行结果
# 函数外部也可以知道函数的返回结果
sum_result = sum_2_num(10, 20)
print("计算结果为:%d" % sum_result)