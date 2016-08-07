from flask import Flask, render_template
from flask import make_response
from flask_script import Manager

app = Flask(__name__)



@app.route('/')
def index():
	politicians = ["trump", "hillary"]
	return render_template('index.html', politicians=politicians)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
