<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, render_template, request, redirect
from flask_dropzone import Dropzone
>>>>>>> bd0f5c5214ae0be8624de9b262db073693381f73
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('construction.html')
    # return render_template('home.html')

<<<<<<< HEAD
=======
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

>>>>>>> bd0f5c5214ae0be8624de9b262db073693381f73
if __name__ == '__main__':
    app.run(debug=True)
