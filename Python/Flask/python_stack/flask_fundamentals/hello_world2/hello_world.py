from flask import Flask,redirect,request,render_template,session
app = Flask(__name__)


app.secret_key = 'Keyboard cat'
@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)