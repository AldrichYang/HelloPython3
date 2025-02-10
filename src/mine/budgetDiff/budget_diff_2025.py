# 计算预算和收入差额
def calc_budget_diff(yearmonth, budget, income, balance=0):
    budget_diff_money = balance + income - budget
    # format数字格式化
    print(yearmonth + ' budget amonut difference is : ', format(budget_diff_money, '0.2f'))
    return budget_diff_money

'''
2025每月定额预算金额:  
    房贷24000 , 养老3000, 房子月用1000,  保险1000, 日用 3500, 度假 2000
    孩子生活1500, 孩子教育1500,
    家人2000, 父母1000
'''
# 2025每月定额预算金额
budget_regular_month = 24000 + 3000 + 1000 + 1000 + 3500 + 2000 + 1500 + 1500 + 2000 + 1000
print("2025年月度预算项目总金额：",budget_regular_month)

# 2025.01
income01 = 44919.31
buget_diff_01 = calc_budget_diff("202501", budget_regular_month, income01)

# 2025.02
income02 = 0
buget_diff_02 = calc_budget_diff("202502", budget_regular_month, income02)

# 2025.03
income03 = 0
buget_diff_03 = calc_budget_diff("202503", budget_regular_month, income03)

# 2025.04
income04 = 0
buget_diff_04 = calc_budget_diff("202504", budget_regular_month, income04)

# 2025.05
income05 = 0
buget_diff_05 = calc_budget_diff("202505", budget_regular_month, income05)

# 2025.06
income06 = 0
buget_diff_06 = calc_budget_diff("202506", budget_regular_month, income06)

# 2025.07
income07 = 0
buget_diff_07 = calc_budget_diff("202507", budget_regular_month, income07)

# 2025.08
income08 = 0
buget_diff_08 = calc_budget_diff("202508", budget_regular_month, income08)

# 2025.09
income09 = 0
buget_diff_09 = calc_budget_diff("202509", budget_regular_month, income09)

# 2025.10
income10 = 0
buget_diff_10 = calc_budget_diff("202510", budget_regular_month, income10)

# 2025.11
income11 = 0
buget_diff_11 = calc_budget_diff("202511", budget_regular_month, income11)

# 2025.12
income12 = 0
buget_diff_12 = calc_budget_diff("202512", budget_regular_month, income12)

sum_income = [income01, income02, income03, income04, income05, income06, income07, income08, income09, income10, income11, income12]
print('total income of 2025 is:', round(sum(sum_income), 2))

#计算月平均收入
avg_income = round(sum(sum_income) / len(sum_income), 2)
print('average income of 2025 is:', avg_income)

sum_budget_diff = [buget_diff_01, buget_diff_02, buget_diff_03, buget_diff_04, buget_diff_05,
                   buget_diff_06, buget_diff_07, buget_diff_08, buget_diff_09, buget_diff_10, buget_diff_11, buget_diff_12]

print('total budget diff amount of 2025 is:', round(sum(sum_budget_diff), 2))