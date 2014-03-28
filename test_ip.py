import csv
import ipdb
import socket
import fcntl 
import struct

f = open('/proc/net/route')
for i in csv.DictReader(f, delimiter="\t"):
	ipdb.set_trace()
	if long(i['Destination'], 16) == 0:
		print i['Iface']


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 
		0x8915, 
		struct.pack('256s', ifname[:15]))[20:24])


print get_ip_address('wlan0')

