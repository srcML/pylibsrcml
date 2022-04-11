# ********************************************************************************************************************************************************
# @file srcml_create_archive_fd.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

#  Example program of the use of the Python API for srcML.
#  Create an archive, file by file, with an output file descriptor

from stat import S_IWUSR
import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Create a new srcml archive structure
archive = srcml.srcml_archive()

# Setup our output file using a file descriptor
srcml_output = os.open("project.xml", os.O_WRONLY | os.O_CREAT, stat.S_IRUSR | stat.S_IWUSR)

# Open a srcML archive for output
archive.write_open_fd(srcml_output)

# Add all the files to the archive
for x in sys.argv[1:] :

    unit = srcml.srcml_unit(archive)

    unit.set_language(archive.check_extension(x))

    # Translate to srcml
    srcml_input = os.open(x, os.O_RDONLY, 0)
    unit.parse_fd(srcml_input)

    # Append to the archive
    archive.write_unit(unit)

    os.close(srcml_input)

# Close srcml archive
archive.close()

# File can now be closed also
os.close(srcml_output)