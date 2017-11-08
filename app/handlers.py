from flask import Blueprint, render_template, current_app, request, redirect, url_for
from app.models.message import Message
from app.models.database import Database
from flask_login import UserMixin
from app.models.adminStuff import adminCommands
from app.models.user import loginOrSignUp
from flask_login import LoginManager
from app.forms import AddMessageForm

site = Blueprint('site', __name__)

@site.route('/', methods=['GET', 'POST'])
def home_page():
    db = Database()
    form = AddMessageForm()
    if form.validate_on_submit():
        title = form.data['title']
        text = form.data['text']
        db.add_message(Message(title,text))
        return redirect(url_for('site.home_page'))
    messages=db.get_messages()
    return render_template('home.html', form=form, messages=sorted(messages.items()))

@site.route('/reset')
def reset():
    adminCommands.resetEverything()
    return redirect(url_for('site.home_page'))

def validate_login_data(form):
    form.data = {}
    form.errors = {}
    if len(form['username'].strip()) == 0:
        form.errors['username'] = 'Username can not be blank.'
    else:
        form.data['username'] = form['username']
    if len(form['pass'].strip()) == 0:
        form.errors['pass'] = 'Password can not be blank.'
    else:
        form.data['pass'] = form['pass']

    return len(form.errors) == 0

@site.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        form = {'username'}
    else:
        valid=validate_login_data(request.form)
        if valid:
            if(loginOrSignUp(request.form)):
                return redirect(url_for('site.home_page'))
        form=request.form
    return render_template('login.html', form=form)

@site.route('/message/<int:message_id>')
def message_page(message_id):
    #message = current_app.messageStore.get_message(message_id)
    return render_template('message.html', message=message)
