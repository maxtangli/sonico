from flask import Flask, request, render_template, Markup, abort, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
"""
day2 finish tutorial, try pip,venv,flask 60min
thoughts
- python> import this # the zen of python
- modern toolchains, microframework...python vs ruby?
"""
