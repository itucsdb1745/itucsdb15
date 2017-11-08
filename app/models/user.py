from flask import current_app
from flask_login import UserMixin
from app.models.database import Database
from passlib.apps import custom_app_context as pwd_context
from flask_login import LoginManager, login_user

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.active = True
        self.is_admin = False

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active

def loginOrSignUp(form):
    db = Database()
    username=form.data['username']
    password=form.data['pass']
    #get hashed pass from db
    dbashedPass=db.get_user_pass(username)
    if(dbashedPass):
        hashedPass=dbashedPass[0][0]
    else:
        hashedPass=None
    if (form['addUser']=='true'):
        hashedPass=pwd_context.encrypt(password)
        result=db.add_user(username,hashedPass);
        #login user
        user = get_user(username)
        login_user(user)
        return True
    if (hashedPass):
        if(pwd_context.verify(password,hashedPass)):
            #login
            user = get_user(username)
            login_user(user)
            form.errors['username'] = 'login succesfull'
            return True
        else:
            form.errors['password'] = 'Wrong password'
    else:
        form.errors['noUser'] = 'No user found please press sign up to add user'
    return False

def get_user(username):
    db = Database()
    userArray = db.get_user(username)
    if len(userArray)==1:
        user=User(username)
        #add admin check here
    return user
