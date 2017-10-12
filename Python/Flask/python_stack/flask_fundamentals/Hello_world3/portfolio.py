from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/myprojects')
def projects():
    return render_template('myprojects.html')
@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')
app.run(debug=True)