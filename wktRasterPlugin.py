"""
/***************************************************************************
wktRaster
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
   
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources,os,sys
# Import the code for the dialog

class wktRaster: 

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):  
        # Create action that will start plugin configuration
        self.AddLayeraction = QAction(QIcon(":/plugins/wktraster/icon.png"), \
            "Add a Postgis Raster Layer", self.iface.mainWindow())
        self.LoadLayeraction = QAction(QIcon(":/plugins/wktraster/icon.png"), \
            "Load raster to Postgis", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.AddLayeraction, SIGNAL("triggered()"), self.callAddLayer) 
        QObject.connect(self.LoadLayeraction, SIGNAL("triggered()"), self.callLoader) 
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.AddLayeraction)
        # MCB 
        # self.iface.addToolBarIcon(self.LoadLayeraction)
        #add to Database menu
        nextAction = self.iface.mainWindow().menuBar().actions()[3].menu().actions()[3]
        self.iface.mainWindow().menuBar().actions()[3].menu().insertAction(nextAction,self.AddLayeraction)
        if hasattr(self.iface, "addPluginToDatabaseMenu"):
            self.iface.addPluginToDatabaseMenu("PostGIS &Raster", self.AddLayeraction)
            self.iface.addPluginToDatabaseMenu("PostGIS &Raster", self.LoadLayeraction)
        else:
            self.iface.addPluginToMenu("PostGIS &Raster", self.AddLayeraction)
            self.iface.addPluginToMenu("PostGIS &Raster", self.LoadLayeraction)
        #self.LoadLayeraction.setEnabled(False)
        

    def unload(self):
        # Remove the plugin menu item and icon
        if hasattr(self.iface, "removePluginDatabaseMenu"):
            self.iface.removePluginDatabaseMenu("&Postgis Raster", self.AddLayeraction)
            self.iface.removePluginDatabaseMenu("&Postgis Raster", self.LoadLayeraction)
        else:
            self.iface.removePluginMenu("&Postgis Raster", self.AddLayeraction)
            self.iface.removePluginMenu("&Postgis Raster", self.LoadLayeraction)
        self.iface.mainWindow().menuBar().actions()[4].menu().removeAction(self.AddLayeraction)
        self.iface.removeToolBarIcon(self.AddLayeraction)
        self.iface.removeToolBarIcon(self.LoadLayeraction)

    def callLoader(self):
        from DlgRasterLoader import DlgRasterLoader
        version=self.gdalVersion()
       # if version<1700: #checks if gdal is greater than 1.7
       #     QMessageBox.warning(self.iface.mainWindow(),"Error", "GDAL version incompatible with WktRaster.\n Your QGIS found GDAL version "+str(version))
       #     return 0
        # create and show the dialog 
        dlg = DlgRasterLoader()
        dlg.show()
        result = dlg.exec_() 
        
    def callAddLayer(self):
        from DlgAddRasterLayer import DlgAddRasterLayer
      #  if self.gdalVersion()<1700: #checks if gdal is greater than 1.7
      #      QMessageBox.warning(self.iface.mainWindow(),"Error", "GDAL version incompatible with WktRaster.")
      #      return 0
        # create and show the dialog 
        dlg = DlgAddRasterLayer()
        dlg.show()
        result = dlg.exec_() 
        
    def gdalVersion(self):
        from osgeo import gdal
        return int(gdal.VersionInfo())

