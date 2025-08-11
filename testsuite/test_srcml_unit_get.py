# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_unit_get.py

@copyright Copyright (C) 2014-2024 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

import pylibsrcml

archive = pylibsrcml.srcMLArchive()
archive.enable_hash()


#################################################
# srcml_unit_get_src_encoding
################################################# 1
unit = archive.unit_create()
assert unit.get_src_encoding() == None
################################################# 2
unit = archive.unit_create()
unit.set_src_encoding("foo")
assert unit.get_src_encoding() == "foo"
#################################################


#################################################
# srcml_unit_get_revision
################################################# 1
unit = archive.unit_create()
unit.set_language("C++")
assert unit.get_revision() == pylibsrcml.version_string()
#################################################


#################################################
# srcml_unit_get_language
################################################# 1
unit = archive.unit_create()
assert unit.get_language() == None
################################################# 2
unit = archive.unit_create()
unit.set_language("C++")
assert unit.get_language() == "C++"
#################################################


#################################################
# srcml_unit_get_filename
################################################# 1
unit = archive.unit_create()
assert unit.get_filename() == None
################################################# 2
unit = archive.unit_create()
unit.set_filename("main.cpp")
assert unit.get_filename() == "main.cpp"
#################################################


#################################################
# srcml_unit_get_version
################################################# 1
unit = archive.unit_create()
assert unit.get_version() == None
################################################# 2
unit = archive.unit_create()
unit.set_version("1.5")
assert unit.get_version() == "1.5"
#################################################


#################################################
# srcml_unit_get_timestamp
################################################# 1
unit = archive.unit_create()
assert unit.get_timestamp() == None
################################################# 2
unit = archive.unit_create()
unit.set_timestamp("Fri Nov 30 14:15:27 EST 2018")
assert unit.get_timestamp() == "Fri Nov 30 14:15:27 EST 2018"
#################################################


#################################################
# srcml_unit_get_hash
################################################# 1
unit = archive.unit_create()
assert unit.get_hash() == None
################################################# 2
unit = archive.unit_create()
unit.set_language("C++")
unit.parse_memory("a;")

assert archive.has_hash()
assert unit.get_hash() == "a301d91aac4aa1ab4e69cbc59cde4b4fff32f2b8"
#################################################


#################################################
# srcml_unit_get_srcml_outer
################################################# 1
unit = archive.unit_create()
assert unit.get_srcml_outer() == None
################################################# 2
unit = archive.unit_create()
assert archive.has_hash()
unit.set_language("C++")
unit.parse_memory("a;")

assert unit.get_srcml_outer() == '<unit revision="1.0.0" language="C++" hash="a301d91aac4aa1ab4e69cbc59cde4b4fff32f2b8"><expr_stmt><expr><name>a</name></expr>;</expr_stmt></unit>'
#################################################


#################################################
# srcml_unit_get_srcml
################################################# 1
unit = archive.unit_create()
assert unit.get_srcml() == None
################################################# 2
unit = archive.unit_create()
assert archive.has_hash()
unit.set_language("C++")
unit.parse_memory("a;")

assert unit.get_srcml() == '<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0" language="C++" hash="a301d91aac4aa1ab4e69cbc59cde4b4fff32f2b8"><expr_stmt><expr><name>a</name></expr>;</expr_stmt></unit>'
#################################################


#################################################
# srcml_unit_get_loc
################################################# 1
locs = [142,35,820,115,399,119,70,51,16,38,97,43,93,32,104,31,17,68,46,170,98,95,41,254,34,92,52]
archive = pylibsrcml.srcMLArchiveRead("data_big.xml")
i = 0
for unit in archive:
    assert unit.get_loc() == locs[i]
    i += 1
#################################################


archive.close()
