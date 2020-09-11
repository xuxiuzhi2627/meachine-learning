# encoding:utf-8
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 多项式回归----sklearn版梯度下降法
# 获取数据
data = np.genfromtxt("job.csv", delimiter=",")
# 第一行到最后一行的第一列
x_data = data[1:, 1]
# 第一行到最后一行的第二列
y_data = data[1:, 2]
# print(x_data)
# print(x_data.shape)---(10,)
# print(y_data)

# 增加维度
x_data = x_data[:, np.newaxis]
y_data = y_data[:, np.newaxis]
# print(x_data)
# 创建模型
# model = LinearRegression()
# # 拟合
# model.fit(x_data, y_data)

# 真实值，散点图
# plt.scatter(x_data, y_data)
# 一元线性回归， 预测值---直线
# plt.plot(x_data, model.predict(x_data), c= "r")
# plt.show()


# 定义多项式回归,degree的值可以调节多项式的特征,degree为5表示5次方
ploy_reg = PolynomialFeatures(degree=5)

# 特征处理---5维的
x_ploy = ploy_reg.fit_transform(x_data)
# print(x_ploy)

# 创建模型
model = LinearRegression()
# 拟合
model.fit(x_ploy, y_data)

# 预测
plt.plot(x_data, y_data, "b.")
plt.plot(x_data, model.predict(x_ploy), "r")

# 1-10之间生成50个点
x_test = np.linspace(1, 10, 50)
x_test = x_test[:, np.newaxis]
# print(x_test)
x_ploy1 = ploy_reg.fit_transform(x_test)
plt.plot(x_test, model.predict(x_ploy1), "y")
plt.xlabel("Position level")
plt.ylabel("Salary")

plt.show()



