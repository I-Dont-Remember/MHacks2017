from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.messaging_response import Message, MessagingResponse
import logging as log
import text

app = Flask(__name__)
db = SQLAlchemy(app)

# Putting all this crap in the same file because I've been burned too many times trying to get the distributed nice looking structure to work
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    password = db.Column(db.String(150))

    def __repr__(self):
        return '<User %r>' %(self.username)


@app.route('/sms', methods=['POST'])
def sms_handler():
    body = request.form['Body']
    from_num = request.form['From']
    log.debug('Text from: %s says: (%s)' % (from_num, body))
    new_body = text.get_response_text(body)

    resp = MessagingResponse()
    resp.message(new_body)
    return str(resp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
