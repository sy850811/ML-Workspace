#this is a basic sceleton on a flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this Flask course"

if __name__=="__main__":
    app.run()