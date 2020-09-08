poem_str = "登鹳雀楼\t王之涣\t白日依山尽\t黄河入海流\t欲穷千里目\t更上一层楼"
# 去掉空白字符(\t\n\r  空格),返回列表类型
print(poem_str.split())

# 2.合并字符串
# 使用" "作为分隔符，拼接字符串
result = " ".join(poem_str)
print(result)
# print(poem_str)