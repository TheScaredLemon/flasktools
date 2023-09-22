import os
from flask import Flask, render_template, request, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

# random secret key
secret_key = os.urandom(24)

app.secret_key = secret_key

@app.route('/')
def start_survey():
    # Initialize session(empty list)
    session['responses'] = []
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/questions/<int:question_id>', methods=['GET'])
def show_question(question_id):
    # ... (Add the show_question route here)

@app.route('/answer', methods=['POST'])
def handle_answer():
    # ... (Add the handle_answer route here)

if __name__ == '__main__':
    app.run(debug=True)

