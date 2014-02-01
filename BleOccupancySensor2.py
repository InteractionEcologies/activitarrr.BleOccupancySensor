# Module: BleOccupancySensor
# Author: Chuan-Che, Jeff, Huang
# 
# References
# 	- https://wiki.python.org/moin/UdpCommunication#Multicasting.3F

import threading
import socket

import ipdb

DISCOVERY_PORT = 48468
DISCOVERY_RESPONSE_PORT = 48467

ANY_IP = "0.0.0.0"
BROADCAST_IP = '255.255.255.255'

# Need to change these parameters after the driver is written.
CLASS_IDENTIFIER = 'HomeOSGadgeteerDevice'
TYPE_IDENTIFIER = 'MoistureSensor'
MANUFACTURER = 'MicrosoftResearch'
DEVICE_UNIQUE_ID = '001'

"""
Process
	Multi-thread: DiscoveryThread()
	1. Send udp broadcast
	2. 
"""
# send udp broadcast


# receive UDP messages
class DiscoveryThread(threading.Thread):

	def run(self):
		discovery()

def discovery():
	print "Start discovery ... "
	sock = socket.socket(socket.AF_INET, #Internet
		socket.SOCK_DGRAM) # UDP

	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((ANY_IP, DISCOVERY_PORT))

	while True:

		### Need to add Wifi checking here. 
		# if no Wifi, ...
		# code ... 

		data, addr = sock.recvfrom(1024)
		print "received messages: %s, from ip: %s" % (data, addr)

		#send back UDPBroadcast via DiscoveryResponsePort
		send_udp_broadcast(DISCOVERY_RESPONSE_PORT)

def send_udp_broadcast(port):
	sock = socket.socket(socket.AF_INET, 
						socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	identifier_string = "%s_%s_%s_%s" % (CLASS_IDENTIFIER, TYPE_IDENTIFIER, MANUFACTURER, DEVICE_UNIQUE_ID)

	sock.sendto(identifier_string, (BROADCAST_IP, DISCOVERY_RESPONSE_PORT))

if __name__ == "__main__":
	print "Program start ... "
	discoveryThread = DiscoveryThread()
	discoveryThread.start()


# 	bleOccupancySensor = BleOccupancySensor()
# 	bleOccupancySensor.start()