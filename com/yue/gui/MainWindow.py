from PyQt4 import QtGui, QtCore
from com.yue.gui.ResultShow import ResultShow
from com.yue.gui.main_ui import Ui_Form
from com.yue.urlconnect.connect import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.results = []
        self.resize(500, 500)
        self.initUi()
        self.initEvent()

    def initUi(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def initEvent(self):
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.propertyButton.clicked.connect(self.openAndSetPropertyWindow)
        self.ui.contentFileBrowser.clicked.connect(self.getFilePath)

        self.ui.paramAdd.clicked.connect(self.paramAdd)
        self.ui.paramRemove.clicked.connect(self.paramRemove)
        self.ui.headersAdd.clicked.connect(self.headersAdd)
        self.ui.headersRemove.clicked.connect(self.headersRemove)

        self.ui.getButton.clicked.connect(self.getEvent)
        self.ui.postButton.clicked.connect(self.postEvent)
        self.ui.putButton.clicked.connect(self.putEvent)
        self.ui.deleteButton.clicked.connect(self.deleteEvent)


    def openAndSetPropertyWindow(self):
        print("open properties windows")
        pass

    def getFilePath(self):
        print("get file path")

    def paramAdd(self):
        pass

    def paramRemove(self):
        pass

    def headersAdd(self):
        pass

    def headersRemove(self):
        pass

    def getEvent(self):
        print("run get event")
        url = self.ui.urlEdit.text()
        headers = self.getHeadersValue()
        paramenter = self.getParamentersValue()
        method = Get(url, headers, paramenter)
        method.run()
        print(method.getBody())
        print(method.getHeaders())
        result = ResultShow(method.getHeaders(), method.getBody())
        self.results.append(result)
        result.setModal(False)
        result.show()



    def postEvent(self):
        print("run post event")

    def putEvent(self):
        print("run put event")

    def deleteEvent(self):
        print("run delete event")

    def getHeadersValue(self):
        return None

    def getParamentersValue(self):
        return None
