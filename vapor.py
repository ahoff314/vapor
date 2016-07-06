from flask import Flask, redirect, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "0c54d5b40d6638fe6aac8828489ae02786036211dea6f49e"
app.debug = True # Remove in production
Bootstrap(app)

class NameForm(Form):
    name = StringField("What is your name, friend?", validators=[Required()])
    submit = SubmitField('Submit')

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ' '
    return render_template('index.html', current_time=datetime.date.today(),
    form=form, name=name)
    

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Development server
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app.run(host=host, port=port)
  