# ********************************************************************************************************************************************************
# @file srcml_split_archive.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Split an archive into two, one for .h files and one for other extensions

from posixpath import isabs
from stat import S_IWUSR
import sys
import difflib
import os
import ctypes
import stat
from unicodedata import numeric
from pylibsrcml import srcml

# Open an existing archive
iarchive = srcml.srcml_archive()
iarchive.read_open_filename("project.xml")

# Create a new srcml archive structure
# Options and attributes of cloned archive start the same as
# the original archive
includearchive = iarchive.clone()
otherarchive = iarchive.clone()

# Open srcml archive for output
includearchive.write_open_filename("project_include.xml")
otherarchive.write_open_filename("project_other.xml")

# Copy the files from the input archive to the output archive
unit = iarchive.read_unit()
while unit != None :
    # Get the filename
    filename = unit.get_filename()

    # Add to archive according to file type
    if ".h" == filename[len(filename)-2:len(filename)] :
        includearchive.write_unit(unit)
    else :
        otherarchive.write_unit(unit)

    unit = iarchive.read_unit()
    


# Close the archives
includearchive.close()
otherarchive.close()
iarchive.close()