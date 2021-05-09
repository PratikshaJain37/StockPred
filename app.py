"""
Stockpred.py - Predicting stock price using ML models on historical data

@authors: Shubham Saurav, Pratiksha Jain
"""
# --------------------------------- #

# Imports needed
import pandas as pd
from flask import Flask, render_template, request
from loaddata import loadStock
from Stockpred import generateTable, saveTable
from currentData import getCurrentPrice

import warnings
warnings.filterwarnings("ignore")

# --------------------------------- #

app = Flask(__name__)

# portfolio is the main list which stores the values of headings
headings = ['stock_name', 'quantity', 'buy_price', 'currentprice', 'predicted_high', 'predicted_low', 'currentreturn', 'predictedreturn', 'decision']
portfolio = []
current_date = ["2021-5-10"]
dates = ["2021-5-9", "2021-5-10", "2021-5-11", "2021-5-12", "2021-5-13"]


# get stock-data_predicted
stock_pred = pd.read_csv("stock_pred.csv", index_col=0)

# Views of app

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   global stock_pred
   if request.method == 'POST':
      stock = request.form['impath']
      stock_loadstatus = loadStock(stock)
      
      if stock_loadstatus == 0:
         return render_template("error.html")
      if stock_loadstatus == 2:
         saveTable(stock, generateTable(stock, dates))
         stock_pred = pd.read_csv("stock_pred.csv", index_col=0)
      
      stock_table = stock_pred[stock_pred.Stock_Name == stock]
      stock_table_dates = pd.DataFrame()
      for date in dates:
         stock_table_dates = pd.concat([stock_table_dates,stock_table[stock_table.Date == date]], ignore_index=True)
      
      stock_table = stock_table_dates

      stock_table.drop(['Stock_Name'], axis=1, inplace=True)

      headings = ['Date','Pred_Low','Pred_High','Pred_Difference','Pred_Difference_Percentage']

      data = stock_table.values.tolist()

      return render_template("result.html",stock=stock, headings=headings, data=data)

@app.route('/add')
def addStock():
   return render_template('add.html')

@app.route("/portfolio", methods=['GET', 'POST'])
def add():
   global portfolio, dates, stock_pred
   if request.method == 'POST':
      stock_name = request.form['stockname']
      quantity = int(request.form['quantity'])
      buy_price = int(request.form['buy_price'])
      
      stock_loadstatus = loadStock(stock_name)
      if stock_loadstatus == 0:
         return render_template("error.html")
      if stock_loadstatus == 2:
         saveTable(stock, generateTable(stock_name, dates))
         stock_pred = pd.read_csv("stock_pred.csv", index_col=0)
         
      currentprice = getCurrentPrice(stock_name)
      stock_table = stock_pred[stock_pred.Stock_Name == stock_name]
      stock_table_dates = pd.DataFrame()
      for date in dates:
         stock_table_dates = pd.concat([stock_table_dates,stock_table[stock_table.Date == date]], ignore_index=True)
      
      table = stock_table_dates
      print(stock_table_dates)

      predicted_high = table.loc[0, 'Pred_High']
      predicted_low = table.loc[0, 'Pred_Low']
      currentreturn = (currentprice - buy_price) * quantity
      predictedreturn = (predicted_high - buy_price) * quantity
      
      if currentreturn > 0:
         decision = "SELL"
      else:
         decision = "KEEP"

      portfolio.append([stock_name, quantity, buy_price, currentprice, predicted_high, predicted_low, currentreturn, predictedreturn, decision])
   
   return render_template('portfolio.html', portfolio=portfolio, headings=headings) 


# --------------------------------- #

if __name__ == '__main__':
   app.run(debug = True)

# --------------------------------- #