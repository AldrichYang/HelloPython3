number = 40000
base_multiple = 1000
ranges = list(range(0, 40000, 1000))
i = 1
range_list = []
while i < len(ranges):
    range_list.append((ranges[i - 1], ranges[i]))
    i = i + 1

[print("update finance_plan set base_rate = 0 where base_rate !=0 and  id >{} and id <={};".format(each[0], each[1]))
 for
 each in
 range_list]


def one_range(multiple=1000, factor=0):
    return multiple * (factor - 1), multiple * factor


