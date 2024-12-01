#this is a basic sceleton on a flask app
from flask import \
    render_template  # this is used to write html in different file and refer to it through one of the functions from this file
from flask import Flask

from flask import request

from flask import redirect,url_for

app = Flask(__name__) # this serves as an WSGI that allows communication between our app and the webserver sucht hat when a request comes to a webapplication for example 0.0.0.0:5000 it can be directed to the application and the application can respond through the web server to the user as well.

#jinja 2 is web template engine. It combines web templates to data source like ML MODEL or SQL DB, CSV


@app.route("/",methods=['GET'])
def welcome():
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def custom_welcome():
    if request.method == 'POST':
        user_name = request.form['name']
        return f"Welcome {user_name} !"
    return render_template("form.html")

@app.route("/result",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form['name']
        return f"Welcome {user_name} !"
    return render_template("form.html")


@app.route('/success/<int:score>')
def success(score):
    return render_template("result.html",results = score)

@app.route('/results/<int:score>')
def results(score):
    res = {"score": score,"result":"Passes" if score >50 else "Failed"}
    return render_template("result1.html",results = res)

@app.route('/FinalResult',methods=['GET','POST'])
def FinalResult():
    if request.method == 'POST':
        subject1 = float(request.form['science'])
        subject2 = float(request.form['maths'])
        subject3 = float(request.form['c'])
        subject4 = float(request.form['datascience'])
        averageScore = (subject1+subject2+subject3+subject4)/4
        print(f"/results/{averageScore}")
        return redirect(url_for('results',score=int(averageScore)))    
    return render_template('getresult.html')

if __name__=="__main__":
    app.run(debug=True) # add debug=True to see changes as you make them during development otherwise to see changes without this parameter we will have to restart he application again and again