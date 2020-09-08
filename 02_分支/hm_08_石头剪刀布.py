# 导入随机工具包
# 注意:在导入工具包的时候,应该将导入的语句放在文件的顶部
# 因为这样可以方便下方的代码在任何需要的时候,使用工具包中的工具
import random

# 从控制台输入要出的拳----石头(1)/剪刀(2)/布(3)
player = int(input("请输入您要出的拳--石头(1)/剪刀(2)/布(3):"))

# 电脑随机出拳
computer = random.randint(1, 3)

# 打印出拳信息
print("玩家选择的拳头是%d, 电脑选择的拳头是%d" %(player, computer))

# 比较胜负
# 1.石头 胜 剪刀
# 2.剪刀 胜 布
# 3.布 胜 石头
# 增加括号可以将下面的or向下回车缩进
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利,电脑弱爆了")
# 平局
elif player == computer:
    print("真是心有灵犀,再来一局")
# 其他情况电脑胜利
else:
    print("不服气,我们决战到天亮!")