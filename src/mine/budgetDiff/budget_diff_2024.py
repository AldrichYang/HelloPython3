# 计算预算和收入差额
def calc_budget_diff(yearmonth, budget, income, balance=0):
    budget_diff_money = balance + income - budget
    # format数字格式化
    print(yearmonth + ' budget amonut difference is : ', format(budget_diff_money, '0.2f'))
    return budget_diff_money

# 2024每月定额预算金额: 房贷 (20000 + 4000) + 长投3000 + 房租1000 + 保险1000 + 孩子3000 + 家人2000 + 父母1000 + 消费5500

budget_regular_month_before4 = 20000 + 3000 + 1000 + 1000 + 3000 + 2000 + 1000 + 5500
print("2024年月度预算项目总金额before 4月：",budget_regular_month_before4)

budget_regular_month = 24000 + 3000 + 1000 + 1000 + 3000 + 2000 + 1000 + 5500
print("2024年月度预算项目总金额：",budget_regular_month)

# 2024.01
income01 = 37317.62
buget_diff_01 = calc_budget_diff("202401", budget_regular_month_before4, income01)

# 2024.02
income02 = 38990.21
buget_diff_02 = calc_budget_diff("202402", budget_regular_month_before4, income02)

# 2024.03
income03 = 37091.91
buget_diff_03 = calc_budget_diff("202403", budget_regular_month_before4, income03)

# 2024.04
income04 = 40637.92
buget_diff_04 = calc_budget_diff("202404", budget_regular_month, income04)

# 2024.05
income05 = 38131.74
buget_diff_05 = calc_budget_diff("202405", budget_regular_month, income05)

# 2024.06
income06 = 36979.48
buget_diff_06 = calc_budget_diff("202406", budget_regular_month, income06)

# 2024.07
income07 = 37028.23
buget_diff_07 = calc_budget_diff("202407", budget_regular_month, income07)

# 2024.08
income08 = 36938.63
buget_diff_08 = calc_budget_diff("202408", budget_regular_month, income08)

# 2024.09
income09 = 36187.24
buget_diff_09 = calc_budget_diff("202409", budget_regular_month, income09)

# 2024.10
income10 = 33889.46
buget_diff_10 = calc_budget_diff("202410", budget_regular_month, income10)

# 2024.11
income11 = 35806.72
buget_diff_11 = calc_budget_diff("202411", budget_regular_month, income11)

# 2024.12
income12 = 0
buget_diff_12 = calc_budget_diff("202412", budget_regular_month, income12)

sum_income = [income01, income02, income03, income04, income05, income06, income07, income08, income09, income10, income11, income12]
print('total income of 2024 is:', round(sum(sum_income), 2))

#计算月平均收入
avg_income = round(sum(sum_income) / len(sum_income), 2)
print('average income of 2024 is:', avg_income)

sum_budget_diff = [buget_diff_01, buget_diff_02, buget_diff_03, buget_diff_04, buget_diff_05,
                   buget_diff_06, buget_diff_07, buget_diff_08, buget_diff_09, buget_diff_10, buget_diff_11, buget_diff_12]

print('total budget diff amount of 2024 is:', round(sum(sum_budget_diff), 2))