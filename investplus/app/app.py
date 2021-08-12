
"""
@author: Javier Escobar Cerezo and Juan Diego Berraquero Romero
"""

from flask import Flask, render_template, session
from flask import request, redirect, url_for
from pickleshare import *
import apimarket
import scrapercrypto
import scrapperinfobolsa
import os

app = Flask(__name__)
# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get("PORT", 5000))

app.secret_key = '1234'
users = PickleShareDB('~/users')


def web(route):
    if 'history' not in session:
        session['history'] = []
    session['history'] = [route] + session['history']


def get_user():
    username = session['username'] if 'username' in session else None
    history = session['history'][0:3] if 'history' in session else []
    return username, history


@app.route('/')
def root():
    web('index')
    user, history = get_user()
    #apimarket.request_data()
    return render_template('index.html', user=user, history=history)

@app.route('/crypto')
def crypto():
    web('crypto')
    user, history = get_user()
    data = scrapercrypto.request_data()
    return render_template('crypto.html', user=user, history=history, data=data)

@app.route('/divisas')
def bolsa():
    web('divisas')
    user, history = get_user()
    data = scrapperinfobolsa.request_data()
    return render_template('divisas.html', user=user, history=history, data=data)


@app.route('/market')
def market():
    web('market')
    user, history = get_user()
    data = apimarket.request_data()
    return render_template('market.html', user=user, history=history, data=data)



@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        session['username'] = username
        session['history'] = []
    return redirect(url_for('root'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('history', None)
    return redirect(url_for('root'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    web('register')
    user, history = get_user()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        users[username] = {"email": email, "password": password}
        session['username'] = username
        session['history'] = []
        return redirect(url_for('root'))
    return render_template('register.html', user=user, history=history)


@app.route('/mod-user', methods=['GET', 'POST'])
def mod_user():
    web('register')
    user, history = get_user()
    userInfo = users[user]
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = {"email": userInfo["email"], "password": password}
        session['username'] = username
        return redirect(url_for('user_info'))
    return render_template(
        'mod_user.html',
        username=user,
        email=userInfo["email"],
        password=userInfo["password"],
        history=history)


@app.route('/user-info')
def user_info():
    web('user-info')
    user, history = get_user()
    userInfo = users[user]
    return render_template(
        'user_info.html',
        user=user,
        email=userInfo["email"],
        history=history)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)
