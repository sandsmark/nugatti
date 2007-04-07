import random
guid = ''
for i in range(7):
	guid = guid + chr(random.randint(0,255))
guid = guid + '\xff'
for i in range(6):
	guid = guid + chr(random.randint(0,255))
guid = guid + '\x00'

print len(guid)
print guid