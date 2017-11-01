from flask import Blueprint, render_template, current_app, request, redirect, url_for
from app.models.message import Message

site = Blueprint('site', __name__)

@site.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        messages=current_app.messageStore.get_messages()
        return render_template('home.html', messages=sorted(messages.items()))
    elif request.form['messageTitle']:
        title=request.form['messageTitle']
        text=request.form['messageText']
        #Add new message
        current_app.messageStore.add_message(Message(title,text))
        return redirect(url_for('site.home_page'))
    messages=current_app.messageStore.get_messages()
    return render_template('home.html', messages=sorted(messages.items()))

@site.route('/login')
def login_page():
    return render_template('login.html')

@site.route('/message/<int:message_id>')
def message_page(message_id):
    message = current_app.messageStore.get_message(message_id)
    return render_template('message.html', message=message)
