from flask import Flask,redirect,request,render_template,session
app = Flask(__name__)

# @app.route('/')
app.secret_key = 'Keyboard cat'



app.run(debug=True)