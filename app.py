from flask import Flask, render_template, request, session, url_for, redirect, flash
from os import urandom

import sqlite3
app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
