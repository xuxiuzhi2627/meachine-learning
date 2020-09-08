# encoding:utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# 第一种设置字体的方法---windows和linux系统
# font = {'family': 'Microsoft YaHei',
#           'weight': 'bold',
#           }
# matplotlib.rc('font', **font)
matplotlib.rc('font',family="Microsoft YaHei", weight="bold")

# 方法2：用matplotlib里font_manager,fname用字体的地址
my_font = font_manager.FontProperties(size=15, fname="/usr/share/fonts/truetype/arphic/ukai.ttc")

x= range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 设置图像大小
plt.figure(figsize=(50, 25), dpi=100)

# 画图
plt.plot(x,y)

# 取x的刻度
# plt.xticks(x[::10])

_x = list(x)
# 每个x刻度的标签值
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应，长度一样，标签旋转45度
plt.xticks(_x[::10], _xticks_labels[::10], rotation=45, fontproperties = my_font)

# 显示图像
plt.show()
