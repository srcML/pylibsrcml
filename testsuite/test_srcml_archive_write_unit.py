import pylibsrcml

srcml_a = f"""<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_b = f"""<s:unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="b.cpp"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>"""

utf8_srcml_no_xmldecl = f"""<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" url="test" filename="project" version="1"><comment type="block">/* ✓ */</comment>
</unit>"""

latin_srcml_no_xmldecl = f"""<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><comment type="block">/* Ã¾Ã¿ */</comment>
</unit>"""

srcml_old_uri_a = f"""<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

utf8_srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" url="test" version="1">

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><comment type="block">/* ✓ */</comment>
</unit>

</unit>
"""

utf8_srcml_latin = f"""<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" url="test" version="1">

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><comment type="block">/* &#10003; */</comment>
</unit>

</unit>
"""

latin_srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" url="test" version="1">

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><comment type="block">/* Ã¾Ã¿ */</comment>
</unit>

</unit>
"""

latin_srcml_latin = f"""<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" url="test" version="1">

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><comment type="block">/* þÿ */</comment>
</unit>

</unit>
"""

srcml_a_single_no_xmldecl = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_a_single = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

srcml_a_archive = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}">

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_old_uri_a_single_no_xmldecl = f"""<unit xmlns="http://www.sdml.info/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_first_old_uri_a_single_no_xmldecl  = f"""<unit xmlns="http://www.sdml.info/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_second_old_uri_a_single_no_xmldecl = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_b_single_no_xmldecl = f"""<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" url="test" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>"""

srcml_b_single = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>
"""

srcml_b_archive = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" url="test" version="1">

<s:unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="b.cpp"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>
"""

srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}">

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

<unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_ns = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" url="test" version="1">

<s:unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="b.cpp"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

<s:unit revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="b.cpp"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>
"""


#################################################
# srcml_archive_write_unit
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
archive.disable_hash()
unit = archive.unit_create()
unit.set_filename("a.cpp")
unit.set_language("C++")
unit.parse_memory("a;\n")

archive.write_unit(unit)

assert archive.is_solitary_unit()

s = archive.close()

assert s == srcml_a_single
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
unit = archive.unit_create()
unit.set_filename("a.cpp")
unit.set_language("C++")
unit.parse_memory("a;\n")

archive.write_unit(unit)

s = archive.close()

assert s == srcml_a_archive
################################################# 3
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
archive.set_language("C++")
archive.set_url("test")
archive.set_version("1")
archive.register_namespace("s","http://www.srcML.org/srcML/src")
unit = archive.unit_create()
unit.set_filename("b.cpp")
unit.parse_memory("b;\n")

archive.write_unit(unit)

unit = archive.unit_create()
unit.set_filename("b.cpp")
unit.parse_memory("b;\n")

archive.write_unit(unit)

s = archive.close()

assert s == srcml_ns
################################################# 4
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
unit = archive.unit_create()
unit.set_filename("a.cpp")
unit.set_language("C++")

unit.parse_memory("a;\n")

archive.write_unit(unit)

unit = archive.unit_create()
unit.set_filename("a.cpp")
unit.set_language("C++")
unit.parse_memory("a;\n")

archive.write_unit(unit)

s = archive.close()

assert s == srcml
################################################# 5
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
archive.disable_hash()
archive.register_namespace("s","http://www.srcML.org/srcML/src")
unit = archive.unit_create()
unit.set_filename("project")
unit.set_language("C++")
unit.set_version("1")
unit.parse_memory("b;\n")

archive.write_unit(unit)

s = archive.close()

assert s == srcml_b_single
################################################# 6
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()

archive.set_url("test")
archive.set_version("1")
archive.register_namespace("s","http://www.srcML.org/srcML/src")
unit = archive.unit_create()
unit.set_filename("b.cpp")
unit.set_language("C++")
unit.parse_memory("b;\n")

archive.write_unit(unit)

s = archive.close()

assert s == srcml_b_archive
################################################# 7
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
archive.set_xml_encoding("UTF-8")
archive.set_url("test")
archive.set_version("1")
unit = archive.unit_create()
unit.set_filename("project")
unit.set_language("C++")
unit.set_version("1")
unit.set_src_encoding("UTF-8")
archive.set_src_encoding("UTF-8")
code = "/* ✓ */\n"
unit.parse_memory(code)

archive.write_unit(unit)

s = archive.close()

assert s == utf8_srcml
################################################# 8
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
archive.set_xml_encoding("ISO-8859-1")
archive.set_language("C++")
archive.set_url("test")
archive.set_version("1")
unit = archive.unit_create()
unit.set_filename("project")
unit.set_language("C++")
unit.set_version("1")
unit.set_src_encoding("UTF-8")
code = "/* ✓ */\n"
unit.parse_memory(code)

archive.write_unit(unit)

s = archive.close()

assert s == utf8_srcml_latin
################################################# 9
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
archive.set_src_encoding("ISO-8859-1")
archive.set_xml_encoding("UTF-8")
archive.set_language("C++")
archive.set_url("test")
archive.set_version("1")
unit = archive.unit_create()
unit.set_filename("project")
unit.set_version("1")
code = "/* þÿ */\n"
unit.parse_memory(code)

assert unit.get_srcml_outer() == latin_srcml_no_xmldecl

archive.write_unit(unit)

s = archive.close()

assert s == latin_srcml
################################################# 10
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
archive.set_xml_encoding("ISO-8859-1")
archive.set_language("C++")
archive.set_url("test")
archive.set_version("1")
unit = archive.unit_create()
unit.set_filename("project")
unit.set_version("1")
code = "/* þÿ */\n"
unit.parse_memory(code)

assert unit.get_srcml_outer() == latin_srcml_no_xmldecl

archive.write_unit(unit)

s = archive.close()

assert s == latin_srcml_latin
################################################# 11
archive = pylibsrcml.srcMLArchiveWriteString()
iarchive = pylibsrcml.srcMLArchiveRead(srcml_a_archive)
unit = iarchive.read_unit()

archive.write_unit(unit)

s = archive.close()
iarchive.close()

assert s == srcml_a_archive
################################################# 12
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
archive.disable_hash()
unit = archive.unit_create()
unit.set_filename("a.cpp")
unit.set_language("C++")

unit.parse_memory("a;\n")
assert unit.get_srcml() == srcml_second_old_uri_a_single_no_xmldecl

archive.write_unit(unit)

s = archive.close()

assert s == srcml_a_single
################################################# 13
archive = pylibsrcml.srcMLArchiveWriteString()
archive.disable_hash()
unit = archive.unit_create()
unit.set_language("C++")
unit.parse_memory("a;\n")
unit.set_filename("a.cpp")

archive.write_unit(unit)

unit = archive.unit_create()
unit.set_filename("a.cpp")
unit.set_language("C++")
unit.parse_memory("a;\n")

archive.write_unit(unit)

s = archive.close()

assert s == srcml
################################################# 14
archive = pylibsrcml.srcMLArchiveWriteString()
unit = archive.unit_create()
try:
    archive.write_unit(unit)
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.UNINITIALIZED_UNIT
################################################# 15
archive = pylibsrcml.srcMLArchiveWriteString()
archive.set_language("C++")
archive.set_url("test")
archive.set_version("1")
archive.register_namespace("s","http://www.srcML.org/srcML/src")
try:
    archive.write_unit(0)
except pylibsrcml.srcMLTypeError:
    pass

s = archive.close()
#################################################
