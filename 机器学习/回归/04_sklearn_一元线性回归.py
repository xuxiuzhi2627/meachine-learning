# encoding:utf-8

# sklearn数据处理到模型训练,机器学习库，线性回归，构建模型
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 载入数据--数组文件(逗号分隔符)
data = np.genfromtxt("data.csv",delimiter=",")
x_data = data[:, 0]
y_data = data[:, 1]

# 散点图
# plt.figure(figsize=(10, 8), dpi=80)
# plt.scatter(x_data, y_data)
# print(x_data.shape) #---->(100,)
# plt.show()


# sklearn中需要再添加一个维度(100,1)
x_data = data[:, 0, np.newaxis]
y_data = data[:, 1, np.newaxis]

# 创建模型，拟合模型
model = LinearRegression()
model.fit(x_data, y_data)
# 真实值
plt.plot(x_data, y_data, "b.")
# model.predict(x_data)---预测
plt.plot(x_data, model.predict(x_data), "r")
plt.show()




