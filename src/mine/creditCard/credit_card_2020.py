# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2020.01
my = 1904.2
pf = 1637.8
zs = 2136.7
ms = 0
pay01 = pc.need_to_pay('2020.01', my, pf, zs, ms)

# 2020.02
ms = 0
my = 1195.31
zs = 401.24
pf = 1957.26
pay02 = pc.need_to_pay('2020.02', my, pf, zs, ms)

# 2020.03
ms = 0
my = 1685.36
zs = 723.10
pf = 742.30
pay03 = pc.need_to_pay('2020.03', my, pf, zs, ms)

# 2020.04
ms = 0
my = 3372.69
zs = 382.16
pf = 3318.49
pay04 = pc.need_to_pay('2020.04', my, pf, zs, ms)

# 2020.05
ms = 0
my = 1838.06
zs = 2906.56
pf = 605.84
pay05 = pc.need_to_pay('2020.05', my, pf, zs, ms)

# 2020.06
ms = 0
my = 2145.52
zs = 479.49
pf = 3316.26
pay06 = pc.need_to_pay('2020.06', my, pf, zs, ms)

# 2020.07
ms = 1868.76
my = 0
zs = 181
pf = 497
pay07 = pc.need_to_pay('2020.07', my, pf, zs, ms)

# 2020.08
ms = 0
my = 13.58
zs = 1281.52
pf = 2025.40
pay08 = pc.need_to_pay('2020.08', my, pf, zs, ms)

# 2020.09
ms = 0
my = 0
zs = 1949.81
pf = 6101.70
pay09 = pc.need_to_pay('2020.09', my, pf, zs, ms)

# 2020.10
ms = 0
my = 0
zs = 2797.56
pf = 7589.9
pay10 = pc.need_to_pay('2020.10', my, pf, zs, ms)

# 2020.11
ms = 0
my = 233.5
zs = 2263.56
pf = 1565.9
pay11 = pc.need_to_pay('2020.11', my, pf, zs, ms)

# 2020.12
ms = 0
my = 0
zs = 5380.57
pf = 537

pay12 = pc.need_to_pay('2020.12', my, pf, zs, ms)


cc_20_sum = sum([pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11, pay12])


print('2020.all ' + format(cc_20_sum,'0.2f'))
