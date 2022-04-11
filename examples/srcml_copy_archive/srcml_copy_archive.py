# ********************************************************************************************************************************************************
# @file srcml_copy_archive.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Copy an archive.

import importlib
import string
import sys
import difflib
import os
import ctypes
from pylibsrcml import srcml

# Open up an existing archive
archive = srcml.srcml_archive()
print("ARCHIVE CREATED")
archive.read_open_filename("project.xml")
print("ARCHIVE READ")

# Create a new srcml archive structure
# Options and attributes of cloned archive start the same as the original archive
oarchive = archive.clone()

# Open a srcML archive for output
oarchive.write_open_filename("project2.xml")
print("OTHER ARCHIVE OPENED FOR WRITING")

# Copy files from the input archive to the output archive
unit = archive.read_unit()
print("INITIAL READ")
while (unit != None) :
    print("IN LOOP")
    # Translate to srcml and append to the archive
    oarchive.write_unit(unit)
    unit = archive.read_unit()

# Close the archives
archive.close()
oarchive.close()