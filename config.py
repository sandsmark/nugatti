import ConfigParser, os

config = ConfigParser.ConfigParser()
if (config.read(['nugatti.cfg', os.path.expanduser('~/.nugatti.cfg')]) == []):
	print "lol"