from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
#     return render_template('construction.html')
     return render_template('home.html')

@app.route("/github")
def github():
    return redirect("https://github.com/pranavaddepalli/Laire", code=302)

@app.route("/pranav")
def pranav():
    return render_template('pranav.html')

@app.route("/sid")
def sid():
    return render_template('sid.html')

@app.route("/haneef")
def haneef():
    return render_template('haneef.html')

if __name__ == '__main__':
    app.run(debug=True)
