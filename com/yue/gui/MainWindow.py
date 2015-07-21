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
        self.ui.closeButton.clicked.connect(QtGui.qApp.quit)
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
        self.ui.paramentersTableView.clicked.connect(self.paramClick)
        self.ui.headersTabelView.clicked.connect(self.headersClick)

    def openAndSetPropertyWindow(self):
        print("open properties windows")
        pass

    def getFilePath(self):
        print("get file path")

    def paramClick(self, index):
        row = index.row()
        print(row)
        key = self.ui.paramentersTabelModel.item(row, 0).text()
        value = self.ui.paramentersTabelModel.item(row, 1).text()
        self.ui.paramKeyEidt.setText(key)
        self.ui.paramValueEidt.setText(value)

    def paramAdd(self):
        key = self.ui.paramKeyEidt.text()
        value = self.ui.paramValueEidt.text()
        if key == "" or key == None:
            QtGui.QMessageBox.information(None, None, "请输入键", "确定")
            return
        if value == "" or value == None:
            QtGui.QMessageBox.information(None, None, "请输入值", "确定")
            return

        rows = self.ui.paramentersTabelModel.findItems(key, QtCore.Qt.MatchExactly, 0)
        if rows == None or len(rows) == 0:
            print("not find")
            row = []
            row.append(QtGui.QStandardItem(key))
            row.append(QtGui.QStandardItem(value))
            self.ui.paramentersTabelModel.appendRow(row)
            print("append success")
        else:
            #逐个去找
            for i in range(self.ui.paramentersTabelModel.rowCount()):
                if self.ui.paramentersTabelModel.item(i, 0).text() == key:
                    self.ui.paramentersTabelModel.setItem(i, 1, QtGui.QStandardItem(value))

    def paramRemove(self):
        key = self.ui.paramKeyEidt.text()
        self.ui.paramKeyEidt.setText("")
        self.ui.paramValueEidt.setText("")
        for i in range(self.ui.paramentersTabelModel.rowCount()):
                if self.ui.paramentersTabelModel.item(i, 0).text() == key:
                    self.ui.paramentersTabelModel.removeRow(i)
                    return

    def headersClick(self, index):
        row = index.row()
        print(row)
        key = self.ui.headersTabelModel.item(row, 0).text()
        value = self.ui.headersTabelModel.item(row, 1).text()
        self.ui.headersKeyEdit.setText(key)
        self.ui.headersValueEdit.setText(value)

    def headersAdd(self):
        key = self.ui.headersKeyEdit.text()
        value = self.ui.headersValueEdit.text()
        if key == "" or key == None:
            QtGui.QMessageBox.information(None, None, "请输入键", "确定")
            return
        if value == "" or value == None:
            QtGui.QMessageBox.information(None, None, "请输入值", "确定")
            return

        rows = self.ui.headersTabelModel.findItems(key, QtCore.Qt.MatchExactly, 0)
        if rows == None or len(rows) == 0:
            print("not find")
            row = []
            row.append(QtGui.QStandardItem(key))
            row.append(QtGui.QStandardItem(value))
            self.ui.headersTabelModel.appendRow(row)
        else:
            #逐个去找
            for i in range(self.ui.headersTabelModel.rowCount()):
                if self.ui.headersTabelModel.item(i, 0).text() == key:
                    self.ui.headersTabelModel.setItem(i, 1, QtGui.QStandardItem(value))

    def headersRemove(self):
        key = self.ui.headersKeyEdit.text()
        self.ui.headersKeyEdit.setText("")
        self.ui.headersValueEdit.setText("")
        for i in range(self.ui.headersTabelModel.rowCount()):
                if self.ui.headersTabelModel.item(i, 0).text() == key:
                    self.ui.headersTabelModel.removeRow(i)
                    return

    def getEvent(self):
        print("run get event")
        url = self.ui.urlEdit.text()
        headers = self.getHeadersValue()
        paramenter = self.getParamentersValue()
        method = Get(url, headers, paramenter)
        method.run()
        if method.responseStatus != 200:
            QtGui.QMessageBox.information(None, None, "statusCode: " + str(method.responseStatus), "确定")
            return

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
        value = {}
        for i in range(self.ui.paramentersTabelModel.rowCount()):
            value[self.ui.paramentersTabelModel.item(i, 0).text()] = self.ui.paramentersTabelModel.item(i, 1).text()
        print(value)
        return value

    #################################################################
    #  below is window event and others
    #################################################################