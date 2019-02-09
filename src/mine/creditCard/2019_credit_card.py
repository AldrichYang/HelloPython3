from mine.creditCard import pay_computes as pc

# 2019.01
my = 1384.42
pf = 636.85
zs = 1776.03
ms = 364.1
pay01 = pc.need_to_pay('2019.01', my, pf, zs)


sum_pay = [pay01]

print(round(sum(sum_pay), 2))
