# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2021.01
my = 0
pf = 5928.6
zs = 6108.11
ms = 0
pay01 = pc.need_to_pay('2021.01', my, pf, zs, ms)

# 2021.02
ms = 0
my = 0
zs = 5122.33
pf = 2046
pay02 = pc.need_to_pay('2021.02', my, pf, zs, ms)

# 2021.03
ms = 0
my = 0
zs = 1618.67
pf = 7475.90
pay03 = pc.need_to_pay('2021.03', my, pf, zs, ms)

# 2021.04
ms = 0
my = 0
zs = 3207
pf = 7870
pay04 = pc.need_to_pay('2021.04', my, pf, zs, ms)

# 2021.05
ms = 0
my = 480
zs = 2899.29
pf = 4033.24
pay05 = pc.need_to_pay('2021.05', my, pf, zs, ms)

# 2021.06
ms = 0
my = 0
zs = 3709.83
pf = 1810.98
pay06 = pc.need_to_pay('2021.06', my, pf, zs, ms)

# 2021.07
ms = 0
my = 0
zs = 1539.79
pf = 4507
pay07 = pc.need_to_pay('2021.07', my, pf, zs, ms)

# 2021.08
ms = 0
my = 0
zs = 1783.15
pf = 988.36
pay08 = pc.need_to_pay('2021.08', my, pf, zs, ms)

# 2021.09
ms = 0
my = 0
zs = 2058.58
pf = 16846.20
pay09 = pc.need_to_pay('2021.09', my, pf, zs, ms)

# 2021.10
ms = 0
my = 0
zs = 2240.16
pf = 11222.00
pay10 = pc.need_to_pay('2021.10', my, pf, zs, ms)

# 2021.11
ms = 0
my = 0
zs = 1722.53
pf = 1584
pay11 = pc.need_to_pay('2021.11', my, pf, zs, ms)

# 2021.12
ms = 0
my = 0
zs = 2952.29
pf = 6366

pay12 = pc.need_to_pay('2021.12', my, pf, zs, ms)


cc_21_sum = sum([pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11, pay12])


print('2021.all ' + format(cc_21_sum,'0.2f'))
