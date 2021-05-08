from flask import Flask, render_template, request
from loaddata import loadStock
from Stockpred import generateTable
import warnings

app = Flask(__name__)
warnings.filterwarnings("ignore")

portfolio = []
headings = ['stock_name', 'quantity', 'buy_price', 'currentprice', 'predicted_high', 'predicted_low', 'currentreturn', 'predictedreturn', 'decision']

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      stock = request.form['impath']
      stock_loadstatus = loadStock(stock)
      if stock_loadstatus == 0:
         return render_template("error.html")
      else:
         table = generateTable(stock)
         headings = table.columns
         data = table.values.tolist()


         return render_template("result.html",stock=stock, headings=headings, data=data)

@app.route('/add')
def addStock():
   return render_template('add.html')

@app.route("/portfolio", methods=['GET', 'POST'])
def add():
   global portfolio
   if request.method == 'POST':
      stock_name = request.form['stockname']
      quantity = int(request.form['quantity'])
      buy_price = int(request.form['buy_price'])
      
      stock_loadstatus = loadStock(stock_name)
      if stock_loadstatus == 0:
         return render_template("error.html")
      else:
         
         currentprice = 10
         table = generateTable(stock_name, dates=["2021-5-10"])
         predicted_high = 10
         predicted_low = 10
         currentreturn = (currentprice - buy_price) * quantity
         predictedreturn = (predicted_high - buy_price) * quantity
         
         if predictedreturn > 0:
            decision = "SELL"
         else:
            decision = "KEEP"

         portfolio.append([stock_name, quantity, buy_price, currentprice, predicted_high, predicted_low, currentreturn, predictedreturn, decision])
   
   return render_template('portfolio.html', portfolio=portfolio, headings=headings) 




if __name__ == '__main__':
   app.run(debug = True)