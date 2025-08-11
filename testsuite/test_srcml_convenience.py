# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_convenience.py

@copyright Copyright (C) 2014-2024 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()

src = "int a;\n"

asrcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp" hash="56f54d1636dfec63c3e1586e5e4bdc9a455bb9f6"><decl_stmt><decl><type><name>int</name></type> <name>a</name></decl>;</decl_stmt>
</unit>
"""

srcml_c = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C" filename="a.cpp" hash="56f54d1636dfec63c3e1586e5e4bdc9a455bb9f6"><decl_stmt><decl><type><name>int</name></type> <name>a</name></decl>;</decl_stmt>
</unit>
"""

srcml_full = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" url="url" filename="file" version="1" hash="56f54d1636dfec63c3e1586e5e4bdc9a455bb9f6"><s:decl_stmt><s:decl><s:type><s:name>int</s:name></s:type> <s:name>a</s:name></s:decl>;</s:decl_stmt>
</s:unit>
"""

with open("a.cpp",'w') as file:
    file.write(src)
with open("project.xml",'w') as file:
    file.write(asrcml)
with open("project.srcML",'w') as file:
    file.write(asrcml)
with open("project_c.xml",'w') as file:
    file.write(srcml_c)
with open("project",'w') as file:
    file.write(asrcml)
with open("project_full.xml",'w') as file:
    file.write(srcml_full)

#################################################
# srcml
################################################# 1
pylibsrcml.srcml("a.cpp","project.cpp.xml")
with open("project.cpp.xml",'r') as file:
    assert file.read() == asrcml
################################################# 2
pylibsrcml.set_language(pylibsrcml.srcMLLanguage.C)
pylibsrcml.srcml("a.cpp","project.c.xml")
with open("project.c.xml",'r') as file:
    assert file.read() == srcml_c
pylibsrcml.set_language(pylibsrcml.srcMLLanguage.NONE)
################################################# 3
pylibsrcml.set_filename("file")
pylibsrcml.set_url("url")
pylibsrcml.set_version("1")
pylibsrcml.register_namespace("s","http://www.srcML.org/srcML/src")
pylibsrcml.srcml("a.cpp","project_full.cpp.xml")
with open("project_full.cpp.xml",'r') as file:
    assert file.read() == srcml_full
################################################# 4
pylibsrcml.srcml("project.xml","inta.cpp")
with open("inta.cpp",'r') as file:
    assert file.read() == src
################################################# 5
pylibsrcml.srcml("project.srcML","inta.cpp")
with open("inta.cpp",'r') as file:
    assert file.read() == src
################################################# 6
pylibsrcml.set_language(pylibsrcml.srcMLLanguage.XML)
pylibsrcml.srcml("project","inta.cpp")
with open("inta.cpp",'r') as file:
    assert file.read() == src
pylibsrcml.set_language(pylibsrcml.srcMLLanguage.NONE)
################################################# 7
pylibsrcml.srcml("project_c.xml","inta.cpp")
with open("inta.cpp",'r') as file:
    assert file.read() == src
################################################# 8
pylibsrcml.srcml("project_full.xml","inta.cpp")
with open("inta.cpp",'r') as file:
    assert file.read() == src
################################################# 9
try:
    pylibsrcml.srcml("foo.c","foo.xml")
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.IO_ERROR
