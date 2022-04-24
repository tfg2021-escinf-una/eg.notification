from flask import Flask
from flask_mail import Mail, Message
import os
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['email']
app.config['MAIL_PASSWORD'] = os.environ['password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/notify")
def notification():
    msg = Message('Notification microservice test', sender =   'tfg2021.escinf.una@gmail.com', recipients = ['edlobo98@gmail.com'])
    msg.body = "This is just a simple notification for testing purposes"
    mail.send(msg)
    return "Message sent!", 200

@app.route("/liveness")
def liveness():
    return "ok", 200

@app.route("/readiness")
def readiness():
    return "ok", 200

if __name__ == '__main__':
   app.run(debug = True)