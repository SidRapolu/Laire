from flask import Flask, render_template

app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/hbclassification", methods=["GET"])
def hbclassification():
    return render_template('hbclassification.html')






if __name__ == "__main__":
    app.run(debug=True)
