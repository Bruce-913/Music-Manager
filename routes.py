from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/sign-in')

def sign_in():
    return render_template('sign-in.html')