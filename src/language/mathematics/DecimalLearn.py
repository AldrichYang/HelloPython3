from decimal import *

getcontext().prec = 6
print(Decimal(1.35) + Decimal(6.15))
print(Decimal(419.99) == float(419.99))
print(Decimal(35) == float(35.0))
print(Decimal(419.99).__float__().hex())
print(float(419.99).hex())
