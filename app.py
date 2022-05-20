from flask import Flask, render_template
import os
import pandas as pd

app = Flask(__name__)

#this is accomplished with nginx so comment out if published
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/<post>")
def post_route(post):
    path = "./data"
    sub = "/"
    dbname = post
    dbpath = path + sub + dbname
    dbfile = os.listdir(dbpath)
    return pd.read_csv(dbpath + sub + dbfile[0]).to_json()


if __name__ == '__main__':
    app.run()
