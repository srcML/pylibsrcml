# ********************************************************************************************************************************************************
# @file srcml_create_archive_full.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Create an archive, file by file, with an output filename, showing
# most of the option features

import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Create a new srcml archive structure
archive = srcml.srcml_archive()

# Setup options and attributes
archive.set_version("211")
archive.set_tabstop(4)

# Treat .h as C++
archive.register_file_extension("h", srcml.SRCML_LANGUAGE_CXX)

# Change prefix of standard namespace
archive.register_namespace("s", "http://www.sdml.info/srcML/src")

# Default prefix is now for cpp namespace
archive.register_namespace("", "http://www.sdml.info/srcML/cpp")

# New prefix for further processing
archive.register_namespace("doc", "http://www.sdml.info/srcML/doc")

###############################
# Open and write to the archive
###############################

# Open an archive for output
archive.write_open_filename("project.xml")

# Add all files on the command line to the archive
for x in sys.argv[1:] :
    # Setup this entry
    unit = srcml.srcml_unit(archive)
    unit.set_language(srcml.SRCML_LANGUAGE_C)
    unit.set_filename(x)

    # Translate the entry to srcML
    unit.parse_filename(x)

    # Append unit to the archive
    archive.write_unit(unit)

###############################
# Finish up
###############################

# Close the srcML archive
archive.close()