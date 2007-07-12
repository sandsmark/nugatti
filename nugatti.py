from qt import *
from nugatti_ui import *
from qpytella import *
import sys
from kdeui import *

class Nugatti(Nugatti_ui):
	
	#def __init__(self):
		
	
	def addSearchList(self):
		lvi = QListViewItem(self.listSearch)
		text = self.search.text().ascii()
		self.search.clear()
		lvi.setText(0, text)
		#f.listSearch.insertItem(e)
	
	def addDownloadList (self):
		lvi = QListViewItem(self.listDownloads)
		text = self.search.text().ascii()
	
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	f = Nugatti()
	f.show()
	#lol = tol()
	app.setMainWidget(f)
        app.connect(f.buttonQuit,SIGNAL("clicked()"),f.accept)
	app.connect(f.buttonSearch,SIGNAL("clicked()"),f.addSearchList)

	app.exec_loop()
