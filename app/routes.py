from app import app
from flask import render_template
from app.forms import RegisterForm

@app.route('/')
def index():
    my_name = 'Patrick'
    my_city = 'American Canyon'
    foods = ['pizza', 'italian food', 'french fries', 'donuts', 'mexican food', 'fruit']
    person = {
        'name': 'Ferris Bueller',
        'age': 18,
        'best_friend': 'Cameron'
    }
    return render_template('index.html', name=my_name, city=my_city, foods=foods, person=person)


@app.route('/name')
def name():
    my_name = 'Patrick'

    return render_template('name.html', name=my_name)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
