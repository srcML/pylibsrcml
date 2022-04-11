# ********************************************************************************************************************************************************
# @file exception.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

from pylibsrcml.options import SRCML_STATUS_OK

# Checks return status value of libsrcml call
# Raises a srcML exception if status is not okay
def check_return(value) :
    if value == SRCML_STATUS_OK :
        return
    raise srcMLException("Recieved invalid return status: " + str(value))

# Class representing a srcml exception
class srcMLException(Exception) :

    def __init__(self, message) :
        self.message = message

    def __str__(self) :
        return self.message
