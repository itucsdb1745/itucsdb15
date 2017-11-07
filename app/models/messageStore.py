import psycopg2 as dbapi2
from flask import current_app
from app.models.message import Message

class MessageStore:
    def __init__(self):
        self.messages = {}
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
        return self.messages
