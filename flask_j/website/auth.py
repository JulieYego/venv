from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    # return render_template('login.html')
    return '<h1>Login</h1>'


@auth.route("/register")
def register():
    # return render_template('register.html')
    return '<h1>Register</h1>'


@auth.route("/logout")
def logout():
    # return render_template('register.html')
    return '<h1>Logout</h1>'
