import pylibsrcml

srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

unit_text = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

with open("project.xml",'w') as file:
    file.write(srcml)


#################################################
# Archive with
################################################# 1
with pylibsrcml.srcMLArchiveRead("project.xml") as archive:
    assert archive.read_unit().get_srcml() == unit_text
assert archive.closed
################################################# 2
with pylibsrcml.srcMLArchiveRead(srcml) as archive:
    assert archive.read_unit().get_srcml() == unit_text
assert archive.closed
################################################# 3
with pylibsrcml.srcMLArchiveWrite("project.xml") as archive:
    archive.enable_solitary_unit()
    archive.disable_hash()
    unit = archive.unit_create()
    unit.set_filename("a.cpp")
    unit.set_language("C++")
    unit.parse_memory("a;\n")
    archive.write_unit(unit)
assert archive.closed
with open("project.xml",'r') as file:
    assert file.read() == srcml
################################################# 4
with open("project.xml",'w') as file, pylibsrcml.srcMLArchiveWrite(file) as archive:
    archive.enable_solitary_unit()
    archive.disable_hash()
    unit = archive.unit_create()
    unit.set_filename("a.cpp")
    unit.set_language("C++")
    unit.parse_memory("a;\n")
    archive.write_unit(unit)
assert archive.closed
assert file.closed
with open("project.xml",'r') as file:
    assert file.read() == srcml
################################################# 5
with pylibsrcml.srcMLArchiveWriteString() as archive:
    archive.enable_solitary_unit()
    archive.disable_hash()
    unit = archive.unit_create()
    unit.set_filename("a.cpp")
    unit.set_language("C++")
    unit.parse_memory("a;\n")
    archive.write_unit(unit)
assert archive.closed
assert archive.get_output_string() == srcml
#################################################

