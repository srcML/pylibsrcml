# ********************************************************************************************************************************************************
# @file srcml_sort_archive.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Sorts an archive in alphabetical filename order.
# Not especially useful, but does show how units can be rearranged.

from stat import S_IWUSR
import sys
import difflib
import os
import ctypes
import stat
from unicodedata import numeric
from pylibsrcml import srcml

num_units = 0
units = [None] * 10
inputFile = "project.xml"
outputFile = "project_tmp.xml"

# Open an existing archive
iarchive = srcml.srcml_archive()

# Create a new srcml archive structure
# Options and attributes of cloned archive start the same as
# the original archive
oarchive = iarchive.clone()
iarchive.read_open_filename(inputFile)
while True :
    units[num_units] = iarchive.read_unit()
    if(units[num_units] == None) :
        break
    num_units += 1

i = 1
while i < num_units :
    j = i

    while j > 0 :
        if units[j].get_filename() == units[j - 1].get_filename() :
            tmp_unit = units[j]
            units[j] = units[j - 1]
            units[j - 1] = tmp_unit
        else :
            break

        j -= 1

    i += 1

# Open a srcml archive for output
oarchive.write_open_filename(outputFile)

i = 0 
for i in range(0, num_units) :
    # Copy the files from the input archive to the output archive
    # Translate to srcml and append to the archive
    oarchive.write_unit(units[i])

# Close archives
oarchive.close()
iarchive.close()