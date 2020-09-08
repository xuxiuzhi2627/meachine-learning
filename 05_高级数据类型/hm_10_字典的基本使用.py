xiaoming_dict = {"name": "小明"}

# 1.取值----通过键取值
# print(xiaoming_dict["name"])
# 若key不存在,程序会报错!
# print(xiaoming_dict["name123"])

# 2.增加/修改
# 若key不存在,会新增键值对
# xiaoming_dict["age"] = 18
# 若key存在,会修改键值对
# xiaoming_dict["name"] = "小小明"

# 若key不存在,新增键值对
xiaoming_dict.setdefault("age", "18")
# 若key存在,保持原来的值不变
xiaoming_dict.setdefault("age", "19")


# 3.删除
# 若key存在,则会删除对应的键值对
# xiaoming_dict.pop("name")
# 若key不存在,程序会报错!
# xiaoming_dict.pop("name123")

# 随机删除一对键值对
xiaoming_dict.popitem()

print(xiaoming_dict)