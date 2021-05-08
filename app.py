from flask import Flask, render_template, request
from loaddata import loadStock
from Stockpred import generateTable
import warnings

app = Flask(__name__)
warnings.filterwarnings("ignore")

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

if __name__ == '__main__':
   app.run(debug = True)