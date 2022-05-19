from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return{"Root Message":"MOSHI MOSHI!"}


if __name__ == '__main__':
    app.run()
