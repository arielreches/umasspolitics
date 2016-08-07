from flask import Flask, render_template
from flask import make_response
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import Required   

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LOVEHURTS'
bootstrap = Bootstrap(app)


class ResAreaForm(Form):
	name = RadioField('Label', choices=[('value','description'),('value_two','whatever')])

	submit = SubmitField('Submit')

@app.route('/')
def index():
	politicians = ["trump", "hillary"]
	form = ResAreaForm()
	return render_template('home.html', politicians=politicians, form=form)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
