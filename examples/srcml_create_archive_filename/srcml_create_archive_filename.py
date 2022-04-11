# ********************************************************************************************************************************************************
# @file srcml_create_archive_filename.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Create an archive, file by file, with an output filename.

import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Create a new srcml archive structure
archive = srcml.srcml_archive()

# Open a srcML archive for output
archive.write_open_filename("project.xml")

# Add all files to the archive
for x in sys.argv[1:] :
    unit = srcml.srcml_unit(archive)
    unit.set_filename(x)

    # Translate to srcml and append to the archive
    unit.parse_filename(x)
    archive.write_unit(unit)

# Close srcML archive
archive.close()