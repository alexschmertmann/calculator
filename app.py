from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display ="", pageTitle = 'MyCalculator')

@app.route('/Calculate', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = request.form
        A = float(form['LoanAmt'])
        n = float(form['NumYears'])*12
        i = float(form['Interest']) / 12
        D = ((( 1 + i ) **n ) - 1 ) / ( i * ( 1+ i) **n)
        LoanPmt = A / D
        return render_template('index.html', display= LoanPmt, pageTitle='MyCalculator')

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
