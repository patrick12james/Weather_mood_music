from app import app
from flask import render_template

@app.route('/')
def index():
    my_name = 'Patrick'
    my_city = 'American Canyon'
    foods = ['pizza', 'italian food', 'french fries', 'donuts', 'mexican food', 'fruit']
    return render_template('index.html', name=my_name, city=my_city, foods=foods)

@app.route('/name')
def name():
    my_name = 'Patrick'
    return f'Hello {my_name}'

@app.route('/test')
def test():
    return '<h1>This is not a test!<h1>'
