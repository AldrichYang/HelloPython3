from src.creditCard import pay_computes as pc

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
