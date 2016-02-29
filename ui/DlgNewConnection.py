# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DlgNewConnection.ui'
#
# Created: Mon Aug 29 21:23:55 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgNewConnection(object):
    def setupUi(self, DlgNewConnection):
        DlgNewConnection.setObjectName(_fromUtf8("DlgNewConnection"))
        DlgNewConnection.resize(227, 199)
        self.formLayout = QtGui.QFormLayout(DlgNewConnection)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEdit_5 = QtGui.QLineEdit(DlgNewConnection)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.label = QtGui.QLabel(DlgNewConnection)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(DlgNewConnection)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(DlgNewConnection)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinBox = QtGui.QSpinBox(DlgNewConnection)
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty(_fromUtf8("value"), 5432)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_3 = QtGui.QLabel(DlgNewConnection)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(DlgNewConnection)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(DlgNewConnection)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(DlgNewConnection)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtGui.QLabel(DlgNewConnection)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtGui.QLineEdit(DlgNewConnection)
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.buttonBox = QtGui.QDialogButtonBox(DlgNewConnection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.buttonBox)
        self.label_6 = QtGui.QLabel(DlgNewConnection)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)

        self.retranslateUi(DlgNewConnection)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgNewConnection.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgNewConnection.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgNewConnection.addNewConnection)
        QtCore.QMetaObject.connectSlotsByName(DlgNewConnection)

    def retranslateUi(self, DlgNewConnection):
        DlgNewConnection.setWindowTitle(QtGui.QApplication.translate("DlgNewConnection", "New PostgreSQL Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("DlgNewConnection", "newConnection", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgNewConnection", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("DlgNewConnection", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DlgNewConnection", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DlgNewConnection", "Database:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DlgNewConnection", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setText(QtGui.QApplication.translate("DlgNewConnection", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DlgNewConnection", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DlgNewConnection", "Connection name:", None, QtGui.QApplication.UnicodeUTF8))

