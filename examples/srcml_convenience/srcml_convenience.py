# ********************************************************************************************************************************************************
# @file srcml_convenience.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the convenience funcion Python API for srcML.

import importlib
import sys
import difflib
import os
import ctypes
from pylibsrcml import srcml

# Setup options and attributes
srcml.set_version("211")
srcml.set_tabstop(4)

# Treat ".h" as C++
srcml.register_file_extension("h", srcml.SRCML_LANGUAGE_CXX)

# Change prefix of standard namespace
srcml.register_namespace("s", "http://www.sdml.info/srcML/src")

# Default prefix is now for cpp namespace
srcml.register_namespace("", "http://www.sdml.info/srcML/cpp")

# New prefix for further processing
srcml.register_namespace("doc", "http://www.sdml.info/srcML/doc")

# Translates source code file "main.cpp" to srcML file "main.cpp.xml".
# - Translate using the above global options
# - The language will be automatically based on the extension of the input (first) filename
# - Since there is only a single input file, the output file will be a non-archive by default.
# Convenience function can also convert to archive
srcml.srcml("main.cpp", "main.cpp.xml")