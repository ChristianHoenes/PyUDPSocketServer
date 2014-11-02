#https://wiki.python.org/moin/UdpCommunication
import socket
import struct
import time
import sqlite3 as lite

UDP_IP = "192.168.1.13"
UDP_PORT = 1313

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

try:
    sock.bind((UDP_IP, UDP_PORT))
    
    datetmp = int(time.strftime("%y%m%d"))
    con = lite.connect("Databases/"+str(datetmp)+".db")
	
    while True:
        datalen = 34
        data, addr = sock.recvfrom(datalen) # buffer size is 1024 bytes
        print("received: ",  data)
        print(len(data))
        if len(data)==datalen:
            message = struct.unpack("<lllLLLLLh",data)
            userID = message[0]
            latitude = message[1]
            longitude = message[2]
            fix_age = message[3]
            time = message[4]
            date = message[5]
            speed = message[6]
            course = message[7]
            checksum = message[8]

            data = (time,latitude,longitude,speed,course)

            if date != datetmp:
                con = lite.connect("Databases/"+str(date)+".db")

            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS id_"+str(userID)+"(Time INT, Latitude INT, Longitude INT, Speed INT, Course INT)")
                cur.execute("INSERT INTO id_"+str(userID)+" VALUES(?, ?, ?, ?, ?)", data)

            for i in range(len(message)):
                print ':',
                print message[i],
            print ""
finally:
    sock.close()
