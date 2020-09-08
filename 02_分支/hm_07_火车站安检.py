# 定义布尔型变量has_ticket表示是否有车票
has_ticket = True
# 定义整型变量knife_length,表示刀的长度,单位:厘米
knife_length = 30
# 首先检查是否有车票,如果有,才允许进行安检
if has_ticket:
    print("车票检查通过,准备进行安检")
    # 安检时,需要按照道的长度,判断是否超过20厘米
    # 如果查过20厘米,提示刀的长度,不允许上车
    if knife_length > 20:
        print("您携带的刀太长了,有%d厘米,超过20厘米,不允许上车" % knife_length)
    # 如果不超过20厘米,安检通过
    # 注意和上一个if对齐
    else:
        print("安检通过,祝您旅途愉快!")
# 如果没有车票,不允许进门
else:
    print("没有车票,不允许进门")
