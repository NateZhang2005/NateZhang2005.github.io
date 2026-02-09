import os
from cs50 import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, url_for, request, session, jsonify
from flask_session import Session
from helpers import apology, login_required

# Much source code kept from Finance pset
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
possibleDB = SQL("sqlite:///possible.db")

# Database source for possible guesses is from: https://gist.github.com/cfreshman/40608e78e83eb4e1d60b285eb7e9732f
# Database source for possible solutions is from: https://github.com/steve-kasica/wordle-words/blob/master/wordle.csv

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/makerselect", methods=['POST'])
def makerSelect():
    return render_template("makerselect.html")

@app.route("/maker", methods=['POST'])
def maker():
    # redundant, but meant to store these variables and transfer them from the form on makerselect.html to maker.html
    customWord = request.form.get("customWord")
    guessCount = request.form.get("guessCount")
    realWord = request.form.get("realWord")
    real = realWord == "yes"
    return render_template("maker.html", customWord=customWord, guessCount=guessCount, real=real)


@app.route('/check', methods=['POST'])
def check():
    try:
        # gets the word from original source (in this case always maker.html)
        data = request.get_json()
        currentWord = data['word']

        wordExists = wordInDatabase(currentWord)

        return jsonify(result=wordExists)
    except Exception as e:
        return jsonify(result=False, error=str(e)), 400

def wordInDatabase(word):
    try:
        # establish connection to database
        conn = sqlite3.connect('possible.db')
        cursor = conn.cursor()

        # check if word appears in possible.db
        cursor.execute("SELECT word FROM possible WHERE word = ?", (word,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return True
        else:
            return False
    except Exception as e:
        return jsonify(result=False, error=str(e)), 400
