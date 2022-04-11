# ********************************************************************************************************************************************************
# @file srcml_direct_language_src2srcml.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# A straightforward translation of source code to the srcML format.
# Translates the file "a.cpp" to the srcML format in "a.cpp.xml":
# * The language is determined automatically from the source file extension
# * This creates a single-unit srcML file, i.e., a non-archive srcML
# * The srcML attribute filename will be the name of the file passed as the first
# parameter.

import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Translate from a source-code file to a srcML file
srcml.srcml("a.cpp", "a.cpp.xml")