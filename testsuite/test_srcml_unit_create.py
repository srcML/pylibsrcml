# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_unit_create.py

@copyright Copyright (C) 2014-2024 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

import pylibsrcml

archive = pylibsrcml.srcMLArchive()
unit = archive.unit_create()

assert unit.get_language() == None
assert unit.get_filename() == None
assert unit.get_version() == None
assert unit.get_timestamp() == None
assert unit.get_hash() == None
assert unit.get_srcml() == None
assert unit.get_srcml_outer() == None
assert unit.get_srcml_inner() == None


archive.close()
