from mine.creditCard import pay_computes as pc

# 2018.01
my = 2361.9
pf = 2592.20
zs = 108.55
pay01 = pc.need_to_pay('2018.01', my, pf, zs)

# 2018.02
my = 1403.01
pf = 1596
zs = 4353
pay02 = pc.need_to_pay('2018.02', my, pf, zs)

# 2018.03
my = 1379.01
pf = 581.11
zs = 0
pay03 = pc.need_to_pay('2018.03', my, pf, zs)

# 2018.04
my = 1806.95
pf = 861.1
zs = 361
pay04 = pc.need_to_pay('2018.04', my, pf, zs)

# 2018.05
my = 1495.58
pf = 1085
zs = 1735.5
ms = 591.4
pay05 = pc.need_to_pay('2018.05', my, pf, zs, ms)

# 2018.06
my = 1498.86
pf = 432.75
zs = 1309.97
ms = 229
pay06 = pc.need_to_pay('2018.06', my, pf, zs, ms)

sum_pay = [pay01, pay02, pay03, pay04]

print(round(sum(sum_pay), 2))
