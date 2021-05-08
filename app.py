from flask import Flask, render_template, request
app = Flask(__name__)


headings = ("Date","Predicted Price")
data= (
   ("10/12/2020", "235"),
   ("11/12/2020", "240"),
   ("12/12/2020", "245")

)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['impath']
      return render_template("result.html",result = result, headings=headings, data=data)

if __name__ == '__main__':
   app.run(debug = True)