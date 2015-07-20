# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created: Mon Jul 20 23:18:06 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(638, 574)
        self.headerText = QtGui.QPlainTextEdit(Form)
        self.headerText.setGeometry(QtCore.QRect(80, 20, 531, 171))
        self.headerText.setObjectName(_fromUtf8("headerText"))
        self.bodyText = QtGui.QPlainTextEdit(Form)
        self.bodyText.setGeometry(QtCore.QRect(80, 210, 531, 301))
        self.bodyText.setObjectName(_fromUtf8("bodyText"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.closeButton = QtGui.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(540, 530, 75, 23))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "headers", None))
        self.label_2.setText(_translate("Form", "body", None))
        self.closeButton.setText(_translate("Form", "Close", None))

