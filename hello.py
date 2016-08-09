import os
from flask import Flask, render_template, session, redirect, url_for
from flask import make_response
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import Required   
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'LOVEHURTS'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
manager = Manager(app)


def make_shell_context():
	return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.Integer)
    year = db.Column(db.String)
    home_location = db.Column(db.String)
    housing = db.Column(db.String)
    building = db.Column(db.String)
    candidate = db.Column(db.String)

    def __repr__(self):
        return 'Year ' + self.year


class MainSurvey(Form):
	year = SelectField(u'What year do you graduate?', choices=[
		('default', ''), 
		('freshman', 'Freshman'), 
		('sophomore', 'Sophomore'), 
		('junior', 'Junior'),
		('senior', 'Senior'),
		('other', 'Other')], validators=[Required()])
	location = SelectField(u'Where are you from? (Optional)', choices=[
		('default', ''), 
		('north', 'North Shore'), 
		('boston', 'Boston Area'), 
		('south', 'South Shore'),
		('cape', 'Cape Cod'),
		('central', 'Central Mass'), 
		('western', 'Western Mass'),
		('out', 'Out of State')
		])
	housing = SelectField(u'Where do you live?', choices=[
		('default', ''), 
		('central', 'Central'), 
		('honors', 'Honors College'), 
		('northeast', 'Northeast'), 
		('north', 'North Apartments'), 
		('orchard', 'Orchard Hill'),
		('southwest', 'Southwest'),
		('sylvan', 'Sylvan'), 
		('off campus', 'Off-campus')
		])
	candidate = SelectField(u'Who is your 2016 candidate?', choices=[
		('default', ''),
		('donald', 'Donald Trump'),
	 	('hillary', 'Hillary Clinton'),
	 	('johnson', 'Gary Johnson'),
	 	('stein', 'Jill Stein')
	 	])
	submit = SubmitField('Submit')


@app.route('/', methods = ['GET','POST'])
def index():
	politicians = ["trump", "hillary"]
	form = MainSurvey()
	if form.validate_on_submit():
		newUser = User(year=form.year.data, home_location=form.location.data, housing=form.housing.data, candidate=form.candidate.data)
		db.session.add(newUser)
		return redirect(url_for('index'))
	return render_template('home.html', politicians=politicians, form=form)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
