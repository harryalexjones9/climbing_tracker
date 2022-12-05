from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, Session
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        note = request.form.get('note')

        # new_note = Note(data=note, user_id=current_user.id)
        # db.session.add(new_note)
        # db.session.commit()

        session = request.form.get('session')

        new_session = Session(v0=session, user_id=current_user.id)
        db.session.add(new_session)
        db.session.commit()

        flash('Session Added!', category='success')

    return render_template("home.html", user=current_user)