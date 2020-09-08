from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [13, 14, 26, 23, 15, 28, 22, 24, 15, 20, 25, 27]

# 设置图片大小
plt.figure(figsize=(10,8),dpi=80)

# 绘图
plt.plot(x, y)

# 保存图像
# plt.savefig("./fig1.png")
# 保存为svg矢量图，放大不会产生锯齿
# plt.savefig("./fig2.svg")

# x的刻度
# plt.xticks(x)

# 每隔3个取一个刻度
plt.xticks(x[::3])
# y从最小值到最大值取,最大值取不到,用max(y)+1取
plt.yticks(range(min(y), max(y)+1))

# 展示图形
plt.show()