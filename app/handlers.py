from flask import Blueprint, render_template, current_app

site = Blueprint('site', __name__)

@site.route('/')
def home_page():
    messages=current_app.messageStore.get_messages()
    return render_template('home.html', messages=sorted(messages.items()))

@site.route('/login')
def login_page():
    return render_template('login.html')
