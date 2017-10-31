from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/')
def home_page():
    return render_template('home.html')

@site.route('/login')
def login_page():
    return render_template('login.html')
