from flask import Flask
import socket
import ipdb
import fcntl
import struct

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


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s', ifname[:15])
	)[20:24])

if __name__ == "__main__":
	# Need to get 
	host = get_ip_address('wlan0')
	app.run(host=host)
