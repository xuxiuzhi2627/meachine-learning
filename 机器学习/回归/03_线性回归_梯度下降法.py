# encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# genfromtxt创建数组表格数据, delimiter--定界符(逗号分隔符)
data = np.genfromtxt("data.csv", delimiter=",")
# print(data)
x_data = data[:, 0]  #取到所有的行,取第0列
y_data = data[:, 1]
# 画散点图
# plt.scatter(x_data, y_data)
#显示图像
# plt.show()

# 学习率
lr = 0.0001
# 截距
b = 0
# 斜率
k = 0
# 最大迭代次数
epochs = 50

# 最小二乘法
def compute_error(b, k, x_data, y_data):
    totalError = 0
    # 样本的个数
    m = float(len(x_data))
    for i in range(0, len(x_data)):
        y_hat = k * x_data[i] + b
        totalError += (y_hat - y_data[i])**2
    return totalError / m / 2.0


# 梯度下降法
def gradient_descent_runner(lr, b, k, x_data, y_data, epochs):
    # 统计数据的长度
    m = float(len(x_data))
    for j in range(epochs):
        b_grad = 0
        k_grad = 0
        # 计算梯度的总和再求平均
        for i in range(0, len(x_data)):
            y_hat = k * x_data[i] + b
            b_grad += 1/m * (y_hat - y_data[i])
            k_grad += 1/m * (y_hat - y_data[i]) * x_data[i]
       # 更新b和k
        b = b - lr * b_grad
        k = k - lr * k_grad
        # 每迭代5次,输出一次图像
        if j % 5 == 0:
            print("epochs为%s次" % j)
            # 原始值----蓝点
            plt.plot(x_data, y_data, "b.")
            # 回归图---红线
            plt.plot(x_data, k * x_data + b, "r")
            plt.show()

    return b, k

print("Staring b = {0}, k = {1}, totalError = {2}".format(b, k, compute_error(b, k, x_data, y_data)))
print("Running......")
b, k = gradient_descent_runner(lr, b, k, x_data, y_data, epochs)
print("After {0} iterations,b = {1},k ={2},error = {3}".format(epochs, b, k, compute_error(b, k, x_data, y_data)))

# 画图
# 原始的标注点
# plt.figure(figsize=(10, 8),dpi=80)
# plt.plot(x_data, y_data, "b.")
# # 最终的红色的线条
# plt.plot(x_data, k * x_data + b, "r")
plt.show()

