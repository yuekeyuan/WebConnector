from PyQt4 import QtCore, QtGui
from com.yue.gui.result_ui import *

class ResultShow(QtGui.QDialog):
    def __init__(self,headers=None, body=None):
        super(ResultShow, self).__init__()
        self.headers = headers
        self.body = body
        self.initUi()

    def initUi(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.updataUi()
        self.initEvent()

    def setData(self, headers=None, body=None):
        self.headers = headers
        self.body = body
        self.updataUi()

    def initEvent(self):
        self.ui.closeButton.clicked.connect(self.close)

    def updataUi(self):
        if self.headers:
            self.ui.headerText.setPlainText(self.headers)
        else:
            self.ui.headerText.setPlainText("")

        if self.body:
            self.ui.bodyText.setPlainText(self.body)
        else:
            self.ui.bodyText.setPlainText("")