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
		datalen = 30
		data, addr = sock.recvfrom(datalen) # buffer size is 1024 bytes
		print("received: ",  data)
		print(len(data))
		if len(data)==datalen:
			message = struct.unpack("<llLLLLLh",data)
			t = message[0]
			latitude = message[1]
			#nord = message[2]
			#longitude = message[3]
			#east = message[4]
			#print("received message:", (t,latitude,nord,longitude,east), " - ", addr)
			for i in range(len(message)):
				print ':',
				print message[i],
			# print("received message:", (t,latitude), " - ", addr)
			print ""
finally:
	sock.close()
