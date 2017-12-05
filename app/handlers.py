from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from app.models.message import Message
from app.models.database import Database
from flask_login import UserMixin
from app.models.adminStuff import adminCommands
from app.models.user import loginOrSignUp
from flask_login import LoginManager
from flask_login import logout_user, current_user
from app.forms import AddMessageForm, LoginForm, AddAnswerForm
from app.models.messageAnswer import MessageAnswer

site = Blueprint('site', __name__)

@site.route('/', methods=['GET', 'POST'])
def home_page():
    db = Database()
    form = AddMessageForm()
    answerForm = AddAnswerForm()
    print(answerForm.data)
    if form.validate_on_submit():
        title = form.data['title']
        text = form.data['text']
        db.add_message(Message(title,text))
        flash('message added')
        return redirect(url_for('site.home_page'))
    if answerForm.validate_on_submit():
        text = answerForm.data['text']
        messageId=answerForm.data['messageID']
        db.add_message_answer(MessageAnswer(0,current_user.username,messageId,text))
        flash('answer added')
        return redirect(url_for('site.home_page'))
    messages=db.get_messages()
    messageAnswer={db.get_message_answer(1)}
    return render_template('home.html', answers=messageAnswer, answerForm=answerForm, form=form, messages=messages)

@site.route('/reset')
def reset():
    adminCommands.resetEverything()
    return redirect(url_for('site.home_page'))

@site.route('/dummy')
def dummy():
    adminCommands.insertDummy()
    return redirect(url_for('site.home_page'))

@site.route('/logOut')
def logout():
    logout_user()
    return redirect(url_for('site.home_page'))

@site.route('/profile')
def profile_page():
    return render_template('profile.html')

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
