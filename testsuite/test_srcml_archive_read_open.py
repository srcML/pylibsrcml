
import pylibsrcml

srcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" url="test" filename="project" version="1">

<unit language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

<unit language="C++" filename="b.cpp"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_single = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" language="C++" url="test" filename="project" version="1"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

srcml_ns = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src">

<s:unit language="C++" filename="a.cpp"><s:expr_stmt><s:expr><s:name>a</s:name></s:expr>;</s:expr_stmt>
</s:unit>

<s:unit language="C++" filename="b.cpp"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>
"""

with open("project.xml",'w') as file:
    file.write(srcml)
with open("project_single.xml",'w') as file:
    file.write(srcml_single)
with open("project_ns.xml",'w') as file:
    file.write(srcml_ns)


#################################################
# srcml_archive_read_open_filename
################################################# 1
archive = pylibsrcml.srcMLArchiveRead("project.xml")
assert archive.get_url() == "test"
assert archive.get_version() == "1"
assert archive.get_options() == 0
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveRead("project_single.xml")
assert archive.get_language() == None
assert archive.get_url() == "test"
assert archive.get_version() == "1"
assert archive.get_options() == 0
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveRead("project_ns.xml")
assert archive.get_namespace_prefix(0) == "s"
assert archive.get_options() == 0
archive.close()
################################################# 4
try:
    archive = pylibsrcml.srcMLArchiveRead("")
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.IO_ERROR
################################################# 5
try:
    archive = pylibsrcml.srcMLArchiveRead("not_real.xml")
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.IO_ERROR
#################################################


#################################################
# srcml_archive_read_open_memory
################################################# 1
archive = pylibsrcml.srcMLArchiveRead(srcml)
assert archive.get_url() == "test"
assert archive.get_version() == "1"
assert archive.get_options() == 0
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveRead(srcml_single)
assert archive.get_language() == None
assert archive.get_url() == "test"
assert archive.get_version() == "1"
assert archive.get_options() == 0
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveRead(srcml_ns)
assert archive.get_namespace_prefix(0) == "s"
assert archive.get_options() == 0
archive.close()
################################################# 4
try:
    archive = pylibsrcml.srcMLArchiveRead(1)
except pylibsrcml.srcMLTypeError:
    pass
################################################# 5
try:
    archive = pylibsrcml.srcMLArchiveRead("", string_read_mode = "source")
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT
#################################################

# DISABLED - File opening doesn't work!
# #################################################
# # srcml_archive_read_open_file
# ################################################# 1
# file = open("project.xml",'r')
# archive = pylibsrcml.srcMLArchiveRead(file)
# assert archive.get_url() == "test"
# assert archive.get_version() == "1"
# assert archive.get_options() == 0
# archive.close()
# ################################################# 2
# file = open("project_single.xml",'r')
# archive = pylibsrcml.srcMLArchiveRead(file)
# assert archive.get_language() == None
# assert archive.get_url() == "test"
# assert archive.get_version() == "1"
# assert archive.get_options() == 0
# archive.close()
# ################################################# 3
# file = open("project_ns.xml",'r')
# archive = pylibsrcml.srcMLArchiveRead(file)
# assert archive.get_namespace_prefix(0) == "s"
# assert archive.get_options() == 0
# archive.close()
# ################################################# 4
# file = open("project.xml",'r')
# file.close()
# try:
#     archive = pylibsrcml.srcMLArchiveRead(file)
# except ValueError:
#     pass
# #################################################
