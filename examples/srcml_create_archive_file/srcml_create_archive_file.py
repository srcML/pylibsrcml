# ********************************************************************************************************************************************************
# @file srcml_create_archive_file.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Example program of the use of the Python API for srcML.
# Create an archive, file by file, with an output FILE*

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

# Setup our output file using a FILE
srcml_output = libc.fopen(str.encode("project.xml"), str.encode("w"))

# Open a srcML archive for output
archive.write_open_FILE(srcml_output)

# Add all the files to the archive
for x in sys.argv[1:] :

    unit = srcml.srcml_unit(archive)

    unit.set_language(archive.check_extension(x))

    # Translate to srcml
    srcml_input = libc.fopen(str.encode(x), str.encode("r"))
    unit.parse_FILE(srcml_input)

    # Append to the archive
    archive.write_unit(unit)

    libc.fclose(srcml_input)

# Close srcml archive
archive.close()

# File can now be closed also
libc.fclose(srcml_output)