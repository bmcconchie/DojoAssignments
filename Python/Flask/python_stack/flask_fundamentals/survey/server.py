from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'cat'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    return render_template('result.html', name = request.form['name'], location = request.form['location'], language = request.form['language'])


app.run(debug = True)