"""
/***************************************************************************
         MultiQml  -  A QGIS plugin to apply single qml to multiple raster 
		 				and vector layers
                             -------------------
    begin                : 2008-12-25
    copyright            : (C) 2008 by Lynx
    email                : lynx21.12.12@gmail.com
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

import sys

from PyQt4.QtCore import QObject, SIGNAL
from PyQt4.QtGui import QMainWindow, QApplication, QAction, QIcon, \
	QDialog, QLabel, QWidget, QVBoxLayout

from multiqml import MultiQmlDlg

import resources

class MultiQmlPlugin():
	def __init__( self, iface ):
		self.iface = iface

	def initGui( self ):
		myTr = QWidget()
		self.actionRun = QAction( QIcon( ":/plugins/multiqml/icon.png" ),\
			myTr.tr( "MultiQml" ), self.iface.mainWindow() )
		self.actionRun.setWhatsThis( myTr.tr( "Apply single qml to multiple raster and vector layers.") )
		self.actionAbout = QAction( myTr.tr( "About" ), self.iface.mainWindow() )

		QObject.connect( self.actionRun, SIGNAL( "activated()" ), self.run )
		QObject.connect( self.actionAbout, SIGNAL( "activated()" ), self.about )

		self.iface.addToolBarIcon(self.actionRun)
		self.iface.addPluginToMenu( myTr.tr( "&MultiQml" ), self.actionRun )
		self.iface.addPluginToMenu( myTr.tr( "&MultiQml" ), self.actionAbout )

		self.isMultiQmlRun = False

	def unload( self ):
		myTr = QWidget()
		self.iface.removePluginMenu( myTr.tr( "&MultiQml" ), self.actionRun )
		self.iface.removePluginMenu( myTr.tr( "&MultiQml" ), self.actionAbout )
		self.iface.removeToolBarIcon(self.actionRun)

	def run( self ):
		if not self.isMultiQmlRun:
			self.isMultiQmlRun = True
			dlgMain = MultiQmlDlg( self.iface.mainWindow() )
			dlgMain.show()
			dlgMain.exec_()
			self.isMultiQmlRun = False

	def about( self ):
		myTr = QWidget()
		dlgAbout = QDialog( self.iface.mainWindow() )
		lines = QVBoxLayout( dlgAbout )
		lines.addWidget( QLabel( myTr.tr( "<b>MultiQml:</b>" ) ) )
		lines.addWidget( QLabel( myTr.tr( "    Apply single qml to multiple raster and vector layers." ) ) )
		lines.addWidget( QLabel( myTr.tr( "<b>Developers:</b>" ) ) )
		lines.addWidget( QLabel( myTr.tr( "    Lynx (lynx21.12.12@gmail.com)" ) ) )
		lines.addWidget( QLabel( myTr.tr( "    Maxim Dubinin (sim@gis-lab.info)" ) ) )
		lines.addWidget( QLabel( myTr.tr( "<b>Link:</b>") ) )
		link = QLabel( "<a href=\"http://gis-lab.info/qa/qgis-multiqml-eng.html\">http://gis-lab.info/qa/qgis-multiqml-eng.html</a>" )
		link.setOpenExternalLinks( True )
		lines.addWidget( link )

		dlgAbout.exec_()

if __name__ == "__main__":
	app = QApplication( sys.argv )
	pluginWidget = MultiQmlPlugin( None )
	pluginWidget.run(  )
	sys.exit( app.exec_(  ) )
