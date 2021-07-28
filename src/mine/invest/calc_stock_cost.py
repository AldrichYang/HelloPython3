# 现在单位成本价，现在数量
current_unit_cost = 78.1
current_amount = 1300

# 计算补仓后成本价
def calc_stock_new_cost(add_buy_amount,add_buy_unit_cost):
    # 补仓买入成本
    buy_stock_cost = add_buy_amount*add_buy_unit_cost
    # 补仓后总投入股票成本 = 现数量 * 现成本单价 + 新数量 * 新成本单价
    new_stock_cost = current_amount * current_unit_cost + buy_stock_cost
    # 补仓后总股票数量 = 现数量 + 新数量
    new_stock_amount = current_amount + add_buy_amount
    # 补仓后新成本价 = 补仓后总投入股票成本 / 补仓后总股票数量
    new_stock_unit_cost = new_stock_cost/new_stock_amount
    # 补仓后新市值 = 新成本单价 * 总股票数量
    new_stock_value = add_buy_unit_cost * new_stock_amount
    # 补仓后跌幅 = （补仓后新市值-补仓后总投入股票成本)/补仓后总投入股票成本
    value_diff_cost = new_stock_value-new_stock_cost
    stock_rate = value_diff_cost/new_stock_cost*100

    print("补仓买入成本: %.2f" % (buy_stock_cost))
    print("补仓后新市值: %.2f,总买入成本: %.2f, 新成本单价: %.2f,新涨跌幅: %.2f,新盈亏额: %.2f " % 
    (new_stock_value, new_stock_cost, new_stock_unit_cost,stock_rate,value_diff_cost))

# 2021.07.28 预计算补仓后成本价
calc_stock_new_cost(2600,53.3)
