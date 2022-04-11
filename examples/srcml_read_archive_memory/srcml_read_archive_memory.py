# ********************************************************************************************************************************************************
# @file srcml_read_archive_memory.py
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

s = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" revision="1.0.0" language="C++" filename="a.cpp" hash="2fa8b0b66d2187278e3cf81cf9d13e3296e6b43a"><comment type="line">// Sample program</comment>
<cpp:include>#<cpp:directive>include</cpp:directive> <cpp:file>&lt;iostream&gt;</cpp:file></cpp:include>

<function><type><name>int</name></type> <name>main</name><parameter_list>(<parameter><decl><type><name>int</name></type> <name>argc</name></decl></parameter>, <parameter><decl><type><name>char</name><modifier>*</modifier></type> <name><name>argv</name><index>[]</index></name></decl></parameter>)</parameter_list> <block>{<block_content>
    <expr_stmt><expr><name><name>std</name><operator>::</operator><name>cout</name></name> <operator>&lt;&lt;</operator> <literal type="string">"Hello World!"</literal> <operator>&lt;&lt;</operator> <name><name>std</name><operator>::</operator><name>endl</name></name></expr>;</expr_stmt>
</block_content>}</block></function></unit>
"""

# Create a new srcml archive
archive = srcml.srcml_archive()
archive.read_open_memory(s)

# Add all the files to the archive
unit = archive.read_unit()
while unit != None :
    # Can inquire about the current unit
    language = unit.get_language()
    filename = unit.get_filename()

    # Unparse and write to terminal
    unit.unparse_memory()
    print(unit.src())

    unit = archive.read_unit()

# Close the srcml archive
archive.close()