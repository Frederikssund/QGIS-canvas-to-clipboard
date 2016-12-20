# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CopyCanvasToClipboard
                                 A QGIS plugin
 This plugin makes a copy of the map canvas and place it in the clipboard
                             -------------------
        begin                : 2016-12-20
        copyright            : (C) 2016 by Bo Victor Thomsen - Municipality of Frederikssund
        email                : bvtho@frederikssund.dk
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
    """Load CopyCanvasToClipboard class from file CopyCanvasToClipboard.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .canvas_clipboard import CopyCanvasToClipboard
    return CopyCanvasToClipboard(iface)
