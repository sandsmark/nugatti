# -*- coding: utf-8 -*-

#######################################
##                                   ##
##  Nugatti  v0.0X                   ##
##   - Gnutella/Python/Qt            ##
##                                   ##
##     ~    network stuff    ~       ##
##                                   ##
##                                   ##
#######################################

##########################################
### COPYRIGHT                          ###
###         MARTIN T. SANDSMARK 2006/7 ###
###       www.mts-productions.com      ###
##########################################

# TODO:
#  ¤ Implement not-really-needed-stuff (experimental gnutella stuff)
#  ¤ Actually do something with parsed packages (like answer and send files)
#  ¤ Threading
#  ¤ testing if it works
#  ¤ (http) serving code
#  ¤ pad payloadlength properly
#  ¤ Register the "NUGT" vendorcode the right place
#  ¤ Read metadata from files (mutagen?)
#_____________________________________ ____ ___ __ _

import BaseHTTPServer, SimpleHTTPServer
import os, urllib, sys, socket, random, threading

#version = '?hostfile=1&client=QPYT&version=0.1'


#gwebcache = gwebcache + version

MAX_PACKET_SIZE = 1024
MAX_PAGE_LEN = 20000 # for reading gwebcache
SERVEPORT = 7770
VENDORCODE = 'NUGT' ## TODO: Register this.
HOSTFILENAME = 'hosts.txt'
DOWNLOADDIR = '/home/martin/Downloads'
WEBCACHE = 'http://gwc.dietpac.com:8080/?hostfile=1&client=QPYT&version=0.1'

DEBUG = 1

#payloadType = {'Ping'		: '\x00',
		#'Pong'		: '\x01',
		#'Bye'		: '\x02',
		#'Push'		: '\x40',
		#'Query'		: '\x80',
		#'Query Hit'	: '\x81' }

class server:
	def __init__(self):
		return

def addressToTuple(combined):
	addressAndPort = combined.split(':',1)[0]
	return (addressAndPort[0], addressAndPort[1])

def debug(message):
	#if DEBUG: 
	print message
	return

def alert(message):  #Do some voodoo and pop up a qdialog here
	print message

def generateGUID():
	guid = ''
	for i in range(7):
		guid = guid + chr(random.randint(0,255))
	guid = guid + '\xff'
	for i in range(7):
		guid = guid + chr(random.randint(0,255))
	guid = guid + '\x00'
	return guid

def getFile(ip, port, filename, fileID):
	file = ''
	path = '/get/' + str(fileID) + filename
	queryAddress = 'http://' + ip + ':' + port + path
	fileContent = urllib.urlopen(queryAddress).read()
	file = open(DOWNLOADDIR + filename, 'w')
	file.write(fileContent)
	file.close()
	return true


class fileList:
	#fileID[] = 0
	#fileName[] = ''
	#filePath[] = ''
	#fileSize[] = 0
	#fileExtended[] = ''
	def __init__(self):
		os.chdir(DOWNLOADDIR)
		filelist = os.listdir(DOWNLOADDIR)
		ID = 0
		for file in filelist:
			self.fileID[ID] = ID
			self.fileName[ID] = file
			self.filePath[ID] = DOWNLOADDIR + file
			self.fileSize[ID] = os.path.getsize(self.filePath[ID])
			self.fileExtended = '' ## TODO: Implement reading of 
						# meta-info from files.
			ID += 1


class Connection:
	server = ''	
	rSocket = None
	wSocket = None
	connected = False
	serventID = ''
	localIP = ''
	localPort = 0
	speed = 10			##TODO: Implement speed checking
	
	def __init__(self, address):		#initiate connection with servent at `address`-tuple
		try:
			debug(address)
			servantSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			servantSocket.connect(address)
			self.rSocket = servantSocket.makefile("rb", 0)
			self.wSocket = servantSocket.makefile("wb", 0)
			debug("initiate handshake...")	
			self.wSocket.write("GNUTELLA CONNECT/0.6\r\n")
			self.wSocket.write("User-Agent: Nugatti/0.1\r\n")
			self.wSocket.write("Pong-Caching: 0.1\r\n")
			self.wSocket.write("GGEP: 0.1\r\n")
			self.wSocket.write("X-Ultrapeer: False\r\n")
			self.wSocket.write("\r\n")
			debug("sent handshake, waiting for reply")
			reply = self.rSocket.readline()
			if ("2" not in reply):
				print 'Host reply error:', reply
				self.wSocket.close()
				self.rSocket.close()
				self.connected = False
				return
			debug("our handshake acknowledged")
			while reply != '\r\n':
				reply = self.rSocket.readline()
				debug(reply)
			debug("acknowledging other handshake")
			self.wSocket.write('GNUTELLA/0.6 200 OK')
			self.wSocket.write('\r\n')
			self.connected = True

			for i in range(15):				##FIXME: Generates a completely random ID, while it optimaly
				sID = sID + chr(random.randint(0,255))	## should be a function of the servents network address.
			self.serventID = sID				## Maybe use MAC-address?

			self.localPort = SERVEPORT			##TODO: read the port from somewhere.

			debug('found a host')
			return None

		except socket.error:
			try:
				self.wSocket.close()
				self.rSocket.close()
				servantSocket.close()
			except:
				alert('Socket error while trying to connect to servent!')
				self.connected = False
				sys.exit()
			return
		


		
	def sendPing(self):
		guid = generateGUID()
		ttl = 7
		hops = 0
		payloadType = '\x00' #Ping
		payload = ''
		self.sendMessage(guid, payloadType, ttl, hops, payload)
		
	def sendPong(self,  guid, ttl, host, port, sizeShared, numShared):
		payload = str(port) + str(host) + str(numShared) + str(sizeShared)
		payloadType = '\x01' #Pong
		hops = 0
		sendMessage(self, guid, payloadType, ttl, hops, payload)
	
	def sendQuery(self, firewalled, criteria):
		newSemantic = '1'
		enableXML = '0'		##TODO: Implement XML support, LGDQ, ggeph oob, and the rest.
		LGDQ = '0'
		ggepH = '0'
		outOfBand = '0'
		reserved = '0000000000'
		minSpeed = chr(int(reserved + outOfBand + ggepH + LGDQ + enableXML + firewalled + newSemantic, 2)) #16 bits=2 bytes
		
		payload = minSpeed + criteria + '\x00' #2 bytes with minSpeed + search criteria terminated with 0x00
		
		guid = generateGUID()
		payloadType = '\x80' #Query
		ttl = 7
		hops = 0
		self.sendMessage(guid, payloadType, ttl, 0, payload)
		
	def sendQueryHit(self, filelist):
		speed = self.speed
		port = self.localPort
		ip = self.localIP
		resultSet = ''
		numHits = 0
		for ID in filelist.fileID:
			resultSet = resultSet + str(ID)
			resultSet = resultSet + str(filelist.fileSize[ID])
			resultSet = resultSet + filelist.fileName[ID] + '\x00'
			resultSet = resultSet + filelist.fileExtended[ID] + '\x00'
			numHits += 1
		EQHD = ''				##TODO: Implement EQHD
		payload = str(numHits) + str(port) + str(ip) + str(speed) + resultSet + EQHD + self.serventID
		guid = generateGUID()
		payloadType = '\x81' #Query hit
		tll = 7
		hops = 0
		self.sendMessage(guid, payloadType, tll, hops, payload)

	def sendPush (self, serventID, fileID):			#Remote servent ID, in case you're wondering
		port = self.localPort
		ip = self.localIP
		guid = generateGUID()
		payload = serventID + str(fileID) + ip + str(port)
		payloadType = '\0x40' #Push
		ttl = 7
		hops = 0
		self.sendMessage(guid, payloadType, ttl, hops, payload)

	def sendMessage(self, guid, payloadType, ttl, hops, payload):
		payloadLength = len(payload)
		headerPad = ''
		if payloadLength < 4:
			for i in range(4 - payloadLength):
				headerPad = headerPad + '\x00'
		header = guid + payloadType + str(ttl) + str(hops) + str(payloadLength) + headerPad
		package = header + payload
		debug(package)
		self.wSocket.write(package)

	def parseLoop(self):
		loop = 1
		packet = ''
		
		guid = ''
		payloadType = ''
		ttl = 0
		hops = 0
		payloadLength = 0
		
		while (loop == 1):
			data = ''
			while (data == ''):
				data = self.rSocket.recv(MAX_PACKET_SIZE)
			packet = packet + data
			if (len(packet) > 23): # We have received enough data for a full header, so we try to parse it.
				guid = packet[0:15]
				payloadType = packet[16]
				ttl = atoi(packet[17])
				hops = atoi(packet[18])
				payloadLength = atoi(packet[19:22]) # Not very fault tolerant is it? TCP ftw.
			if ((23 + atoi(payloadLength)) <= len(packet)): #Check if we have received the whole package
				payload = packet[23:(23+payloadLength)]
				## DO MAGIC!
				packet = packet[(23 + atoi(payloadLength)):] ## Return the unused packetparts
				
		
		
		###Parse the darn package.




class Hosts:
	list = [ ]

	def __init__(self):
		self.list = [ ]
		self.list = self.load()
		if not self.list:
			debug('no hosts saved, getting new hosts')
			self.list = self.gwebcache(WEBCACHE)
		if not self.list:
			print 'Cannot find any hosts!'
			sys.exit()
		else:
			self.save(self.list)

	def gwebcache(self, url):
		try:
			hostList = urllib.urlopen(url).read(MAX_PAGE_LEN)
		except IOError, e:
			alert('I/O Error when reading gwebcache from URL' + url + ':\n' + e.strerror)
			sys.exit()
		return hostList.splitlines()

	def save(self, hostlist):
		debug(hostlist)
		global hostfilename
		try:
			output = open(hostfilename, 'w')
			#output.writelines (hostlist)
			for line in hostlist:
				output.write(line)
			output.close()
		except IOError,e:
			alert('error writing hosts file')
			sys.exit()

	def load(self):
		global hostfilename
		try:
			input = open(hostfilename, 'r')
			hostlist = input.readlines()
			input.close()
		except IOError,e:
			hostlist = [ ]
		return hostlist
	

#hosts = Hosts()
#debug(hosts.list)
#for address in hosts.list:
	#ip = address.split(':',1)[0]
	#port = int(address.split(':',1)[1])
	#print ip, port
	#host = Connection((ip, port))
	#if (host.connected == True):
		#break

#host.server = BaseHTTPServer.HTTPServer(('',host.localPort),SimpleHTTPServer.SimpleHTTPRequestHandler) 
#server.serve_forever()
lol = Connection (('127.0.0.1', 33587))
print lol
lol.sendPing()
