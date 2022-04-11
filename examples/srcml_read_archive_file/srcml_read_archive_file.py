# ********************************************************************************************************************************************************
# @file srcml_read_archive_file.py
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

# Set up libc link
LIBC_PATH = ""
if sys.platform == "darwin" :
    LIBC_PATH = "libc.dylib"
elif sys.platform == "linux" :
    LIBC_PATH = "libc.so.6"
else :
    LIBC_PATH = "msvcrt.dll"

libc = ctypes.cdll.LoadLibrary(LIBC_PATH)

if sys.platform == "win32" or sys.platform == "cygin" :
    os.open = libc._open
    os.close = libc._close
    os.O_WRONLY = 1
    os.O_CREAT = 256
    os.O_RDONLY = 0

libc.fopen.restype = ctypes.c_void_p
libc.fopen.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

libc.fclose.restype = ctypes.c_int
libc.fclose.argtypes = [ctypes.c_void_p]

# Create a new srcml archive structure
archive = srcml.srcml_archive()

# Open a srcml archive for input
input = libc.fopen(str.encode("project.xml"), str.encode("r"))
archive.read_open_FILE(input)

# Add all files to the archive
unit = archive.read_unit()
while unit != None :
    # Can inquire about current unit
    language = unit.get_language()
    filename = unit.get_filename()

    # Unparse and write to a file
    output = libc.fopen(str.encode(filename), str.encode("w"))
    unit.unparse_FILE(output)

    libc.fclose(output)
    unit = archive.read_unit()

# Close the srcml archive
archive.close()