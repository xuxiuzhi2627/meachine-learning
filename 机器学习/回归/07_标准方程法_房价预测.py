# encoding:utf-8
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 载入数据
data = np.genfromtxt("data.csv", delimiter=",")
x_data = data[:, 0, np.newaxis]
y_data = data[:, 1, np.newaxis]

# <class 'numpy.ndarray'>
# print(type(x_data))

# 散点图
plt.scatter(x_data, y_data)
# plt.show()

# 将array转化为矩阵形式
# print(np.mat(x_data).shape)
# <class 'numpy.matrix'>
# print(type(np.mat(x_data)))
# print(np.mat(y_data).shape)

# 给样本添加偏置项
# np.ones(100,1)形状为(100,1)全为1的矩阵，作为x0, 与theta0相乘
# 与第一列的元素在行上拼接
X_data = np.concatenate((np.ones((100, 1)), x_data), axis=1)
# print(X_data)

# 标准方程法求解回归参数
# xArr,yArr表示X矩阵(x0,x1...)和Y矩阵(标签y),数组形式
def weights(xArr, yArr):
    # 转换为矩阵形式
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)
    # xTx表示x的转置乘以x
    xTx = xMat.T * xMat
    # 判断是否可逆
    if np.linalg.det(xTx)== 0.0:
        print("This matrix cannot do inverse")
        return
    # xTx.I为xTx的逆矩阵
    ws = xTx.I * xMat.T * yMat
    return ws

ws = weights(X_data, y_data)
print(ws)
print(ws[0])
print(ws[1])

# 画图
# 确定一个点(x0,x1)
x_test = np.array([[20],[80]])
# print(x_test.shape)----(2, 1)
#  ws[0]，ws[1]分别为第0行，第1行
# y = theta0 + x * theta1
y_test = ws[0] + x_test * ws[1]
plt.plot(x_test, y_test, "r")
plt.show()
