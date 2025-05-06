from flask import Flask, render_template, request
import pandas as pd
from nlp_processor import process_query
from data_handler import load_faqs, save_feedback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question']
    answer, feedback = process_query(user_question)
    return render_template('index.html', answer=answer, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
