from decimal import *

getcontext().prec = 6
print(Decimal(1.35) + Decimal(6.15))
print(Decimal(419.99) == float(419.99))
print(Decimal(35) == float(35.0))
print(Decimal(419.99).__float__().hex())
print(float(419.99).hex())

print(round(31358.430000 - 3205.790000, 2))
print(28152.64)

coupon_csyy = {

}
if "123" in coupon_csyy:
    print(coupon_csyy["123"])
else:
    print(110)

print(810 + 12857.67 + 184940)
print(round(810 + 12857.67 + 184940 - 84679.2, 2))
