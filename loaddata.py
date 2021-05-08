# Loads data from MoneyControl
# Passengers - Frosthack
# Author: Pratiksha Jain

import time
import numpy as np
import pandas as pd
import investpy

'''
#df = investpy.get_stock_historical_data(stock='HDBK',
                                        country='India',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')
#print(df.head())


#info = investpy.get_stock_company_profile(stock='HDBK',
                                        country='India', language='english')

#print(info)
#df2 = investpy.get_stock_recent_data(stock='HDBK',
                                        country='India',
                                        interval='Weekly')

print(df2)

data = investpy.get_stock_financial_summary(stock='HDBK',
                                        country='India', summary_type='income_statement', period='annual')
data2 = investpy.get_stock_financial_summary(stock='HDBK',
                                        country='India', summary_type='cash_flow_statement', period='annual')
data3 = investpy.get_stock_financial_summary(stock='HDBK',
                                        country='India', summary_type='balance_sheet', period='quarterly')                                                                                
print(data)
print(data2)
print(data3)
'''


def loadHistoricalData(stock):
    df = investpy.get_stock_historical_data(stock=stock,
                                        country='India',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')

    df = df.drop('Currency', axis=1)
    df.to_csv('stock_details/%s.csv'%(stock))

def loadStocks(specific_stocks=[], max_stocks=20):
    stocks = investpy.stocks.get_stocks_list(country='India')
    stocks = [i for i in stocks if not i in specific_stocks]
    stocks = stocks[:(max_stocks-len(specific_stocks))]
    stocks_req = stocks+specific_stocks

    for stock in stocks_req:
        loadHistoricalData(stock)
        print(stock, ' done')
    
    return stocks_req

stocks = loadStocks()


