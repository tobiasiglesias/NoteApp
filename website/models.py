from . import db
from flask_login import UserMixin
from wtforms import StringField, PasswordField, validators, TextAreaField
from flask_wtf import FlaskForm


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))
    notes = db.relationship('Note', backref='note', passive_deletes=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(30))
    body = db.Column(db.Text)


# ---Forms---

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Length(min=4, max=30), validators.DataRequired()])

class SignUpForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=4, max=30), validators.DataRequired(),
                                         validators.EqualTo('confirm', message='Passwords must match')])
    email = StringField('Email', [validators.Length(min=4,max=50), validators.DataRequired(),])
    confirm = PasswordField('Repeat password')
    
class NoteForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1,max=30)])
    body = TextAreaField('Body',{validators.DataRequired()}) 