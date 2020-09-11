# encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# 多元线性回归----定义梯度下降法
# 获取数据
data = np.genfromtxt("Delivery.csv", delimiter=",")

# x_data取所有行,取第一列到倒数第二列的特征值
x_data = data[:, 0:-1]
# y_data取最后一列的标签
y_data = data[:, -1]
# print(x_data)
# print(y_data)

lr = 0.0001
theta0 = 0
theta1 = 0
theta2 = 0
epochs = 1000

def computeError(theta0,theta1,theta2, x_data, y_data):
    totalError = 0
    # 遍历每行，预测值-真实值
    m = float(len(y_data))
    for i in range(0, len(x_data)):
        # 预测值
        y_hat = theta0 + theta1 * x_data[i, 0] + theta2 * x_data[i, 1]
        # 损失值
        totalError += (y_hat - y_data[i])**2

    return totalError / m * 2

def gradient_descent_runner(lr, theta0, theta1, theta2, x_data, y_data):
    m = float(len(x_data))
    theta0_grad = 0
    theta1_grad = 0
    theta2_grad = 0
    # 循环epochs次
    for i in range(epochs):
        for j in range(0, len(x_data)):
            # 预测值
            y_hat = theta0 + theta1 * x_data[j, 0] + theta2 * x_data[j, 1]
            # 总损失对theta0的求导结果
            theta0_grad += 1 / m * (y_hat-y_data[j])
            # 第一个特征
            theta1_grad += 1/len(x_data) * (y_hat-y_data[j])* x_data[j, 0]
            # 第二个特征
            theta2_grad += 1/len(x_data) * (y_hat-y_data[j])* x_data[j, 1]
        # 更新theta0, theta1, theta2
        theta0 = theta0 - lr * theta0_grad
        theta1 = theta1 - lr * theta1_grad
        theta2 = theta2 - lr * theta2_grad

    return theta0, theta1, theta2

print("初始的theta0为{0},theta1为{1},theta2为{2}, totalError为{3}".format(theta0,theta1,theta2,computeError(theta0, theta1, theta2, x_data, y_data)))
print("Running......")
theta0, theta1, theta2 = gradient_descent_runner(lr, theta0, theta1, theta2, x_data, y_data)
print("在迭代{0}次后，theta0为{1},theta1为{2},theta2为{3},总损失totalError为{4}".format(epochs, theta0, theta1, theta2, (computeError(theta0, theta1,theta2, x_data, y_data))))

# fig.add_subplot(111)就是构成 1x1的3D子图
ax = plt.figure().add_subplot(111, projection="3d")
# 保存图像
# plt.savefig("1*1的子图.png")
# plt.show()

ax.scatter(x_data[:, 0], x_data[:, 1], y_data, c="r", marker="o", s=50)

x0 = x_data[:, 0]
x1 = x_data[:, 1]
# 生成网格矩阵---每个点对应,一个面
x0, x1 = np.meshgrid(x0, x1)

# 预测值
z = theta0 + x0 * theta1 + x1 * theta2

# 画3D图
ax.plot_surface(x0, x1, z)

# 设置坐标轴
ax.set_xlabel("Mile")
ax.set_ylabel("Number of Deliveries")
ax.set_zlabel("Time")

plt.show()

