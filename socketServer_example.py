#http://stackoverflow.com/questions/16589342/send-arduino-sensor-data-to-server-with-gprs-shield-and-at-commands
import SocketServer

PORTNO = 14

class handler(SocketServer.DatagramRequestHandler):
	def handle(self):
		newmsg = self.rfile.readline().rstrip()
	print (newmsg)
		self.wfile.write(self.server.oldmsg)
		self.server.oldmsg = newmsg

s = SocketServer.UDPServer(('',PORTNO), handler)
print "Awaiting UDP messages on port %d" % PORTNO
s.oldmsg = "This is the starting message."
s.serve_forever()
