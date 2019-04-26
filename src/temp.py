import math
def each_year(x, add):
    return (x + add) * 1.09


each_year_add = [120000] * 20
earn_after_20_year = 0
for each in each_year_add:
    earn_after_20_year = each_year(earn_after_20_year, each)

print(earn_after_20_year)

print(earn_after_20_year * math.pow(1.05, 5))