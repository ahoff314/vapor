from flask import Flask, redirect, render_template, url_for, flash, session,\
    current_app, make_response
from flask_login import current_user
from . import main
from flask import Flask
import datetime
from flask import render_template, redirect, url_for
import os

from .forms import PostForm
from .. import db # or from APP.MODELS?
from ..models import Role, User, Post

from .forms import NameForm, PostForm

app = Flask(__name__)

# Routes
@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', current_time=datetime.date.today(), ## TODO DELETE SOME OF EXCESS
                            form=form, posts=posts)
    

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)
