import os
import datetime

from flask import Flask, redirect, render_template, url_for, flash, session,\
    current_app, make_response, abort
from flask_login import current_user, login_required
from flask import Flask
from flask import render_template, redirect, url_for

from .forms import PostForm, CommentForm
from .. import db
from ..models import Role, User, Post, Comment
from . import main
from .forms import NameForm, PostForm

app = Flask(__name__)


# Index page to validate current user and render posts
@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', current_time=datetime.date.today(),
                           form=form, posts=posts)


# User profile 
@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)


# Post with relative id
@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post,
                          author=current_user._get_current_object())
        db.session.add(comment)
        flash('Your comment has been added to VAPORLAND')
        return redirect(url_for('.post', id=post.id))
    pagination = post.comments.order_by(Comment.timestamp.asc()).all()
    comments = pagination
    return render_template('post.html', posts=[post], form=form,
                           comments=comments, pagination=pagination)


# Edit post with relative ID and make sure editor is the post author
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        flash('The VAPORPOST has been updated!')
        return redirect(url_for('main.post', id=post.id))
    form.body.data = post.body
    return render_template('edit_post.html', form=form)
