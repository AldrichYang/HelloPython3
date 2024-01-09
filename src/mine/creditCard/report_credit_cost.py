# 统计信用卡这些年的总花费和平均每年花费

year_cost_2017 = 80300.64
year_cost_2018 = 49990.31
year_cost_2019 = 51169.26
year_cost_2020 = 65035.1
year_cost_2021 = 106120.01
year_cost_2022 = 172700.88
year_cost_2023 = 119346.13

year_costs = [year_cost_2017,year_cost_2018,year_cost_2019,year_cost_2020,year_cost_2021,year_cost_2022,year_cost_2023]

total_pay_2017_2023 = sum(year_costs)
average_year_pay = round(total_pay_2017_2023/year_costs.__len__(), 2)

# 一个print函数打印多个结果,多个结果放在字符串的特定位置
print('''2017-2023 total credit cost of 7 years is: %s 
        average year is : %s ''' % 
      (total_pay_2017_2023, average_year_pay))

