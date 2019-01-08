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

# 2018.07
my = 1172.22
pf = 551
zs = 617.7
ms = 322.26
pay07 = pc.need_to_pay('2018.07', my, pf, zs, ms)

# 2018.08
my = 1630.98
zs = 209.70
pf = 1220.00
ms = 0
pay08 = pc.need_to_pay('2018.08', my, pf, zs, ms)

# 2018.09
my = 2924.41
zs = 3422.8
pf = 628.26
ms = 0
jd = 152.9
pay09 = pc.need_to_pay('2018.09', my, pf, zs, ms, jd)

# 2018.10
my = 1387.40
zs = 2059.37
pf = 2116.70
ms = 141.50
pay10 = pc.need_to_pay('2018.10', my, pf, zs, ms)

# 2018.11
my = 1536
zs = 161.90
pf = 472.92
ms = 0
pay11 = pc.need_to_pay('2018.11', my, pf, zs, ms)

# 2018.12
zs = 217
pf = 1668
ms = 0
my = 1595.40
pay12 = pc.need_to_pay('2018.12', my, pf, zs, ms)

sum_pay = [pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11, pay12]

print(round(sum(sum_pay), 2))
