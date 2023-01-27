from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import LoginForm, SignUpForm, User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user


auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        if User.query.filter_by(email=email).first():
            flash('Email already in use', category='error')
        elif User.query.filter_by(username=username).first():
            flash('Username already in use', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering')
            login_user(user=new_user, remember=True)
            return redirect(url_for('views.notes'))
    return render_template('sign_up.html', template_form=form, user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user=user, remember=True)
                flash(f'Logged in as {user.username}!')
                redirect(url_for('views.home'))
        else:
            flash('Username or Password not matching.')
            

    return render_template('login.html', template_form=form, user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))