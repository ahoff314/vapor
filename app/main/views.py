from flask import Flask, redirect, render_template, url_for, flash, session,\
    current_app, make_response
from . import main
from flask import Flask
import datetime
from flask import render_template, redirect, url_for
import os


from .forms import NameForm

app = Flask(__name__)

# Routes
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('You changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', current_time=datetime.date.today(),
        form=form, name=session.get('name'), known=session.get('known', False))
    

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
