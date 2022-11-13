from website import create_app
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
