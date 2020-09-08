# 1. 输入苹果的单价
price_str = input("请输入苹果的单价:")
# 1. 将价格转换成小数
# price = float(price_str)
# 2. 输入苹果的重量
weight_str = input("请输入苹果的重量:")
# 2. 将重量转换成小数
# weight = float(weight_str)
# 3. 计算支付的总金额
# 注意:两个字符串不能进行相乘
# money = price * weight
# print(money)

# 多个变量记录一个值,占用空间多

# 或者直接进行转换后相乘
money = float(price_str) * float(weight_str)
print(money)
# <class 'float'>
print(type(money))