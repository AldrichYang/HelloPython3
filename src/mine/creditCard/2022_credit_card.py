# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2022.01
my = 0
pf = 2653.99
zs = 5340.6
ms = 0
pay01 = pc.need_to_pay('2022.01', my, pf, zs, ms)

# 2022.02
ms = 0
my = 0
zs = 3243.95
pf = 3154
pay02 = pc.need_to_pay('2022.02', my, pf, zs, ms)

# 2022.03
ms = 0
my = 0
zs = 2456.63
pf = 7668.6
pay03 = pc.need_to_pay('2022.03', my, pf, zs, ms)

# 2022.04
ms = 0
my = 0
zs = 427.56
pf = 1062.62
pay04 = pc.need_to_pay('2022.04', my, pf, zs, ms)

# 2022.05
ms = 0
my = 0
zs = 0
pf = 0
pay05 = pc.need_to_pay('2022.05', my, pf, zs, ms)

# 2022.06
ms = 0
my = 0
zs = 0
pf = 0
pay06 = pc.need_to_pay('2022.06', my, pf, zs, ms)

# 2022.07
ms = 0
my = 0
zs = 0
pf = 0
pay07 = pc.need_to_pay('2022.07', my, pf, zs, ms)

# 2022.08
ms = 0
my = 0
zs = 0
pf = 0
pay08 = pc.need_to_pay('2022.08', my, pf, zs, ms)

# 2022.09
ms = 0
my = 0
zs = 0
pf = 0
pay09 = pc.need_to_pay('2022.09', my, pf, zs, ms)

# 2022.10
ms = 0
my = 0
zs = 0
pf = 0
pay10 = pc.need_to_pay('2022.10', my, pf, zs, ms)

# 2022.11
ms = 0
my = 0
zs = 0
pf = 0
pay11 = pc.need_to_pay('2022.11', my, pf, zs, ms)

# 2022.12
ms = 0
my = 0
zs = 0
pf = 0

pay12 = pc.need_to_pay('2022.12', my, pf, zs, ms)


sum_pay = [pay01, pay02, pay03, pay04, pay05,
           pay06, pay07, pay08, pay09, pay10, pay11, pay12]

print('total credit cost of 2022 is:',round(sum(sum_pay), 2))
