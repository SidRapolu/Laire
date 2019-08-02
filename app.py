from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
<<<<<<< HEAD
     #return render_template('construction.html')
      return render_template('home.html')
=======
     return render_template('construction.html')
    # return render_template('home.html')
>>>>>>> fb23f35ce7c5800a1e9ed589f8cb6d02ea66dc54

@app.route("/github")
def github():
    return redirect("https://github.com/pranavaddepalli/Laire", code=302)

if __name__ == '__main__':
    app.run(debug=True)
