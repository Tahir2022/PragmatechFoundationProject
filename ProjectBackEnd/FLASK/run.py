from flask import Flask, render_template, url_for

app = Flask(__name__)

# app/routes
from app.routes import *

# admin/routes
from admin.routes import *

if __name__ == "__main__":
    app.run(debug = True)