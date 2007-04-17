from qt import *
from nugatti_ui import *
from qpytella import *
import sys
class tol:
	def lol(self):
		print 'lol'
	
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	
	f = Nugatti()
	f.show()
	lol = tol()
	app.setMainWidget(f)
        app.connect(f.buttonQuit,SIGNAL("clicked()"),f.accept)
	app.connect(f.buttonSearch,SIGNAL("clicked()"),lol.lol())

	app.exec_loop()
	
