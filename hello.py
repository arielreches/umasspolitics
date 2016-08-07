from flask import Flask, render_template
from flask import make_response
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def index():
	politicians = ["trump", "hillary"]
	return render_template('user.html', politicians=politicians)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
