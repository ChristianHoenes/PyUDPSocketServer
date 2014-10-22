#https://wiki.python.org/moin/UdpCommunication
import socket
import struct

UDP_IP = "192.168.1.13"
UDP_PORT = 1313

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

try:
	sock.bind((UDP_IP, UDP_PORT))
	
	while True:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		
		print("received message:", data, " - ", addr)
finally:
	sock.close()
