#https://wiki.python.org/moin/UdpCommunication
import socket
import time
import struct

#GPS Example
# $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
lat = 4882373
lon = 906030
fix_age = 36
t = 12351913
date=131313
speed = 20
course = 13
checksum = 42

btime = struct.pack("<llLLLLLHcc",lat,lon,fix_age,t,date,speed,course,checksum,'\r','\r')

UDP_IP = "karadras.ddns.net"
# UDP_IP = "46.252.18.138"
UDP_PORT = 1313
MESSAGE = btime

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
while (True):
	print("UDP target IP:", UDP_IP)
	print("UDP target port:", UDP_PORT)
	print("message:", MESSAGE)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	time.sleep(1)
