# 计算预算和收入差额
def calc_budget_diff(yearmonth, budget, income, balance=0):
    budget_diff_money = balance + income - budget
    # format数字格式化
    print(yearmonth + ' budget amonut difference is : ', format(budget_diff_money, '0.2f'))
    return budget_diff_money

# 2023每月定额预算金额: 买房20000 + 长投3000 + 房租1000 + 保险1000 + 孩子3000 + 家人2000 + 父母1000 + 消费5500
budget_regular_month = 20000 + 3000 + 1000 + 1000 + 3000 + 2000 + 1000 + 5500
print("2023年月度预算项目总金额：",budget_regular_month)

# 2023.01
income01 = 38381.99
buget_diff_01 = calc_budget_diff("202301", budget_regular_month, income01)

# 2023.02
income02 = 36606.79
buget_diff_02 = calc_budget_diff("202302", budget_regular_month, income02)

# 2023.03
income03 = 36441.39
buget_diff_03 = calc_budget_diff("202303", budget_regular_month, income03)

# 2023.04
income04 = 37143.53
buget_diff_04 = calc_budget_diff("202304", budget_regular_month, income04)

# 2023.05
income05 = 35482.96
buget_diff_05 = calc_budget_diff("202305", budget_regular_month, income05)

# 2023.06
income06 = 34025.8
buget_diff_06 = calc_budget_diff("202306", budget_regular_month, income06)

# 2023.07
income07 = 33791.48
buget_diff_07 = calc_budget_diff("202307", budget_regular_month, income07)

# 2023.08
income08 = 34383.48
buget_diff_08 = calc_budget_diff("202308", budget_regular_month, income08)

# 2023.09
income09 = 33843.48
buget_diff_09 = calc_budget_diff("202309", budget_regular_month, income09)

# 2023.10
income10 = 40564.46
buget_diff_10 = calc_budget_diff("202310", budget_regular_month, income10)

# 2023.11
income11 = 31860.82
buget_diff_11 = calc_budget_diff("202311", budget_regular_month, income11)

# 2023.12
income12 = 32228.26
buget_diff_12 = calc_budget_diff("202312", budget_regular_month, income12)

sum_income = [income01, income02, income03, income04, income05, income06, income07, income08, income09, income10, income11, income12]
print('total income of 2023 is:', round(sum(sum_income), 2))

sum_budget_diff = [buget_diff_01, buget_diff_02, buget_diff_03, buget_diff_04, buget_diff_05,
                   buget_diff_06, buget_diff_07, buget_diff_08, buget_diff_09, buget_diff_10, buget_diff_11, buget_diff_12]

print('total budget amount difference of 2023 is:', round(sum(sum_budget_diff), 2))