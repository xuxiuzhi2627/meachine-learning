# encoding:utf-8
import numpy as np
from sklearn import linear_model

def polyfit(x, y):
    # 实例化一个线性回归的模型
    linear = linear_model.LinearRegression()
    # 拟合线
    linear.fit(x, y)
    # 预测值
    y_hat = linear.predict(x)
    y_mean = np.mean(y)
    SSR = 0
    SST = 0
    for i in range(len(y)):
        SSR += (y_hat[i] - y_mean) ** 2
        SST += (y[i] - y_mean) ** 2

    return SSR/SST


train_x = [1, 3, 8, 7, 9]
train_y = [10, 12, 24, 21, 34]
train_x_2d = [[x] for x in train_x]    #通用的方式,训练集通常是二维的
print(polyfit(train_x_2d, train_y))
