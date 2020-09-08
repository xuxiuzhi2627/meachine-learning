# continue演练
i = 0
while i < 10:
    # continue当某一条件满足时，不执行后续重复的代码,
    # 退出当前循环,回到while
    if i == 3:
        # 注意：在循环中，使用continue这个关键字前，需要确认循环的计数是否修改
        # 不加i += 1,会造成死循环
        i += 1
        continue
    print(i)
    i += 1


