from qt import *
from nugatti_ui import *
from qpytella import *
import sys


if __name__ == "__main__":
	app = QApplication(sys.argv)
	f = Nugatti()
	f.show()
	app.setMainWidget(f)
	app.exec_loop()