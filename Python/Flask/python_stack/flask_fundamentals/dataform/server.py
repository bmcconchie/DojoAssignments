from flask import Flask,render_template,request,redirect,session,flash
app = Flask(__name__)
app.secret_key = 'Farn'

@app.route ('/')
def index():
    
    return render_template('index.html')

@app.route ('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
         
    # else:
    #     flash("Success! Your name is {}".format(request.form['name']))
    elif len(request.form['comment']) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) >= 120:
        flash("Comments cannot be longer than 120 char.!") 
        return redirect('/')
    else:
        flash("Success!")
    
    return render_template('result.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])


app.run(debug = True)
