from com.yue.gui.MainWindow import MainWindow
from com.yue.gui.ResultShow import *
from PyQt4 import QtGui
import sys
from com.yue.urlconnect.connect import Get


if __name__ == "__main__":
    #get = Get("http://www.baidu.com")
    #get.run()

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
