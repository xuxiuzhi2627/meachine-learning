# encoding:utf-8
# 条件分支(if-else)
# temp = input("请输入一个数字：")
# guess = int(temp)
# if guess == 8:
#     print("你是小甲鱼肚子里的蛔虫吗？")
#     print("哼，猜对也没有奖励")
# else:
#     if guess > 8:
#         print("哥，大了大了")
#     else:
#         print("嘿，小了小了")
# print("游戏结束，不玩啦")

# temp = input("请输入一个数字：")
# guess = int(temp)
# if guess == 8:
#     print("你是小甲鱼肚子里的蛔虫吗？")
#     print("哼，猜对也没有奖励")
# elif guess > 8:
#     print("哥，大了大了")
# else:
#     print("嘿，小了小了")
# print("游戏结束，不玩啦")

# while循环

count = 1
while count < 4:
    temp = input("请输入小甲鱼心里想的数字：")
    guess = int(temp)
    if guess == 8:
        print("你是小甲鱼肚子里的蛔虫吗？")
        print("哼，猜对也没有奖励")
        break
    elif guess > 8:
        print("哥，大了大了")
    else:
        print("嘿，小了小了")
    count += 1
else:
    print("次数用完了")
print("游戏结束，不玩啦")
