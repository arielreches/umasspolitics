from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from . import main
from .forms import MainSurvey


@main.route('/', methods = ['GET','POST'])
def index():
	politicians = ["trump", "hillary"]
	form = MainSurvey()
	if form.validate_on_submit():
		newUser = User(year=form.year.data, home_location=form.location.data, housing=form.housing.data, candidate=form.candidate.data)
		db.session.add(newUser)
		return redirect(url_for('index'))
	return render_template('home.html', politicians=politicians, form=form)