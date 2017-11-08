from flask import current_app
from flask_login import UserMixin
from app.models.database import Database
from passlib.apps import custom_app_context as pwd_context

class User(UserMixin):
    def __init__(self,):
        self.active = False
        self.is_admin = False

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active


    def loginOrSignUp(self,form):
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
            form=form
            #add login management
            return True
        if (hashedPass):
            if(pwd_context.verify(password,hashedPass)):
                #login
                form.errors['username'] = 'login succesfull'
                self.username = username
                #add login management
                return True
            else:
                form.errors['password'] = 'Wrong password'
        else:
            form.errors['noUser'] = 'No user found please press sign up to add user'
        return False
