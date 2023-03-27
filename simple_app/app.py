from flask import Flask, render_template, request
from power import get_powers

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/power', methods=['POST'])
def search():
    query = request.form.get('query')
    results = get_powers(query)
    return render_template('results.html', results=results)
