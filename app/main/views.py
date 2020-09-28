from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .. import db
from .forms import BlogPostForm,CommentForm,EditProfileForm,UpdateBlogForm
from ..email import mail_message
from .requests import get_quote
@main.route('/')
def index():
    blogs = Blog.query.all()
    title = 'Home'
    return render_template('index.html', title = title,blogs = blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_title = form.blog_title.data
        blog_content = form.blog_content.data
        

        # Updated  blog instance
        new_blog =Blog(title= blog_title, content= blog_content,user_id = current_user.id)

        # save blog method
        new_blog.save_blog()

        #sending email
        recepients = User.query.all()
        for user in recepients:
            mail_message("New Blog","email/new_blog",user.email,user=user)

        return redirect(url_for('.index' ))
        

    
    title = 'New blog'
    return render_template('new_blog.html',title = title,form = form)

@main.route('/blog/update/<blog_id>',methods=['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    form = UpdateBlogForm()

    if form.validate_on_submit():
        blog_title = form.blog_title.data
        blog_content = form.blog_content.data

        #update blog
        blog.title=blog_title
        blog.content = blog_content
        db.session.commit()

        return redirect(url_for('.view_blog',blog_id = blog.id))
    return render_template('update_blog.html',form=form)
@main.route('/blog/delete/<blog_id>',methods=['GET','POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    user = User.query.filter_by(id=blog.user_id).first()
    uname = user.username
    Blog.query.filter_by(id=blog_id).delete()
    db.session.commit()
    return redirect(url_for('.user_blogs',uname =uname))


@main.route('/comment/delete/<comment_id>', methods =['GET', 'POST'])
@login_required
def delete_comment(comment_id):
    comment=Comment.query.filter_by(id=comment_id).first()
    blog_id = comment.blog_id
    blog = Blog.query.filter_by(id=blog_id).first()
    user = User.query.filter_by(id=blog.user_id).first()
    if user == current_user:
        Comment.query.filter_by(id=comment_id).delete()
        db.session.commit() 
    return redirect(url_for('.view_blog',blog_id=blog_id))
@main.route('/blog/view/<blog_id>', methods=['GET', 'POST'])
def view_blog(blog_id):
    blog=Blog.query.filter_by(id= blog_id).first()
    user = User.query.filter_by(id=blog.user_id).first()
    comments = Comment.get_comments(blog_id)
    comment_form = CommentForm()
    if current_user.is_authenticated:
        
        if comment_form.validate_on_submit():
            comments = comment_form.description.data

            new_comment = Comment(comment=comments,user_id=current_user.id, blog_id =  blog_id)

            new_comment.save_comment()
            
            return redirect(url_for('.view_blog', blog_id= blog_id))
        comments = Comment.get_comments(blog_id)
          
    return render_template('blog.html',  blog= blog, comments=comments,  blog_id= blog.id, comment_form = comment_form, user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def edit_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = EditProfileForm()

    if form.validate_on_submit():
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/edit_profile.html',form =form)

@main.route('/user/<uname>/blogs')
def user_blogs(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    
    return render_template("profile/myblog.html", user=user, blogs= blogs)


@main.route('/quote')
def quote( quote_id):
    '''function that displays a  quote in  quote.html'''
    quotes = get_quote()
    return render_template(' quote.html', quotes=quotes)
