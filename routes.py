from flask import render_template, url_for
from __int__ import app
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Madu Micheal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date posted': 'August 2, 2022'
    },
    {
        'author': 'Chizoba Joy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date posted': 'August 3, 2022'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)
