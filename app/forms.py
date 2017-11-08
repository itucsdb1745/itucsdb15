from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddMessageForm(FlaskForm):
    #add maximum lenght
    title = StringField(
        'Title',
        validators=[
            DataRequired()
        ]
    )

    text = StringField(
        'Text',
        validators=[
            DataRequired()
        ]
    )
