# 要求:顺序并且居中对齐输出以下内容
poem = ["登鹳雀楼",
         "王之涣",
         "白日依山尽",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]
for poem_str in poem:
    # "　"处要用中文全角字体输入，10表示width
    # "　"表示fillchar填充字符
    # print("|%s|" % poem_str.center(10, "　"))
    # print("|%s|" % poem_str.ljust(10, "　"))
    # print("|%s|" % poem_str.rjust(10, "　"))