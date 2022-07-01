##
# @file __init__.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# The srcML Toolkit is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# The srcML Toolkit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with the srcML Toolkit; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#

__title__ = "pylibsrcml"
__license__ = "GNU GPL3"
__copyright__ = "Copyright (C) 2022 srcML, LLC (srcML.org)"
__version__ = "1.0.0-1"

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