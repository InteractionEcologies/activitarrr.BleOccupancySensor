from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/check')
def check():
	return 'Check'

@app.route('/api/occupancy')
def get_occupancy():
	return "Occupancy"

if __name__ == "__main__":
	# Need to get 
	host = socket.gethostbyname(socket.gethostname())
	app.run(host=host)