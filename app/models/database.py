import psycopg2 as dbapi2
from flask import current_app
from app.models.message import Message

class Database:
    def __init__(self):
        self.last_m_id = 0

    def add_message(self, message):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO MESSAGES (TITLE, CONTENT) VALUES (%s, %s)"
            cursor.execute(query, (message.title, message.text))
            connection.commit()
            self.last_m_id = cursor.lastrowid

    def delete_message(self, messageId):
        del self.messages[messageId]

    def get_message(self, messageId):
        return self.messages[messageId]

    def get_messages(self):
        return {}

    def get_user_pass(self, username):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT PASS FROM USERS WHERE USERNAME = %s"
            cursor.execute(query, (username,))
            return cursor.fetchall()

    def get_user(self, username):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM USERS WHERE USERNAME = %s"
            cursor.execute(query, (username,))
            return cursor.fetchall()

    def add_user(self,username,password):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            print (password)
            cursor = connection.cursor()
            query = "SELECT PASS FROM USERS WHERE USERNAME = %s"
            cursor.execute(query, (username,))
            if(cursor.fetchall()):
                return 'User already exists'
            query = "INSERT INTO USERS (USERNAME, PASS) VALUES (%s, %s)"
            cursor.execute(query, (username,password))
