# ********************************************************************************************************************************************************
# @file __init__.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

__title__ = "pylibsrcml"
__license__ = "GNU GPL3"
__copyright__ = "Copyright (C) 2022 srcML, LLC (srcML.org)"
__version__ = "1.0.1"



import sys
import ctypes
from .srcml_archive import *
from .srcml_unit import *
from .globals import *
from .options import *
from .exception import srcMLException, srcMLNotFoundError
from ctypes import c_int, c_void_p, c_char_p, CFUNCTYPE

#srcml_archive = srcml_archive.srcml_archive
#srcml_unit = srcml_unit.srcml_unit

write_callback_t = CFUNCTYPE(c_int, c_void_p, c_char_p, c_int)
read_callback_t  = CFUNCTYPE(c_int, c_void_p, c_char_p, c_int)
close_callback_t = CFUNCTYPE(c_int, c_void_p)