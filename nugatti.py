# -*- coding: utf-8 -*-

####################################
# NUGATTI (c)  martin t. sandsmark #
#  http://www.mts-productions.com  #
####################################

from qt import *
from nugatti_ui import *
#from qpytella import *
import sys
from kdeui import KLed

class Nugatti(Nugatti_ui):
	
	#def __init__(self):
	connected = 0
	
	def addSearchList(self):
		lvi = QListViewItem(self.listSearch)
		text = self.search.text().ascii()
		self.search.clear()
		lvi.setText(0, text)
		#f.listSearch.insertItem(e)
	
	def addDownloadList (self):
		lvi = QListViewItem(self.listDownloads)
		text = self.search.text().ascii()
		
	def toggleConnected(self):
		
		if (self.connected == 0):
			self.ledConnected.setState(KLed.State(0))
			self.connected = 1
			#print dir(KLed.state)
		else:
			self.ledConnected.setState(KLed.State(1))
			self.connected = 0
			#print dir(KLed.state)
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	f = Nugatti()
	f.show()
	#lol = tol()
	app.setMainWidget(f)
        app.connect(f.buttonQuit, SIGNAL("clicked()"),f.accept)
	app.connect(f.buttonSearch, SIGNAL("clicked()"),f.addSearchList)
	app.connect(f.buttonHelp, SIGNAL("clicked()"), f.toggleConnected)

	app.exec_loop()
