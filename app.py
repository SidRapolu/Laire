from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route("/")
def home():
     #return render_template('construction.html')
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

app.config.update(dict(
    MAIL_SERVER = 'smtp.domain.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'hello@laire.org',
    MAIL_PASSWORD = 'qwertyuiopA123!'
))
mail = Mail(app)

@app.route('/contact_email', methods=['POST'])
def contact_email():
    print(request.form['Name'])
    msg = Message('Contact From Website', sender='hello@laire.org', recipients=['info.laire@gmail.com'])
    msg.body = 'Name: ' + request.form['Name'] + '\n' + 'Subject: ' + request.form['Subject'] + '\n' + 'Message: ' + request.form['Message'] + '\n' + 'Email: ' + request.form['Email'] #Customize based on user input

    mail.send(msg)
    return redirect("/#contact")

if __name__ == '__main__':
    app.run(debug=True)
