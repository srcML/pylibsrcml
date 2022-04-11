# ********************************************************************************************************************************************************
# @file srcml.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

import sys
import ctypes
import pylibsrcml.srcml_archive
import pylibsrcml.srcml_unit
from pylibsrcml.globals import *
from pylibsrcml.options import *
from pylibsrcml.exception import srcMLException
from ctypes import c_int, c_void_p, c_char_p, CFUNCTYPE

srcml_archive = pylibsrcml.srcml_archive.srcml_archive
srcml_unit = pylibsrcml.srcml_unit.srcml_unit

write_callback_t = CFUNCTYPE(c_int, c_void_p, c_char_p, c_int)
read_callback_t  = CFUNCTYPE(c_int, c_void_p, c_char_p, c_int)
close_callback_t = CFUNCTYPE(c_int, c_void_p)