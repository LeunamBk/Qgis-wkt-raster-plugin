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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Load Postgis Raster to QGIS" 
def description():
  return "Allows connecting to database and choose wktraster tables."
def version(): 
  return "Version 0.5.4" 
def qgisMinimumVersion():
  return "1.7"
def classFactory(iface): 
  # load wktRaster class from file wktRaster
  from wktRasterPlugin import wktRaster 
  return wktRaster(iface)


