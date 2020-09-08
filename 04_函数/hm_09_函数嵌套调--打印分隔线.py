# 定义一个print_line函数打印 * 组成的一条分隔线
# def print_line():
#     print("*" * 50)
# print_line()

# 定义一个print_line函数打印 任意字符 组成的一条分隔线
# def print_line(char):
#     print(char * 50)
# print_line("-")

# 定义一个print_line函数打印 任意字符 任意次数的组成的一条分隔线
def print_line(char,times):

    print(char * times)

print_line("-", 10)