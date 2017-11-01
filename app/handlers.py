from flask import Blueprint, render_template, current_app, request, redirect, url_for
from app.models.message import Message

site = Blueprint('site', __name__)

@site.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        form = {'messageTitle': '', 'messageText': ''}
    else:
        valid=validate_message_data(request.form)
        if valid:
            title=request.form.data['messageTitle']
            text=request.form.data['messageText']
            #Add new message
            current_app.messageStore.add_message(Message(title,text))
            return redirect(url_for('site.home_page'))
        form=request.form
    messages=current_app.messageStore.get_messages()
    return render_template('home.html', form=form, messages=sorted(messages.items()))

def validate_message_data(form):
    form.data = {}
    form.errors = {}
    if len(form['messageTitle'].strip()) == 0:
        form.errors['messageTitle'] = 'Title can not be blank.'
    else:
        form.data['messageTitle'] = form['messageTitle']

    form.data['messageText'] = form['messageText']

    return len(form.errors) == 0

@site.route('/login')
def login_page():
    return render_template('login.html')

@site.route('/message/<int:message_id>')
def message_page(message_id):
    message = current_app.messageStore.get_message(message_id)
    return render_template('message.html', message=message)
