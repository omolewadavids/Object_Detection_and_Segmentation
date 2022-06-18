from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("firstpage.html")


@app.route("/page")
def page():
    return render_template("secondpage.html")


def main():
    app.run(host='localhost', port=5000, debug=True)


if __name__ == '__main__':
    main()
