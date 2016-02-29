from PyQt4 import QtGui
import sys
import DlgRasterLoader

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = DlgRasterLoader.DlgRasterLoader()
    dlg.show()
    retval = app.exec_()
    sys.exit(retval) 
