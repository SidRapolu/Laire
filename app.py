from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
     return render_template('construction.html')
    # return render_template('home.html')

@app.route("/hbc")
def hbc():
    return render_template('hbc.html')

@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('hbc.html')

@app.route("/github")
def github():
    return redirect("https://github.com/pranavaddepalli/Laire", code=302)

if __name__ == '__main__':
    app.run(debug=True)
