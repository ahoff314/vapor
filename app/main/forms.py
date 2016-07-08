from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField,\
    SubmitField
from wtforms.validators import Required, Length, Email

class NameForm(Form):
    name = StringField("What is your name, friend?", validators=[Required()])
    submit = SubmitField('SUBMIT')
    
class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), 
                                                                    Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in to Vapor Land')
    submit = SubmitField('Log In')