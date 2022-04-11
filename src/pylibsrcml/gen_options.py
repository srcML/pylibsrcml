# ********************************************************************************************************************************************************
# @file gen_options.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

SRC2SRCML = src2srcml
SRCML2SRC = srcml2src

$SRC2SRCML ../../src/libsrcml/srcml.h | $SRCML2SRC --xpath "//cpp:define | //src:comment[following-sibling::*[1][self::cpp:define]]" | $SRCML2SRC -0 | tr "\0" "\n" | tail +2 | sed "s/#define *//" | sed "s/ [^ ]/ =&/" | sed "s/\/[*]* =/\#/" | sed "s/ *\*\///"
