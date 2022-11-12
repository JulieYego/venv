# store routes for authentication
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    # return render_template('login.html')
    return render_template('login.html', ship='Wilmon')


@auth.route("/register")
def register():
    # return render_template('register.html')
    return render_template('register.html')


@auth.route("/logout")
def logout():
    # return render_template('register.html')
    return '<h1>Logout</h1>'
