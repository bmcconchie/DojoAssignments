from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'cattail'

@app.route('/')
def index():   
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print request.form['name']
    return redirect('/')
    # return render_template('process.html')

app.run(debug=True)
