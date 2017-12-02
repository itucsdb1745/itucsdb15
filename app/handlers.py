from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from app.models.message import Message
from app.models.database import Database
from flask_login import UserMixin
from app.models.adminStuff import adminCommands
from app.models.user import loginOrSignUp
from flask_login import LoginManager
from app.forms import AddMessageForm, LoginForm

site = Blueprint('site', __name__)

@site.route('/', methods=['GET', 'POST'])
def home_page():
    db = Database()
    form = AddMessageForm()
    print (form.data)
    if form.validate_on_submit():
        title = form.data['title']
        text = form.data['text']
        db.add_message(Message(title,text))
        flash('message added')
        return redirect(url_for('site.home_page'))
    messages=db.get_messages()
    return render_template('home.html', form=form, messages=messages)

@site.route('/reset')
def reset():
    adminCommands.resetEverything()
    return redirect(url_for('site.home_page'))

@site.route('/login', methods=['GET', 'POST'])
def login_page():
    db = Database()
    form = LoginForm()
    if form.validate_on_submit() and loginOrSignUp(form):
        flash('login succesfull')
        return redirect(url_for('site.home_page'))
    else:
        print ('fail to sign in')
        return render_template('login.html', form=form)

@site.route('/message/<int:message_id>')
def message_page(message_id):
    db=Database()
    message = db.get_message(message_id)
    return render_template('message.html', message=message)
