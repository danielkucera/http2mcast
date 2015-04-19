#!/usr/bin/python

import urllib
import socket

url = "https://tv.danman.eu/stream/channelid/452736958?ticket=F27E6BCAC914CA9219CE4C146C8C207BEF8DADFE&profile=pass"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

fh = urllib.urlopen(url)
#fh = open("prima.ts", 'r')

i = 0
payload = ""
PID = 8

while True:
	packet = fh.read(188)

	PID = ord(packet[2]) + (ord(packet[1]) % 32) * 256

	if PID == 0:
		payload = packet[4:]
#		print "Have PAT"
#		print packet.encode("hex")
#		print payload.encode("hex")
		j = 9
		while j < 20:
			print "Program number", ord(payload[j])*256 + ord(payload[j+1])
			print "PMT", ord(payload[j+2])*256 + ord(payload[j+3])
			print ""
			j += 4

	if i == 7:
		sock.sendto(payload, ("239.1.1.1", 1234))
		payload = packet
		i = 0
	else:
		payload += packet
	i += 1
		


