import psycopg2 as dbapi2
from flask import current_app
from app.models.message import Message
from app.models.messageAnswer import MessageAnswer
from flask_login import current_user

class Database:
    def __init__(self):
        self.last_m_id = 0

    def add_message(self, message):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO MESSAGES (TITLE, CONTENT, USERNAME) VALUES (%s, %s, %s)"
            cursor.execute(query, (message.title, message.text, current_user.username))
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
            query = "SELECT * FROM MESSAGES LEFT OUTER JOIN USERS ON MESSAGES.USERNAME = USERS.USERNAME"
            cursor.execute(query)
            messages = cursor.fetchall()
            return messages

    def get_message_answers(self):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM MESSAGES"
            cursor.execute(query)
            messages = cursor.fetchall()
            answers = {}
            for message in messages:
                query = "SELECT * FROM ANSWERS LEFT OUTER JOIN USERS ON ANSWERS.USERNAME=USERS.USERNAME WHERE MESSAGE_ID=%s ORDER BY VOTES DESC"
                cursor.execute(query,(message[0],))
                answer = cursor.fetchall()
                answers[message[0]]=answer
            return answers

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

    def get_message_answer(self, messageId):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM ANSWERS INNER JOIN USERS ON ANSWERS.USERNAME=USERS.USERNAME WHERE ID = %s"
            cursor.execute(query, (messageId,))
            messageArray = cursor.fetchall()
            print(messageArray)
            if messageArray is not None and len(messageArray)==1 :
                return messageArray[0]
            return None

    def add_message_answer(self, messageAnswer):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO ANSWERS (MESSAGE_ID,USERNAME,CONTENT) VALUES (%s, %s, %s)"
            cursor.execute(query, (messageAnswer.messageId, messageAnswer.username, messageAnswer.text,))
            connection.commit()

    def up_answer(self,answerId):
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = "UPDATE ANSWERS SET VOTES = VOTES + 1 WHERE ID=%s "
            cursor.execute(query,(answerId,))
            connection.commit()
