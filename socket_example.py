#http://stackoverflow.com/questions/17558551/write-udp-data-to-csv-in-python
#include libraries n stuff
import socket
import traceback
import csv

#assign variables n stuff
host = ''
port = 5555
csvf = 'accelerometer.csv'

#do UDP stuff
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

#do CSV stuff
with open(csvf, 'wb') as csv_handle:
	while True:
		try:
			message, address = s.recvfrom(8192) 
			print(message)                      #display data on screen
			csv_handle.write(message + b'\n')
		except Exception:
			traceback.print_exc()
