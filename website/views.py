from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, Climb, User
from . import db
from io import BytesIO
import base64
from matplotlib.figure import Figure


views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    UserData = Climb.query.filter_by(user_id=User.id)

    dates = []
    v0 = []
    v1 = []
    v2 = []
    v3 = []
    v4 = []
    v5 = []
    v6 = []
    v7 = []
    v8 = []
    v9 = []
    v10 = []

    for climb in UserData:
        dates.append(climb.date)
        v0.append(climb.v0)
        v1.append(climb.v1)
        v2.append(climb.v2)
        v3.append(climb.v3)
        v4.append(climb.v4)
        v5.append(climb.v5)
        v6.append(climb.v6)
        v7.append(climb.v7)
        v8.append(climb.v8)
        v9.append(climb.v9)
        v10.append(climb.v10)



    if request.method == 'POST':

        v0_new = request.form.get('v0')
        v1_new = request.form.get('v1')
        v2_new = request.form.get('v2')
        v3_new = request.form.get('v3')
        v4_new = request.form.get('v4')
        v5_new = request.form.get('v5')
        v6_new = request.form.get('v6')
        v7_new = request.form.get('v7')
        v8_new = request.form.get('v8')
        v9_new = request.form.get('v9')
        v10_new = request.form.get('v10')
        date = request.form.get('date')

        new_climb = Climb(v0=v0_new, v1=v1_new, v2=v2_new, v3=v3_new, v4=v4_new, v5=v5_new, v6=v6_new, v7=v7_new, v8=v8_new, v9=v9_new, v10=v10_new, date=date, user_id=current_user.id)
        db.session.add(new_climb)
        db.session.commit()

        flash('Session Added!', category='success')

    return render_template("home.html", user=current_user, dates=dates, v0=v0, v1=v1, v2=v2, v3=v3, v4=v4, v5=v5, v6=v6, v7=v7, b8=v8, v9=v9, v10=v10)