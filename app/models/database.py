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
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM MESSAGES WHERE ID = %s"
            cursor.execute(query,(messageId,))
            message = cursor.fetchall()
            if message is not None and len(message)==1:
                return Message(message[0][1],message[0][2],message[0][0])
            else:
                return None

    def get_messages(self):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM MESSAGES"
            cursor.execute(query)
            return cursor.fetchall()

    def get_user_pass(self, username):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT PASS FROM USERS WHERE USERNAME = %s"
            cursor.execute(query, (username,))
            password = cursor.fetchall()
            if password is not None and len(password)==1:
                return password[0][0]
            else:
                return None

    def get_user(self, username):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM USERS WHERE USERNAME = %s"
            cursor.execute(query, (username,))
            return cursor.fetchall()

    def add_user(self,username,password):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT PASS FROM USERS WHERE USERNAME = %s"
            cursor.execute(query, (username,))
            if(cursor.fetchall()):
                return 'User already exists'
            query = "INSERT INTO USERS (USERNAME, PASS) VALUES (%s, %s)"
            cursor.execute(query, (username,password))
            connection.commit()
