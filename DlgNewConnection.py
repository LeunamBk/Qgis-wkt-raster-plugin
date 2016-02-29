import os,sys
"""sys.path.append("/usr/lib/eclipse/plugins/org.python.pydev.debug_2.2.1.2011071313/pysrc/")
import pydevd
pydevd.settrace()"""

from PyQt4 import QtCore, QtGui 
from ui.DlgNewConnection import Ui_DlgNewConnection

# create the dialog for zoom to point
class DlgNewConnection(QtGui.QDialog,Ui_DlgNewConnection):
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        # Set up the user interface from Designer. 
        self.setupUi(self)
    def addNewConnection(self):
        settings = QtCore.QSettings()
        key = "/PostgreSQL/connections/"+str(self.lineEdit_5.text())
        settings.setValue(key + "/host", QtCore.QVariant(str(self.lineEdit.text())))
        settings.setValue(key + "/port", QtCore.QVariant(int(self.spinBox.value())))
        settings.setValue(key + "/database", QtCore.QVariant(str(self.lineEdit_2.text())))
        settings.setValue(key + "/username", QtCore.QVariant(str(self.lineEdit_3.text())))
        settings.setValue(key + "/password", QtCore.QVariant(str(self.lineEdit_4.text())))
        settings.setValue("/PostgreSQL/connections/selected", QtCore.QVariant(str(self.lineEdit_5.text())))
        settings.sync()

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = DlgNewConnection()
    dlg.show()
    retval = app.exec_()
    sys.exit(retval)