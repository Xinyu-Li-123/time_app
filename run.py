from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
	e = dt.now()	
	return "You visited this page at {}/{}/{} {}:{}:{} GMT".format(
		e.year, e.month, e.day, e.hour, e.minute, e.second
	)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
