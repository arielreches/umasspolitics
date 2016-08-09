from flask_wtf import Form
from wtforms import SelectField, SubmitField
from wtforms.validators import Required

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