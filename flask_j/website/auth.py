# store routes for authentication
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', ship='Wilmon')


@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # check if information is valid
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match', category='error')
        elif len(password) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            # add user to db
            flash('Account created!', category='success')

    return render_template('register.html')


@auth.route("/logout")
def logout():
    # return render_template('register.html')
    return '<h1>Logout</h1>'
