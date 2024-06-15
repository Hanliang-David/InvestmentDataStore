# 找出ROE大于15 的相关市场股票信息，ROE为年度净资产收益率
from futu import *
import time

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
simple_filter = SimpleFilter()
simple_filter.filter_min = 0.1
simple_filter.filter_max = 10000
simple_filter.stock_field = StockField.CUR_PRICE
simple_filter.is_no_filter = False
simple_filter.sort = SortDir.ASCEND

financial_filter = FinancialFilter()
financial_filter.filter_min = 14.99
financial_filter.filter_max = 150
financial_filter.stock_field = StockField.RETURN_ON_EQUITY_RATE
financial_filter.is_no_filter = False
financial_filter.sort = SortDir.NONE
financial_filter.quarter = FinancialQuarter.ANNUAL

nBegin = 0
last_page = False
ret_list = list()
while not last_page:
    nBegin += len(ret_list)
    ret, ls = quote_ctx.get_stock_filter(market=Market.HK, filter_list=[simple_filter, financial_filter], begin=nBegin)  # 对香港市场的股票做简单、财务和指标筛选
    if ret == RET_OK:
        last_page, all_count, ret_list = ls
        print('all count = ', all_count)
        for item in ret_list:
            # print(item.stock_code)  # 取股票代码
            # print(item.stock_name)  # 取股票名称
            # print(item[simple_filter])   # 取 simple_filter 对应的变量值
            # print(item[financial_filter])   # 取 financial_filter 对应的变量值
            # print(item[custom_filter])  # 获取 custom_filter 的数值
            print(item.stock_code, item.stock_name, item[simple_filter], item[financial_filter])
    else:
        print('error: ', ls)
    time.sleep(3)  # 加入时间间隔，避免触发限频

quote_ctx.close()  # 结束后记得关闭当条连接，防止连接条数用尽
