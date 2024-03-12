# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2024.01
zs = 2564.35
pf = 2139
pay01 = pc.need_to_pay('2024.01',  pf, zs)

# 2024.02
zs = 2897.22
pf = 6107.46
pay02 = pc.need_to_pay('2024.02',  pf, zs, )

# 2024.03
zs = 0
pf = 0
pay03 = pc.need_to_pay('2024.03',  pf, zs, )

# 2024.04
zs = 0
pf = 0
pay04 = pc.need_to_pay('2024.04',  pf, zs, )

# 2024.05
zs = 0
pf = 0
pay05 = pc.need_to_pay('2024.05',  pf, zs, )

# 2024.06
zs = 0
pf = 0
pay06 = pc.need_to_pay('2024.06',  pf, zs, )

# 2024.07
zs = 0
pf = 0
pay07 = pc.need_to_pay('2024.07',  pf, zs, )

# 2024.08
zs = 0
pf = 0
pay08 = pc.need_to_pay('2024.08',  pf, zs, )

# 2024.09
zs = 0
pf = 0
pay09 = pc.need_to_pay('2024.09',  pf, zs, )

# 2024.10
zs = 0
pf = 0
pay10 = pc.need_to_pay('2024.10',  pf, zs, )

# 2024.11
zs = 0
pf = 0
pay11 = pc.need_to_pay('2024.11',  pf, zs, )

# 2024.12
zs = 0
pf = 0

pay12 = pc.need_to_pay('2024.12', pf, zs, )


sum_pay = [pay01, pay02, pay03, pay04, pay05,
           pay06, pay07, pay08, pay09, pay10, pay11, pay12]

print('total credit cost of 2024 is:',round(sum(sum_pay), 2))
