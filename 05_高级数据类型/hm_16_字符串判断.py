# str = " \t\n\r"
# 1. 判断是否只包含空格,则返回True
# print(str.isspace())

# 2. 判断是否字符串中的字符是否为字母或者数字,则返回True
# str = "adn35"
# print(str.isalnum())
# str = "adf"
# print(str.isalnum())

# 3.判断所有字符都是字母,则返回True
str = "abns"
# print(str.isalpha())

# 4. 判断字符串中是否只包含数字
# num_str = "1.8"
# <1>isdecimal()(开发中常用),isdigit(),isnumeric()都可以判断整型数字,都不能判断小数
# print(num_str.isdecimal()) 
# print(num_str.isdigit())
# print(num_str.isnumeric())

# <2>isnumeric()不可以判断unicode字符串
# num_str = "\u00b2"
# print(num_str) #---->平方符号
# print(num_str.isnumeric())   #---->False
# print(num_str.isdigit())     #---->True
# print(num_str.isnumeric())   #---->True

# <3>isnumeric()可以判断汉字中的数字
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())   #--->False
print(num_str.isdigit())     #--->False
print(num_str.isnumeric())   #--->True