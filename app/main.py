from flask import Flask, request, render_template, url_for, redirect, g, session
from flask_login import LoginManager
from flask_login import LoginManager, UserMixin, login_required
from flask_login import login_user, logout_user, current_user
from twilio.twiml.messaging_response import Message, MessagingResponse
import logging as log
import text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A super secret key yahhhh!!!'

@app.route('/sms', methods=['POST'])
def sms_handler():
    body = request.form['Body']
    from_num = request.form['From']
    log.debug('Text from: %s says: (%s)' % (from_num, body))
    new_body = text.get_response_text(body)

    resp = MessagingResponse()
    resp.message(new_body)
    return str(resp)


@app.route('/user/<username>')
def user(username):
    print('in user function')
    if username != 'admin':
        return '<h1>You are not authorized to access that page</h1>'

    user = {
        'username': 'admin',
        'name': 'Kevin',
        'phone': '+1334iiiii',
        'friend1': '+13545465646',
        'friend2': '+171504354'
    }
    print('rendering template for account')
    return render_template('account.html',
                            current_user=user)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    json = request.get_json()
    log.debug('login json: %s' %(json))
    username = json['username']
    password = json['password']

    if username != 'admin' or password != 'password':
        return 'Denied', 401

    return redirect(request.args.get('next') or url_for('user', username=username))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
