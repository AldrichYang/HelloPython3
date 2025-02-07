# from mine.creditCard import pay_computes as pc
from src.mine.creditCard import pay_computes as pc

# 2025.01
zs = 3659.71
pf = 0
pay01 = pc.need_to_pay('2025.01',  pf, zs)

# 2025.02
zs = 0
pf = 0
pay02 = pc.need_to_pay('2025.02',  pf, zs, )

# 2025.03
zs = 0
pf = 0
pay03 = pc.need_to_pay('2025.03',  pf, zs, )

# 2025.04
zs = 0
pf = 0
pay04 = pc.need_to_pay('2025.04',  pf, zs, )

# 2025.05
zs = 0
pf = 0
pay05 = pc.need_to_pay('2025.05',  pf, zs, )

# 2025.06
zs = 0
pf = 0
pay06 = pc.need_to_pay('2025.06',  pf, zs, )

# 2025.07
zs = 0
pf = 0
pay07 = pc.need_to_pay('2025.07',  pf, zs, )

# 2025.08
zs = 0
pf = 0
pay08 = pc.need_to_pay('2025.08',  pf, zs, )

# 2025.09
zs = 0
pf = 0
pay09 = pc.need_to_pay('2025.09',  pf, zs, )

# 2025.10
zs = 0
pf = 0
pay10 = pc.need_to_pay('2025.10',  pf, zs, )

# 2025.11
zs = 0
pf = 0
pay11 = pc.need_to_pay('2025.11',  pf, zs, )

# 2025.12
zs = 0
pf = 0
zs_baby = 319+48+228+66+2823.4+500+1300+1978+80+610+105+7+22+52+18+936.37+935.10


pay12 = pc.need_to_pay('2025.12', pf, zs, )


cc_24_sum = sum([pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11, pay12])


print('2025.all ' + format(cc_24_sum,'0.2f'))
