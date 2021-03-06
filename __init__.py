# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenHazardsPH
                                 A QGIS plugin
 A plugin to load publicly available geospatial hazard data created by various agencies in the Philippines.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-01-19
        copyright            : (C) 2020 by BNHR
        email                : hi@bnhr.xyz
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OpenHazardsPH class from file OpenHazardsPH.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .open_hazards_ph import OpenHazardsPH
    return OpenHazardsPH(iface)
