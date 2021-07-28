import math
def each_year(x, add):
    return (x + add) * 1.09


each_year_add = [120000] * 20
earn_after_20_year = 0
for each in each_year_add:
    earn_after_20_year = each_year(earn_after_20_year, each)

print(earn_after_20_year)

print(earn_after_20_year * math.pow(1.05, 5))


rate_list = [7.20, 7.40, 7.60, 7.80, 8.00,
             8.20, 8.40, 8.60, 8.80, 9.00, 9.20, 9.40]
amount = 1000
days = 415
profit = []
[profit.append(round(amount * 30 * each / 100 / 365,2)) for each in rate_list]
print(sum(profit) + round(amount * (days%(30*12))*9.4/100/365,2))
print(pow(2,32))