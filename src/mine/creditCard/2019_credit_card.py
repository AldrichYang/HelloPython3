# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2019.01
my = 1384.42
pf = 636.85
zs = 1776.03
ms = 364.1
pay01 = pc.need_to_pay('2019.01', my, pf, zs, ms)

# 2019.02
ms = 308.5
my = 1062.65
zs = 597.65
pf = 3158.2
pay02 = pc.need_to_pay('2019.02', my, pf, zs, ms)

# 2019.03
ms = 0
my = 1626.67
zs = 1652.48
pf = 540
pay03 = pc.need_to_pay('2019.03', my, pf, zs, ms)

# 2019.04
ms = 0
my = 1848.79
zs = 135.03
pf = 378
pay04 = pc.need_to_pay('2019.04', my, pf, zs, ms)

# 2019.05
ms = 0
my = 1506.38
zs = 1345.00
pf = 4950.48
pay05 = pc.need_to_pay('2019.05', my, pf, zs, ms)

sum_pay = [pay01, pay02, pay03,pay04]

print(round(sum(sum_pay), 2))
