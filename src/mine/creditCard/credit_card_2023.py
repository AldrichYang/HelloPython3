# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2023.01
my = 0
pf = 14110.47
zs = 2377.78
ms = 0
pay01 = pc.need_to_pay('2023.01', my, pf, zs, ms)

# 2023.02
ms = 0
my = 0
zs = 3154.74
pf = 2615
pay02 = pc.need_to_pay('2023.02', my, pf, zs, ms)

# 2023.03
ms = 0
my = 0
zs = 1985.66
pf = 8425.68
pay03 = pc.need_to_pay('2023.03', my, pf, zs, ms)

# 2023.04
ms = 0
my = 0
zs = 3482.46
pf = 9422.38
pay04 = pc.need_to_pay('2023.04', my, pf, zs, ms)

# 2023.05
ms = 0
my = 0
zs = 2875.3
pf = 1708.07
pay05 = pc.need_to_pay('2023.05', my, pf, zs, ms)

# 2023.06
ms = 0
my = 0
zs = 3673.58
pf = 10132.8
pay06 = pc.need_to_pay('2023.06', my, pf, zs, ms)

# 2023.07
ms = 0
my = 0
zs = 2417.4
pf = 2997.4
pay07 = pc.need_to_pay('2023.07', my, pf, zs, ms)

# 2023.08
ms = 0
my = 0
zs = 9326.4
pf = 16218.1
pay08 = pc.need_to_pay('2023.08', my, pf, zs, ms)

# 2023.09
ms = 0
my = 0
zs = 4341.76
pf = 2787
pay09 = pc.need_to_pay('2023.09', my, pf, zs, ms)

# 2023.10
ms = 0
my = 0
zs = 1713.23
pf = 3882.91
pay10 = pc.need_to_pay('2023.10', my, pf, zs, ms)

# 2023.11
ms = 0
my = 0
zs = 3279.57
pf = 3464.36
pay11 = pc.need_to_pay('2023.11', my, pf, zs, ms)

# 2023.12
ms = 0
my = 0
zs = 1094.66
pf = 3859.42

pay12 = pc.need_to_pay('2023.12', my, pf, zs, ms)


cc_23_sum = sum([pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11, pay12])


print('2023.all ' + format(cc_23_sum,'0.2f'))



