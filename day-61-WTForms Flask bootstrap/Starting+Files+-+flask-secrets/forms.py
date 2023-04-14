from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators


# in order to install validators you need to tap to terminal and pass validator package ex pip install wtforms[email]
class SignUpForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), validators.Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label="Sign up")
