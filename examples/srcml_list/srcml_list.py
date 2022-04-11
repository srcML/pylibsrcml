# ********************************************************************************************************************************************************
# @file srcml_list.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Gather info from an archive from a given unit.

import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Create srcml archive
archive = srcml.srcml_archive()
archive.read_open_filename("project.xml")

unit = archive.read_unit()
while unit != None :
    print(unit.get_filename())
    unit = archive.read_unit()

archive.close()