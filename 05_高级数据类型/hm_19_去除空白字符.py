poem = ["\n\t登鹳雀楼",
         "王之涣",
         "白日依山尽\t",
         "黄河入海流",
         "欲穷千里目\t",
         "更上一层楼"]
for poem_str in poem:
    # 先使用strip方法去除字符串中的空白字符
    # 然后使用center函数居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))