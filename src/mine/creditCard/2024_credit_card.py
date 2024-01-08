# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2024.01
my = 0
pf = 0
zs = 0
ms = 0
pay01 = pc.need_to_pay('2024.01', my, pf, zs, ms)

# 2024.02
ms = 0
my = 0
zs = 0
pf = 0
pay02 = pc.need_to_pay('2024.02', my, pf, zs, ms)

# 2024.03
ms = 0
my = 0
zs = 0
pf = 0
pay03 = pc.need_to_pay('2024.03', my, pf, zs, ms)

# 2024.04
ms = 0
my = 0
zs = 0
pf = 0
pay04 = pc.need_to_pay('2024.04', my, pf, zs, ms)

# 2024.05
ms = 0
my = 0
zs = 0
pf = 0
pay05 = pc.need_to_pay('2024.05', my, pf, zs, ms)

# 2024.06
ms = 0
my = 0
zs = 0
pf = 0
pay06 = pc.need_to_pay('2024.06', my, pf, zs, ms)

# 2024.07
ms = 0
my = 0
zs = 0
pf = 0
pay07 = pc.need_to_pay('2024.07', my, pf, zs, ms)

# 2024.08
ms = 0
my = 0
zs = 0
pf = 0
pay08 = pc.need_to_pay('2024.08', my, pf, zs, ms)

# 2024.09
ms = 0
my = 0
zs = 0
pf = 0
pay09 = pc.need_to_pay('2024.09', my, pf, zs, ms)

# 2024.10
ms = 0
my = 0
zs = 0
pf = 0
pay10 = pc.need_to_pay('2024.10', my, pf, zs, ms)

# 2024.11
ms = 0
my = 0
zs = 0
pf = 0
pay11 = pc.need_to_pay('2024.11', my, pf, zs, ms)

# 2024.12
ms = 0
my = 0
zs = 0
pf = 0

pay12 = pc.need_to_pay('2024.12', my, pf, zs, ms)


sum_pay = [pay01, pay02, pay03, pay04, pay05,
           pay06, pay07, pay08, pay09, pay10, pay11, pay12]

print('total credit cost of 2024 is:',round(sum(sum_pay), 2))
