from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Evaristo'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'The Avangers movie was so cool!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Beautiful day in Portland!'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)