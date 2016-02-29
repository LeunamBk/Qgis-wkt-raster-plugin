"""
/***************************************************************************
wktRasterDialog
A QGIS plugin
Allows connecting to database and choose wktraster tables.
                             -------------------
begin                : 2010-10-20 
copyright            : (C) 2010 by Mauricio de Paulo
email                : mauricio.dev@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os,sys
"""sys.path.append("/usr/lib/eclipse/plugins/org.python.pydev.debug_2.2.1.2011071313/pysrc/")
import pydevd
pydevd.settrace()"""

from PyQt4 import QtCore, QtGui 
from PyQt4.QtCore import QSettings
from ui.DlgAddRasterLayer import Ui_DlgAddRasterLayer
import conn
from qgis.core import *




# create the dialog for zoom to point
class DlgAddRasterLayer(QtGui.QDialog,Ui_DlgAddRasterLayer):
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.settings = QSettings('wktRaster', 'foo')
              
        # Set up the user interface from Designer. 
        self.setupUi(self) 
        dblist = conn.listDatabases()
        self.comboBox.addItems(dblist.keys())
#        if len(dblist.keys()) > 0:
#            self.updateUIMode()

        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.listTables)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.savePreselectTable)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellClicked(int,int)"), self.copyTableName)
        self.pushButton.clicked.connect(lambda:self.listLayers())
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("currentIndexChanged(int)"), self.listLayers)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)
        # set preselected table in comboBox
        self.setPreSelectedTable()        
        
    def getCurrentConnection(self):
        return self.comboBox.currentText() 
    
    def getTable(self):
        return self.lineEdit.text()
        
    def savePreselectTable(self):
        self.settings.setValue('lastTable', str(self.comboBox.currentText()))
        # This will write the setting to the platform specific storage.
        del self.settings
    
    def setPreSelectedTable(self):
        # set last selected table 
        if(self.getPreselectTable()):
            index = self.comboBox.findText(self.getPreselectTable(), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox.setCurrentIndex(index)

    def getPreselectTable(self):
        return self.settings.value('lastTable')
    
    def listTables(self,i=0):
        """This method connects to the database using a python Postgres connection and reads the raster_columns table"""
        connstring=conn.getConnString(self,self.getCurrentConnection())
        tables=conn.listTables(self,connstring) #returns a list of pairs (index, value)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
         # set accesable tables        
        #availableTables = ['crumapsmean100', 'single_recon_temp_png', 'monthly_recon_temp', 'ogr_test','n12']
        for table in tables:
            #if any(table[0][1].text() in s for s in availableTables):
            self.tableWidget.insertRow(0)
            for pair in table:
                self.tableWidget.setItem(0,pair[0],pair[1])

    def listLayers(self,i=0):
        """This method connects to the database using a python Postgres connection and reads the raster_columns table"""
        connstring=conn.getConnString(self,self.getCurrentConnection())
        lables, tables=conn.listTableLayers(self, connstring, self.getTable(), self.lineEdit_2.text()) #returns a list of pairs (index, value)
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        # set table header lables
        columns = len(lables)
        print 'lenlen', columns
        self.tableWidget_2.setColumnCount(columns)
        
        # set table header lables
        for i, label in enumerate(lables):
            self.tableWidget_2.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(label[i]))
     
            # set accesable tables        
        for table in tables:
            self.tableWidget_2.insertRow(0)
            for idx, pair in enumerate(table):
                #tValue = QtGui.QLineEdit(str(pair[0]))
                self.tableWidget_2.setItem(0, idx, pair)
     
 
    def copyTableName(self,i,j):
        #test if the table is external. GDAL doesn't suport external yet.
        if (self.tableWidget.item(i,4).text()=="True"):
            self.lineEdit.setText("GDAL does not support external tables yet.")
        else:
            self.lineEdit.setText(self.tableWidget.item(i,0).text()+"."+self.tableWidget.item(i,1).text())

    def getMode(self):
        mode=['convexhull','row','table','db']
        return (mode[1])
    '''
    def listRIds(self,i=-1,j=-1):
        if (i != -1):
            if (self.getMode()=='row'): 
                connstring=str(conn.getConnString(self,self.getCurrentConnection()))
                rids=conn.listRIDs(self, connstring, str(self.tableWidget.item(i,0).text())+"."+str(self.tableWidget.item(i,1).text()) )
                self.ridComboBox.clear()
                self.ridComboBox.addItems(rids)
    '''
    
    def updateUIMode(self,i=0):
        mode=self.getMode()
        if (mode=='db'):
            self.tableWidget.setVisible(False)
            self.label_2.setVisible(False)
            self.lineEdit.setVisible(False)
        elif (mode=='row'):
            self.tableWidget.setVisible(True)
            self.label_2.setVisible(True)
            self.lineEdit.setVisible(True)
            self.listTables()
        else: #(convexhull and table)
            self.tableWidget.setVisible(True)
            self.label_2.setVisible(True)
            self.lineEdit.setVisible(True)
            self.listTables()
        self.adjustSize()

    #===================================================================
    # given a tablewidget which has a selected row...
    # return the column value in the same row which corresponds to a given column name
    # fyi: columnname is case sensitive
    #===================================================================
    def getQueryIdent(self, widget, columnnames):
        queryString = ''
        sCount = 0        
        row = widget.currentItem().row()
        #col = widget.currentItem().column()
        #loop through headers and find column number for given column name
        headercount = widget.columnCount()
        for x in range(0,headercount,1):
            headertext = widget.horizontalHeaderItem(x).text()
            if any(headertext in s for s in columnnames):
                cValue =  widget.item(row,x).text()
                if sCount == 0:    
                    if(headertext == 'event_id_array'):
                        queryString += str(' '+ 'uniq(sort(event_id_array::int[])) = uniq(sort(array'+cValue+'))' + ' ')
                    else:
                        queryString += str(' '+headertext + ' = ' + cValue + ' ')
                else:
                    if(headertext == 'event_id_array'):
                        queryString += str(' AND '+ 'uniq(sort(event_id_array::int[])) = uniq(sort(array'+cValue+'))' + ' ')
                    else:
                        queryString += str(' AND '+headertext + ' = ' + cValue + ' ')

                            
                sCount = sCount + 1
   
        print queryString
        return queryString
    
    # run method that performs all the real work
    def run(self): 
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
        table=str(self.getTable()).split(".") #splits table name from schema
        if (table[0]=="GDAL does not support external tables yet"):
            QtGui.QMessageBox.warning(self,"Error", "GDAL does not support external tables yet")
            return False
        connstring = str(conn.getConnString(self,self.getCurrentConnection()))
        mode=self.getMode()
        name=""
        
        #setting table name and mode 
        if (mode!='db'): #connection string doesn't include table and schema if the whole db is being read
            if len(table)>1: #checking if there is schema in the table name
                name+=str(table[0])
                connstring+=" schema="+str(table[0])
            connstring+=' table='+str(table[-1])
            name+="."+str(table[-1])
            if (mode=='row'):
                # get sleected row and prepare sql WHERE string array defines selector columns     
                qString = self.getQueryIdent(self.tableWidget_2,['year','month','event_id','event_id_array']) 
                connstring+=' mode=1 where=\''+qString+'\''
            elif (mode=='table'):
                connstring+=' mode=2'
        rlayer=None
        try:
            if (mode=='convexhull'):#asked for a vector layer
                uri=QgsDataSourceURI(connstring[4:]) #removes the PG: from the connstring
                uri.setDataSource("", "(select rid,st_convexhull(rast) as geom from "+name+")", "geom", "", "rid")
                rlayer=QgsVectorLayer(uri.uri(),name,'postgres')
            else:
                rlayer = QgsRasterLayer(connstring, name)
                rlayer.setNoDataValue(9999)
                rlayer.rasterTransparency().initializeTransparentPixelList(9999)
        except :
            print ''
                #TODO:   QtGui.QMessageBox.warning(None,"Error","Could not load layer.")        
                #                 
                #workaround for the nodata problem sets properties to fix the bug
        
        
        #try to add layer to qgis.
        if rlayer: 
            if rlayer.isValid():
                status=QgsMapLayerRegistry.instance().addMapLayer(rlayer)
            else:
                QtGui.QMessageBox.warning(self,"Error", "Could not load "+connstring)
        QtGui.QApplication.restoreOverrideCursor()

