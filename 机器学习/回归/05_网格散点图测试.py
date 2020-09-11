# encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# 网格矩阵测试
# x0, x1 = np.meshgrid([1,2,3],[4,5,6])生成
# (1,4),(2,4),(3,4)
# (1,5),(2,5),(3,5)
# (1,6),(2,6),(3,6)
# 坐标组合起来
x0, x1 = np.meshgrid([1, 2, 3], [4, 5, 6])
plt.scatter(x0, x1)
plt.show()

# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]
# print(x0)

# [[4 4 4]
#  [5 5 5]
#  [6 6 6]]
# print(x1)