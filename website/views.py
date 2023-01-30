from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from .models import NoteForm, Note
from . import db
# from flask_sqlalchemy import session

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    titles = get_titles()
    return render_template('home.html', user=current_user, titles=titles)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    form = NoteForm(request.form)
    notes = (db.session.query(Note).filter(Note.user==int(current_user.get_id())))
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        new_note = Note(user=current_user.get_id(), title=title, body=body)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added')
    return render_template('notes.html', user=current_user, template_form=form, notes=notes)

@views.route('/<username>/<title>')
@login_required
def title(username, title):
    if current_user.username == username: 
        form = NoteForm(request.form)
        titles=get_titles()
        try: 
            notes = list(db.session.query(Note).filter(Note.title==title))
            return render_template('title.html', user=current_user, titles=titles, notes=notes, template_form=form)
        
        except:
            return render_template('access.html', user=current_user)
    else:
        return render_template('access.html', user=current_user)


@views.route('/<username>/delete:<note_id>', methods={"POST"})
@login_required
def delete_note(username, note_id):
    if current_user.username == username:
        db.session.query(Note).filter_by(id=note_id).delete()
        db.session.commit() 
    return redirect('/notes')

        


def get_titles():
    user_id = int(current_user.get_id())
    posts = list(db.session.query(Note).filter_by(user = user_id).group_by(Note.title).distinct())
    titles = list(map((lambda note: note.title), posts))
    return titles

