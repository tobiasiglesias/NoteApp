from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import NoteForm, Note
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    form = NoteForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        new_note = Note(user=current_user.get_id(), title=title, body=body)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added')

        
    return render_template('notes.html', user=current_user, template_form=form)