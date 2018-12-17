from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Archit'}
    posts = [
        {
            'author': {'username': 'Kashyap'},
            'body': 'Back to college'
        },
        {
            'author': {'username': 'Shubham'},
            'body': 'Trying to learn web development'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
