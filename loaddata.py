# Loads data from MoneyControl
# Passengers - Frosthack
# Author: Pratiksha Jain

import time
import numpy as np
import pandas as pd
import investpy


companies_list = []
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

#print(df2)
'''
data = investpy.get_stock_financial_summary(stock='HDBK',
                                        country='India', summary_type='income_statement', period='annual')
data2 = investpy.get_stock_financial_summary(stock='HDBK',
                                        country='India', summary_type='cash_flow_statement', period='annual')
data3 = investpy.get_stock_financial_summary(stock='HDBK',
                                        country='India', summary_type='balance_sheet', period='quarterly')                                                                                
print(data)
print(data2)
print(data3)



def loadStocks():
    stocks = investpy.stocks.get_stocks(country='India').head(10)
    return stocks_dict

def loadHistoricalData(stock):
    pass




