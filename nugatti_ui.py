# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nugatti_ui.ui'
#
# Created: Tue Apr 17 22:12:28 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!
#(c)mtsproductions

from qt import *
from kdeui import *

class Nugatti_ui(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Nugatti_ui")

        self.setSizeGripEnabled(1)

        Nugatti_uiLayout = QVBoxLayout(self,11,6,"Nugatti_uiLayout")

        self.tab = QTabWidget(self,"tab")

        self.Widget8 = QWidget(self.tab,"Widget8")
        Widget8Layout = QVBoxLayout(self.Widget8,11,6,"Widget8Layout")

        layoutSearchTop = QHBoxLayout(None,0,6,"layoutSearchTop")

        self.labelSearch = QLabel(self.Widget8,"labelSearch")
        layoutSearchTop.addWidget(self.labelSearch)

        self.search = QLineEdit(self.Widget8,"search")
        layoutSearchTop.addWidget(self.search)

        self.buttonSearch = QPushButton(self.Widget8,"buttonSearch")
        self.buttonSearch.setDefault(1)
        layoutSearchTop.addWidget(self.buttonSearch)
        Widget8Layout.addLayout(layoutSearchTop)

        self.listSearch = QListView(self.Widget8,"listSearch")
        self.listSearch.addColumn(self.__tr("Name"))
        Widget8Layout.addWidget(self.listSearch)

        layoutSearchBottom = QHBoxLayout(None,0,6,"layoutSearchBottom")

        self.labelResults = QLabel(self.Widget8,"labelResults")
        layoutSearchBottom.addWidget(self.labelResults)

        self.labelResultsNumber = QLabel(self.Widget8,"labelResultsNumber")
        layoutSearchBottom.addWidget(self.labelResultsNumber)

        self.labelSearchProgress = QLabel(self.Widget8,"labelSearchProgress")
        layoutSearchBottom.addWidget(self.labelSearchProgress)

        self.progressSearch = QProgressBar(self.Widget8,"progressSearch")
        layoutSearchBottom.addWidget(self.progressSearch)

        self.buttonDownload = QPushButton(self.Widget8,"buttonDownload")
        layoutSearchBottom.addWidget(self.buttonDownload)
        Widget8Layout.addLayout(layoutSearchBottom)
        self.tab.insertTab(self.Widget8,QString.fromLatin1(""))

        self.Widget9 = QWidget(self.tab,"Widget9")
        Widget9Layout = QVBoxLayout(self.Widget9,11,6,"Widget9Layout")

        self.listDownloads = QListView(self.Widget9,"listDownloads")
        self.listDownloads.addColumn(self.__tr("Name"))
        self.listDownloads.addColumn(self.__tr("Progress"))
        Widget9Layout.addWidget(self.listDownloads)

        layoutDownloadsBottom = QHBoxLayout(None,0,6,"layoutDownloadsBottom")

        self.labelDownloads = QLabel(self.Widget9,"labelDownloads")
        layoutDownloadsBottom.addWidget(self.labelDownloads)

        self.labelDownloadsNumber = QLabel(self.Widget9,"labelDownloadsNumber")
        layoutDownloadsBottom.addWidget(self.labelDownloadsNumber)
        spacerDownloads = QSpacerItem(360,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layoutDownloadsBottom.addItem(spacerDownloads)

        self.buttonCancelDownload = QPushButton(self.Widget9,"buttonCancelDownload")
        layoutDownloadsBottom.addWidget(self.buttonCancelDownload)
        Widget9Layout.addLayout(layoutDownloadsBottom)
        self.tab.insertTab(self.Widget9,QString.fromLatin1(""))
        Nugatti_uiLayout.addWidget(self.tab)

        layoutBottom = QHBoxLayout(None,0,6,"layoutBottom")

        self.buttonHelp = QPushButton(self,"buttonHelp")
        self.buttonHelp.setAutoDefault(1)
        layoutBottom.addWidget(self.buttonHelp)
        spacingLeftBottom = QSpacerItem(260,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layoutBottom.addItem(spacingLeftBottom)

        self.labelConnected = QLabel(self,"labelConnected")
        layoutBottom.addWidget(self.labelConnected)

        self.ledConnected = KLed(self,"ledConnected")
        layoutBottom.addWidget(self.ledConnected)
        spacerRightBottom = QSpacerItem(21,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layoutBottom.addItem(spacerRightBottom)

        self.buttonQuit = QPushButton(self,"buttonQuit")
        self.buttonQuit.setAutoDefault(1)
        self.buttonQuit.setDefault(0)
        layoutBottom.addWidget(self.buttonQuit)
        Nugatti_uiLayout.addLayout(layoutBottom)

        self.languageChange()

        self.resize(QSize(776,470).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonQuit,SIGNAL("clicked()"),self.accept)


    def languageChange(self):
        self.setCaption(self.__tr("Nugatti"))
        self.labelSearch.setText(self.__tr("Search:"))
        self.buttonSearch.setText(self.__tr("&search"))
        self.buttonSearch.setAccel(QKeySequence(self.__tr("Alt+S")))
        self.listSearch.header().setLabel(0,self.__tr("Name"))
        self.labelResults.setText(self.__tr("Results:"))
        self.labelResultsNumber.setText(self.__tr("<b>0</b>"))
        self.labelSearchProgress.setText(self.__tr("Search progress:"))
        self.buttonDownload.setText(self.__tr("&Download"))
        self.buttonDownload.setAccel(QKeySequence(self.__tr("Alt+D")))
        self.tab.changeTab(self.Widget8,self.__tr("S&earch"))
        self.listDownloads.header().setLabel(0,self.__tr("Name"))
        self.listDownloads.header().setLabel(1,self.__tr("Progress"))
        self.labelDownloads.setText(self.__tr("Downloads:"))
        self.labelDownloadsNumber.setText(self.__tr("<b>0</b>"))
        self.buttonCancelDownload.setText(self.__tr("&Cancel download"))
        self.buttonCancelDownload.setAccel(QKeySequence(self.__tr("Alt+C")))
        self.tab.changeTab(self.Widget9,self.__tr("Downloads"))
        self.buttonHelp.setText(self.__tr("&Help"))
        self.buttonHelp.setAccel(QKeySequence(self.__tr("F1")))
        self.labelConnected.setText(self.__tr("Connected:"))
        self.buttonQuit.setText(self.__tr("&QUIT"))
        self.buttonQuit.setAccel(QKeySequence(self.__tr("Ctrl+Q")))


    def __tr(self,s,c = None):
        return qApp.translate("Nugatti_ui",s,c)
