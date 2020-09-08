# 传递两个参数


def sum_2_num(num1, num2):
    """对两个数求和
    :param num1:
    :param num2:
    :return: result
    """
    result = num1 + num2
    # 只有函数内部知道函数的返回结果
    print("%d + %d = %d" % (num1, num2, result))

sum_2_num(1, 20)