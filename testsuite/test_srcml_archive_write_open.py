import pylibsrcml

empty_srcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0"/>
"""

srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.version_string()}">

<unit revision="{pylibsrcml.version_string()}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""


#################################################
# srcml_archive_write_open_filename
################################################# 1
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.close()
with open("project.xml",'r') as file:
    assert file.read() == empty_srcml
################################################# 2
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.write_string(srcml)
archive.close()
with open("project.xml",'r') as file:
    assert file.read() == srcml
#################################################


#################################################
# srcml_archive_write_open_memory
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
s = archive.close()
assert s == empty_srcml
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.write_string(srcml)
s = archive.close()
assert s == srcml
#################################################


#################################################
# srcml_archive_write_open_file
################################################# 1
file = open("project.xml",'w')
archive = pylibsrcml.srcMLArchiveWrite(file)
archive.close()
with open("project.xml") as file:
    assert file.read() == empty_srcml
################################################# 2
file = open("project.xml",'w')
archive = pylibsrcml.srcMLArchiveWrite(file)
archive.write_string(srcml)
archive.close()
with open("project.xml",'r') as file:
    assert file.read() == srcml
#################################################
