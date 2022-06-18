import datetime
from flask import Flask, render_template
from pymongo import MongoClient
from common.utils import InitDBConnection as conn


app = Flask(__name__)

client = MongoClient(conn.mongodb_connection())
print(client.ODS.entries.find({}))
app.db = client.ODS
class test:
    def __init__(self, fname, lname, mname):
        self.fname = fname
        self.lname = lname
        self.mname = mname


@app.route("/")
def hello_world():
    return render_template("firstpage.html")


@app.route("/page")
def page():
    return render_template("secondpage.html")


@app.route("/pythonobj")
def obj():
    testing = test("Omolewa", "Adaramola", "Bukola")
    return render_template("thirdpage.html", testing=testing)


def main():
    app.run(host='localhost', port=5000, debug=True)


if __name__ == '__main__':
    main()
