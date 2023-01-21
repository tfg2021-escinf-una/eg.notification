from flask import Flask, request
from flask_cors import CORS
from mailjet_rest import Client
import os

app = Flask(__name__)
CORS(app)
 
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']
sender_address = os.environ['EMAIL_SENDER']
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/notify", methods=['POST'])
def notification():
    args = request.get_json()
    email_to_send = args["address"]
    subject = args["subject"]
    message = args["message"]
    data = {
        'Messages': [
            { "From": {	"Email": sender_address, "Name": "TFG - Sitio Didáctico" },
              "To": [{ "Email": email_to_send, "Name": "You" }],
              "Subject": subject,
              "TextPart": "Greetings from Mailjet!",
              "HTMLPart": f"<h4>{message}</h4><br />Este es un mensaje autogenerado por nuestro sitio utilizando MailJet."
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result.json()

@app.route("/liveness")
def liveness():
    return "ok", 200

@app.route("/readiness")
def readiness():
    return "ok", 200

if __name__ == '__main__':
   app.run(port=5000, debug = True)