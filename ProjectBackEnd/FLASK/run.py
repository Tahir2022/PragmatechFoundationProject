from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# app/routes
from app.routes import *

# admin/routes
from admin.routes import *

if __name__ == "__main__":
    # db.create_all()
    app.run(debug = True)