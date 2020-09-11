# encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

# 多元线性回归----sklearn版梯度下降法
# 数组格式
data = np.genfromtxt("Delivery.csv", delimiter=",")
# 取数据---特征值(除最后一列)
x_data = data[:, 0:-1]
# 取数据---标签
y_data = data[:, -1]
# print(x_data)
# print(y_data)

# 创建模型
model = LinearRegression()
# 拟合
model.fit(x_data, y_data)
# 系数
print("Coefficients:", model.coef_)
# 截距
print("intercept:", model.intercept_)

# 预测值
# predict = model.predict(x_data)
# print(predict)

# 测试
# x_test = [[100, 4]]
# predict = model.predict(x_test)
# print("predict:",predict)

# 1*1的子图
ax = plt.figure().add_subplot(111, projection="3d")
# 画点
ax.scatter(x_data[:, 0], x_data[:, 1], y_data, c="r", marker="o", s=50)
# 第一个特征
x0 = x_data[:, 0]
# 第二个特征
x1 = x_data[:, 1]
# 网格矩阵
x0, x1 = np.meshgrid(x0, x1)
# 预测---系数里对应
z = model.coef_[0] * x0 + model.coef_[1] * x1 + model.intercept_
# 画3d图
ax.plot_surface(x0, x1, z)

# 次数
ax.set_xlabel("Times")
# 运送里程
ax.set_ylabel("Number of deliveries")
# 运送时间
ax.set_zlabel("Time")

plt.show()




