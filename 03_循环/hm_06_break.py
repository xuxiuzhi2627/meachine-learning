i = 0
while i < 10:
    # break 某一条件满足时，退出所有循环，不执行后续的重复代码
    # 4-9不会执行,直接跳出while循环
    if i == 3:
        # 直接跳出循环,执行打印over
        break
    print(i)
    i += 1
print("over")
