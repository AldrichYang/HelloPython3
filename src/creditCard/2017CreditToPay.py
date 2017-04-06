def need_to_pay(yearmonth, my, pf, zs):
    print(yearmonth + ' credit card cost: ', round(my + pf + zs, 2))


# 2016.12
my = 3901.5
pf = 1204.0
zs = 4845.63
need_to_pay('2016.12', my, pf, zs)

# 2017.01
my = 1759.61
zs = 7918.85
pf = 378.0
need_to_pay('2017.01', my, pf, zs)

# 2017.02
my = 1586.88
pf = 527.0
zs = 4643.27
need_to_pay('2017.02', my, pf, zs)

# 2017.03
my = 1464.51
pf = 527.98
zs = 859.97
need_to_pay('2017.03', my, pf, zs)
