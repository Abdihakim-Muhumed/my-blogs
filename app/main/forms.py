from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField,  BooleanField, TextAreaField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Required
from app.models import User, Blog, Comment

class BlogPostForm(FlaskForm):
    blog_title = StringField('Title', validators = [Required()])
    blog_content = TextAreaField("Enter blog content", validators = [Required()])
    submit = SubmitField('Submit')
class UpdateBlogForm(FlaskForm):
    blog_title = StringField('Title', validators = [Required()])
    blog_content = TextAreaField("Enter blog content", validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    description = TextAreaField('Add a comment:', validators = [Required()])
    submit = SubmitField('Submit')

class EditProfileForm(FlaskForm):
    bio= TextAreaField('Edit your bio:',validators = [Required()])
    submit = SubmitField('Submit')
