# 使用多个键值对,存储描述一个物体的相关信息---描述更复杂的数据信息
# 将多个字典放在一个列表中,再进行遍历,在循环体内部对每个字典进行相同的操作
card_list =[
    {"name": "小明",
     "age": 18,
     "gender": True},
    {"name": "小丽",
     "age": 15,
     "gender": False}]

# 循环遍历字典
for card_info in card_list:
    print(card_info)