# ********************************************************************************************************************************************************
# @file srcml_direct_language_srcml2src.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Translates the srcML file "a.cpp.xml" to the source-code file "a.cpp":
# * This creates a single-unit srcML file, i.e., a non-archive srcML
# * The srcML attribute filename will be the name of the file passed as the first
# parameter.

import sys
import difflib
import os
import ctypes
import stat
from pylibsrcml import srcml

# Translate from a srcML file to a source-code file
srcml.srcml("a.cpp.xml", "a.cpp")