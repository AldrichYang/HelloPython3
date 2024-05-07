# 统计信用卡这些年的总花费和平均每年花费

from credit_card_2017 import cc_17_sum
from credit_card_2018 import cc_18_sum
from credit_card_2019 import cc_19_sum
from credit_card_2020 import cc_20_sum
from credit_card_2021 import cc_21_sum
from credit_card_2022 import cc_22_sum
from credit_card_2023 import cc_23_sum
from credit_card_2024 import cc_24_sum


year_cost_2017 = cc_17_sum
year_cost_2018 = cc_18_sum
year_cost_2019 = cc_19_sum
year_cost_2020 = cc_20_sum
year_cost_2021 = cc_21_sum
year_cost_2022 = cc_22_sum
year_cost_2023 = cc_23_sum

year_costs = [year_cost_2017,year_cost_2018,year_cost_2019,year_cost_2020,year_cost_2021,year_cost_2022,year_cost_2023]

total_pay_2017_2023 = sum(year_costs)
average_year_pay = round(total_pay_2017_2023/year_costs.__len__(), 2)

# 一个print函数打印多个结果,多个结果放在字符串的特定位置
print('''2017-2023 total credit cost of 7 years is: %s 
        average year is : %s ''' % 
      (total_pay_2017_2023, average_year_pay))

