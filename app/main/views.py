from flask import render_template
from . import main
from ..models import User,Blog,Comment
from .. import db

@main.route('/')
def index():
    blogs = Blog.get_all_blogs()
    title = 'Home'
    return render_template('index.html', title = title,blogs = blogs)