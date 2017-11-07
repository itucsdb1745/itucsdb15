import psycopg2 as dbapi2
from flask import current_app
class adminCommands:
    def resetEverything():
        # add admin check
        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()

            query = "DROP TABLE IF EXISTS MESSAGES"
            cursor.execute(query)

            query = "CREATE TABLE MESSAGES (ID SERIAL PRIMARY KEY,TITLE VARCHAR(50),CONTENT VARCHAR(500))"
            cursor.execute(query)

            #add user and comments tables

            connection.commit()
