# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_archive_create.py

@copyright Copyright (C) 2014-2025 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

import pylibsrcml

srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.version_string()}">

<unit revision="{pylibsrcml.version_string()}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>"""


archives = [pylibsrcml.srcMLArchive(),
            pylibsrcml.srcMLArchiveRead(srcml),
            pylibsrcml.srcMLArchiveWrite("output1.xml"),
            pylibsrcml.srcMLArchiveWriteString()]

for archive in archives:
    assert archive.get_language() == None
    assert archive.get_xml_encoding() == None if type(archive) != pylibsrcml.srcMLArchiveRead else "UTF-8"
    assert archive.get_src_encoding() == None
    assert archive.get_url() == None
    assert archive.get_version() == None
    assert archive.get_tabstop() == 8
    assert archive.get_namespace_size() == 1
    assert archive.get_namespace_uri(0) == "http://www.srcML.org/srcML/src"
    archive.close()
