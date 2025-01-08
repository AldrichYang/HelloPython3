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
zs = 2279.56
pf = 2330.10
pay03 = pc.need_to_pay('2024.03',  pf, zs, )

# 2024.04
zs = 2900.56
pf = 2932.3
pay04 = pc.need_to_pay('2024.04',  pf, zs, )

# 2024.05
zs = 3276.67
pf = 4196.85
pay05 = pc.need_to_pay('2024.05',  pf, zs, )

# 2024.06
zs = 2755.27
pf = 13066.45
pay06 = pc.need_to_pay('2024.06',  pf, zs, )

# 2024.07
zs = 5325.52
pf = 1872.17
pay07 = pc.need_to_pay('2024.07',  pf, zs, )

# 2024.08
zs = 2546.12
pf = 1444.00
pay08 = pc.need_to_pay('2024.08',  pf, zs, )

# 2024.09
zs = 1868.27
pf = 4616.54
pay09 = pc.need_to_pay('2024.09',  pf, zs, )

# 2024.10
zs = 3480.67
pf = 16575.99
pay10 = pc.need_to_pay('2024.10',  pf, zs, )

# 2024.11
zs = 2616.63
pf = 7553.89
pay11 = pc.need_to_pay('2024.11',  pf, zs, )

# 2024.12
zs = 12732.01
pf = 2190.47
zs_baby = 319+48+228+66+2823.4+500+1300+1978+80+610+105+7+22+52+18+936.37+935.10
'''
本月孩子的支出：10027.87
本月消费的支出：4894.61
'''

pay12 = pc.need_to_pay('2024.12', pf, zs, )


cc_24_sum = sum([pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11, pay12])


print('2024.all ' + format(cc_24_sum,'0.2f'))
