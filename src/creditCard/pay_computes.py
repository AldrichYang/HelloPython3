def need_to_pay(yearmonth, my, pf, zs, ms=0):
    unpay = my + pf + zs + ms
    # format数字格式化
    print(yearmonth + ' credit card cost: ', format(unpay, '0.2f'))
    return unpay
