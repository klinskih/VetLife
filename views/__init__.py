# -*- coding: utf-8 -*-
from VetLife import app
from flask_login import login_required
from flask.templating import render_template
from flask import g
from .auth import login
from .medicine import medicine_edit, medicine_list
from .user import user, edit


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
