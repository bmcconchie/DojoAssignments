from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = 'cat'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html', gold = session['gold'])

@app.route('/process', methods=['POST'])
def process():
    if request.form['building'] == 'cave':
        session['gold'] += 5
    if request.form['building'] == 'house':
        session['gold'] += 1000
    if request.form['building'] == 'castle':
        session['gold'] += 10000    
    return redirect('/')
    
app.run(debug=True)
