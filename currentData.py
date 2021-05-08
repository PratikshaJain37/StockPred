"""
cuurentData.py - Gets realtime data of stock

@authors: Pratiksha Jain, Shubham Saurav
"""
# --------------------------------- #

# Imports needed

import requests
from bs4 import BeautifulSoup

# --------------------------------- #

# Write MoneyControl Stock URL here:
#URL = 'https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI'
#URL = 'https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/vodafoneidealimited/IC8'

def getURL(stock):
    BASEURL = "https://in.investing.com/equities/"
    #pageResponse = requests.get(BASEURL)

    # Returns site in form of HTML tags   
    #bsParser = BeautifulSoup(pageResponse.content, 'html.parser')

    # Finding title of stock
    #name = bsParser.find_all('a')


    return BASEURL


def getCurrentPrice(stock):
    URL = getURL(stock)

    # Request data from URL, by 'GET' method
    #pageResponse = requests.get(URL)

    # Returns site in form of HTML tags   
    #bsParser = BeautifulSoup(pageResponse.content, 'html.parser')

    # Finding title of stock
    #price = bsParser.find('bdo', class_='last-price-value js-streamable-element').text

    #print(price)
    return 10

# --------------------------------- #