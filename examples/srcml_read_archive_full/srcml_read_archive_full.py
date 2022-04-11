# ********************************************************************************************************************************************************
# @file srcml_read_archive_full.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Take an archive and extract the invidual units and write to a filesystem.

from stat import S_IWUSR
import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Create a new srcml archive structure
archive = srcml.srcml_archive()

# Open a srcml archive for input
archive.read_open_filename("project.xml")

# Add all the files to the archive
unit = archive.read_unit()
while unit != None :
    # Can inquire about the current unit
    language = unit.get_language()
    filename = unit.get_filename()

    # Unparse and write to a file
    unit.unparse_filename(filename)

    unit = archive.read_unit()

# Close the srcml archive
archive.close()