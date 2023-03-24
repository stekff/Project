from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index(): return render_template("index.html")


@app.route('/naprav')
def naprav(): return render_template("naprav.html")


@app.route('/japan')
def japan(): return render_template("japan.html")


@app.route('/france')
def france(): return render_template("france.html")


@app.route('/italia')
def italia(): return render_template("italia.html")


if __name__ == "__main__":
    app.run(debug=True)
