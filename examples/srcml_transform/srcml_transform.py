# ********************************************************************************************************************************************************
# @file srcml_transform.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Use XPath, XSLT, and RelaxNG.

from posixpath import isabs
from re import I
from stat import S_IWUSR
import sys
import difflib
import os
import ctypes
import stat
from unicodedata import numeric
from pylibsrcml import srcml

# Create an archive and read in input
iarchive = srcml.srcml_archive()
iarchive.read_open_filename("project.xml")

# Create a clone and open it for output
oarchive = iarchive.clone()
oarchive.write_open_filename("transform.xml")

# Append transforms
iarchive.append_transform_xpath("//src:unit")
iarchive.append_transform_xslt_filename("copy.xsl")
iarchive.append_transform_relaxng_filename("schema.rng")

# Close archives
iarchive.close()
oarchive.close()