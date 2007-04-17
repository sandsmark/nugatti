#####################
"""Nugatti - Nutella Python Qt """
""" network stuff """
#TODO sendQueryHit
import BaseHTTPServer, SimpleHTTPServer
import os, urllib, sys, socket, random

os.chdir('/home/martin/Stuff/Downloads')

#version = '?hostfile=1&client=QPYT&version=0.1'

hostfilename = 'hosts.txt'
#gwebcache = gwebcache + version

MAX_PAGE_LEN = 20000
SERVEPORT = 7770

payloadType = {'Ping'		: '\x00',
		'Pong'		: '\x01',
		'Bye'		: '\x02',
		'Push'		: '\x40',
		'Query'		: '\x80',
		'Query Hit'	: '\x81' }

class server:
	def __init__(self):
		server = BaseHTTPServer.HTTPServer(('',SERVEPORT),SimpleHTTPServer.SimpleHTTPRequestHandler)
		return

def addressToTuple(combined):
	addressAndPort = combined.split(':',1)[0]
	return (addressAndPort[0], addressAndPort[1])

def debug(message):
	#print message
	return

class Connection:
	
	rSocket = None
	wSocket = None
	connected = False
	
	def __init__(self, address):
		try:
			debug(address)
			servantSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			servantSocket.connect(address)
			self.rSocket = servantSocket.makefile("rb", 0)
			self.wSocket = servantSocket.makefile("wb", 0)
		
			self.wSocket.write("GNUTELLA CONNECT/0.6\r\n")
			self.wSocket.write("User-Agent: qPyTella/0.1\r\n")
			self.wSocket.write("Pong-Caching: 0.1\r\n")
			self.wSocket.write("GGEP: 0.1\r\n")
			self.wSocket.write("X-Ultrapeer: False\r\n")
			self.wSocket.write("\r\n")

			reply = self.rSocket.readline()
			if ("200" not in reply):
				print 'Host reply error:', reply
				self.wSocket.close()
				self.rSocket.close()
				self.connected = False
				return
		
			while reply != '\r\n':
				reply = self.rSocket.readline()
				debug(reply)
		
			self.wSocket.write('GNUTELLA/0.6 200 OK')
			self.wSocket.write('\r\n')
			self.connected = True
			debug('found a host')
			return None

		except socket.error:
			try:
				self.wSocket.close()
				self.rSocket.close()
				servantSocket.close()
			except:
				print "Something is horribly wrong!"
			self.connected = False
			return
		
	def sendPing(self):
		guid = generateGUID
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
		enableXML = '0'
		LGDQ = '0'
		ggepH = '0'
		outOfBand = '0'
		reserved = '0000000000'
		minSpeed = chr(int(reserved + outOfBand + ggepH + LGDQ + enableXML + firewalled + newSemantic, 2)) #16 bits = 2 bytes
		
		payload = minSpeed + criteria + '\x00' #2 bytes with minSpeed + search criteria terminated with 0x00
		
		guid = generateGUID
		payloadType = '\x80'
		ttl = 7
		hops = 0
		self.sendMessage(guid, payloadType, ttl, 0, payload)
		
	def sendQueryHit(self, numHits, port, host, speed):
		###################TODO
		pass

	def sendMessage(self, guid, payloadType, ttl, hops, payload):
		payloadLength = len(payload)
		
		header = guid + payloadTypes(payloadType) + ttl + hops + payloadLength
		
		package = header + payload
		
		self.wSocket.write(package)


	def generateGUID(self):
		guid = ''
		for i in range(7):
			guid = guid + chr(random.randint(0,255))
		guid = guid + '\xff'
		for i in range(6):
			guid = guid + chr(random.randint(0,255))
		guid = guid + '\x00'
		return guid



class Hosts:
	list = [ ]
	def __init__(self):
		self.list = [ ]
		self.list = self.load()
		if not self.list:
			debug('getting new hosts')
			self.list = self.gwebcache('http://gwc.dietpac.com:8080/?hostfile=1&client=QPYT&version=0.1')
		if not self.list:
			print 'Cannot find any hosts!'
			sys.exit()
		else:
			self.save(self.list)
	def gwebcache(self, url):
		try:
			hostList = urllib.urlopen(url).read(MAX_PAGE_LEN)
		except IOError, e:
			print 'I/O Error when reading URL',url,':\n',e.strerror
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
			print 'error writing hosts file'
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


#server.serve_forever()