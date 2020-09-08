# encoding:utf-8
import  numpy as np
import math

def computeCorrelation(x:list, y:list):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    Cov = 0   #协方差
    Var = 0   #方差
    var_x = 0
    var_y = 0
    for xi, yi in zip(x,y):
        diff_x = xi - x_mean
        diff_y = yi - y_mean
        Cov += diff_x * diff_y
        var_x += diff_x **2
        var_y += diff_y ** 2
        Var = math.sqrt(var_x * var_y)

    return Cov/Var

# 测试相关系数
train_x = [1, 3, 8, 7, 9]
train_y = [10, 12, 24, 21, 34]
print(computeCorrelation(train_x, train_y))   # 0.94031007654487

