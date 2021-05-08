"""
daily_update.py - Updates data and predicts prices everytime it is run

@authors: Pratiksha Jain, Shubham Saurav
"""
# --------------------------------- #

# Imports needed

from loaddata import loadStocks
from Stockpred import generateTable, saveTable
from os import listdir
from os.path import isfile, join

# --------------------------------- #

# Edit dates as needed
dates = ["2021-5-9", "2021-5-10", "2021-5-11", "2021-5-12", "2021-5-13"]

# Edit stocks list as needed
loadStocks()

stocks_loaded = [f for f in listdir('stock_details') if isfile(join('stock_details', f))]

for stock in stocks_loaded:
    saveTable(stock, generateTable(stock, dates))
    print(stock, 'saved')

# --------------------------------- #