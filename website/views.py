from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, Climb
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        # note = request.form.get('note')

        # new_note = Note(data=note, user_id=current_user.id)
        # db.session.add(new_note)
        # db.session.commit()

        v0 = request.form.get('v0')
        v1 = request.form.get('v1')
        v2 = request.form.get('v2')
        v3 = request.form.get('v3')
        v4 = request.form.get('v4')
        v5 = request.form.get('v5')
        v6 = request.form.get('v6')
        v7 = request.form.get('v7')
        v8 = request.form.get('v8')
        v9 = request.form.get('v9')
        v10 = request.form.get('v10')
        date = request.form.get('date')

        new_climb = Climb(v0=v0, v1=v1, v2=v2, v3=v3, v4=v4, v5=v5, v6=v6, v7=v7, v8=v8, v9=v9, v10=v10, date=date, user_id=current_user.id)
        db.session.add(new_climb)
        db.session.commit()

        flash('Session Added!', category='success')

    return render_template("home.html", user=current_user)