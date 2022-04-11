# ********************************************************************************************************************************************************
# @file srcml_create_archive_memory.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Create an archive, file by file, with an output memory.

import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Create a new srcml archive structure
archive = srcml.srcml_archive()

# Open a srcml archive for output
archive.write_open_memory()

for x in sys.argv[1:] :
    unit = srcml.srcml_unit(archive)

    # Translate to srcml and append to the archive
    srcml_input = os.open(x, os.O_RDONLY, 0)
    buffer = str(os.read(srcml_input, 256))
    os.close(srcml_input)
    unit.set_language(archive.check_extension(x))

    unit.parse_memory(buffer)

    # Translate to srcml and append to the archive
    archive.write_unit(unit)

# Close archive
archive.close()

# Dump archive contents
print(archive.srcML())