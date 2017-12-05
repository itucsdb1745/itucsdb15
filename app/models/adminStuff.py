import psycopg2 as dbapi2
from flask import current_app
from passlib.apps import custom_app_context as pwd_context
from flask_login import current_user

class adminCommands:
    def resetEverything():
        if current_user.is_admin:
            with dbapi2.connect(current_app.config['dsn']) as connection:
                cursor = connection.cursor()

                query = "DROP TABLE IF EXISTS ANSWERS"
                cursor.execute(query)
                
                query = "DROP TABLE IF EXISTS MESSAGES"
                cursor.execute(query)

                query = "DROP TABLE IF EXISTS USERS"
                cursor.execute(query)

                query = "CREATE TABLE USERS (USERNAME VARCHAR(50) PRIMARY KEY,PASS VARCHAR(120), ISADMIN BOOLEAN)"
                cursor.execute(query)

                query = "CREATE TABLE MESSAGES (ID SERIAL PRIMARY KEY,TITLE VARCHAR(50),CONTENT VARCHAR(500), USERNAME VARCHAR(50) REFERENCES USERS(USERNAME))"
                cursor.execute(query)

                query = "CREATE TABLE ANSWERS (ID SERIAL PRIMARY KEY, MESSAGE_ID INTEGER REFERENCES MESSAGES(ID), USERNAME VARCHAR(50) REFERENCES USERS(USERNAME), CONTENT VARCHAR(500))"
                cursor.execute(query)

                hashedPass = pwd_context.encrypt('admin')
                query = "INSERT INTO USERS VALUES (%s, %s, %s)"
                cursor.execute(query,('admin',hashedPass,True,))

                connection.commit()
