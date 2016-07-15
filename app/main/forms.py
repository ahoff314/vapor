from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField,\
    SubmitField, TextAreaField
from wtforms.validators import Required, Length, Email
from flask_pagedown.fields import PageDownField


class NameForm(Form):
    name = StringField("What is your name, friend?", validators=[Required()])
    submit = SubmitField('SUBMIT')


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in to Vapor Land')
    submit = SubmitField('Log In')


class PostForm(Form):
    body = TextAreaField("POST TO VAPORLAND", validators=[Required()])
    submit = SubmitField('SUBMIT')


class CommentForm(Form):
    body = StringField('', validators=[Required()])
    submit = SubmitField('SUBMIT')
