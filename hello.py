from flask import Flask, render_template
from flask import make_response
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import Required   

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LOVEHURTS'
bootstrap = Bootstrap(app)

class ResAreaForm(Form):
	year = SelectField(u'What year do you graduate?', choices=[
		('default', ''), 
		('2017', '2017'), 
		('2018', '2018'), 
		('2019', '2019'),
		('2020', '2020'),
		('2021', '2021'), 
		('2022', '2022')])
	location = SelectField(u'Where are you from? (Optional)', choices=[
		('default', ''), 
		('north', 'North Shore'), 
		('boston', 'Boston Area'), 
		('south', 'South Shore'),
		('cape', 'Cape Cod'),
		('central', 'Central Mass'), 
		('western', 'Western Mass'),
		('out', 'Out of State')])
	housing = SelectField(u'Where do you live?', choices=[
		('default', ''), 
		('central', 'Central'), 
		('honors', 'Honors College'), 
		('northeast', 'Northeast'), 
		('north', 'North Apartments'), 
		('orchard', 'Orchard Hill'),
		('southwest', 'Southwest'),
		('sylvan', 'Sylvan'), 
		('off campus', 'Off-campus')])
	building = SelectField(u'(Filter this given previous answer) Which building?', choices=[
		('default', '')])
	candidate = SelectField(u'Who is your 2016 candidate?', choices=[
		('default', ''),
		('donald', 'Donald Trump'),
	 	('hillary', 'Hillary Clinton')])
	submit = SubmitField('Submit')

@app.route('/', methods = ['GET','POST'])
def index():
	politicians = ["trump", "hillary"]
	form = ResAreaForm()
	return render_template('home.html', politicians=politicians, form=form)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
