from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle = 'MyCalculator')

@app.route('/Alex')
def Alex():
    return render_template('Alex.html', pageTitle = 'Alex')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
