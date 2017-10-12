from flask import Flask, render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'cat'
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')


@app.route('/dojos/new', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    submit = request.form['submit']
    return render_template('dojos.html')
app.run(debug=True)