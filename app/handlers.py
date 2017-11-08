from flask import Blueprint, render_template, current_app, request, redirect, url_for
from app.models.message import Message
from app.models.database import Database
from flask_login import UserMixin
from app.models.adminStuff import adminCommands
from app.models.user import User

site = Blueprint('site', __name__)

@site.route('/', methods=['GET', 'POST'])
def home_page():
    db = Database()
    if request.method == 'GET':
        form = {'messageTitle': '', 'messageText': ''}
    else:
        valid=validate_message_data(request.form)
        if valid:
            title=request.form.data['messageTitle']
            text=request.form.data['messageText']
            #Add new message
            db.add_message(Message(title,text))
            return redirect(url_for('site.home_page'))
        form=request.form
    messages=db.get_messages()
    return render_template('home.html', form=form, messages=sorted(messages.items()))

@site.route('/reset')
def reset():
    adminCommands.resetEverything()
    return redirect(url_for('site.home_page'))

def validate_message_data(form):
    form.data = {}
    form.errors = {}
    #add maximum lenght
    if len(form['messageTitle'].strip()) == 0:
        form.errors['messageTitle'] = 'Title can not be blank.'
    else:
        form.data['messageTitle'] = form['messageTitle']

    form.data['messageText'] = form['messageText']

    return len(form.errors) == 0

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
    user=User()
    if request.method == 'GET':
        form = {'username'}
    else:
        valid=validate_login_data(request.form)
        if valid:
            if(user.loginOrSignUp(request.form)):
                return redirect(url_for('site.home_page'))
        form=request.form
    return render_template('login.html', form=form)

@site.route('/message/<int:message_id>')
def message_page(message_id):
    #message = current_app.messageStore.get_message(message_id)
    return render_template('message.html', message=message)
