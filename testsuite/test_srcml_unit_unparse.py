import pylibsrcml

src = "a;\n"
utf8_src = "/* ✓ */\n"
latin_src = "/* &#10003; */\n"

srcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src">

<unit language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

# utf8_srcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <unit xmlns="http://www.srcML.org/srcML/src" language="C++" url="test" filename="project" version="1"><comment type="block">/* ✓ */</comment>
# </unit>
# """

# latin_srcml = """<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
# <unit xmlns="http://www.srcML.org/srcML/src" language="C++" url="test" filename="project" version="1"><comment type="block">/* &#10003; */</comment>
# </unit>
# """

# latin_from_utf8_srcml = """<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
# <unit xmlns="http://www.srcML.org/srcML/src" language="C++" url="test" filename="project" version="1"><comment type="block">/* &#10003; */</comment>
# </unit>
# """

# latin_from_latin_srcml = """<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
# <unit xmlns="http://www.srcML.org/srcML/src" language="C++" url="test" filename="project" version="1"><comment type="block">/* &#10003; */</comment>
# </unit>
# """

with open("project.xml",'w') as file:
    file.write(srcml)
# with open("project_utf8.xml",'wb') as file:
#     file.write(utf8_srcml.encode())
# with open("project_latin.xml",'w') as file:
#     file.write(latin_srcml)
# with open("project_latin_from_utf8.xml",'w') as file:
#     file.write(latin_from_utf8_srcml)
# with open("project_latin_from_latin.xml",'w') as file:
#     file.write(latin_from_latin_srcml)


#################################################
# srcml_unit_unparse_filename
################################################# 1
# archive1 = pylibsrcml.srcMLArchiveRead(srcml); print(archive1.c_archive)
archive2 = pylibsrcml.srcMLArchiveRead("project.xml"); print(archive2.c_archive)
# unit = archive.read_unit()
# print(unit.get_srcml())

# unit.unparse_filename("project.c")
# with open("project.c",'r') as file:
#     assert file.read() == src
# ################################################# 2
# archive = pylibsrcml.srcMLArchiveRead("project_utf8.xml")
# unit = archive.read_unit()
# unit.set_src_encoding("UTF-8")

# unit.unparse_filename("project_utf8.cpp")
# with open("project_utf8.cpp",'rb') as file:
#     assert file.read().decode() == utf8_src
# ################################################# 3
# archive = pylibsrcml.srcMLArchiveRead("project_latin_from_utf8.xml")
# unit = archive.read_unit()
# unit.set_src_encoding("UTF-8")

# unit.unparse_filename("project_latin_from_utf8.cpp")
# with open("project_latin_from_utf8.cpp",'rb') as file:
#     assert file.read().decode() == utf8_src
# ################################################# 4
# archive = pylibsrcml.srcMLArchiveRead("project_latin.xml")
# unit = archive.read_unit()
# unit.set_src_encoding("ISO-8859-1")

# unit.unparse_filename("project_latin.cpp")
# with open("project_latin.cpp",'r') as file:
#     assert file.read() == latin_src
# ################################################# 5
# archive = pylibsrcml.srcMLArchiveRead("project_latin_from_latin.xml")
# unit = archive.read_unit()
# unit.set_src_encoding("ISO-8859-1")

# unit.unparse_filename("project_latin_from_latin.cpp")
# with open("project_latin_from_latin.cpp",'r') as file:
#     assert file.read() == latin_src
# ################################################# 6
# archive = pylibsrcml.srcMLArchiveRead("project.xml")
# unit = archive.read_unit()

# unit.unparse_filename("project.c")
# with open("project.c",'r') as file:
#     assert file.read() == src
# ################################################# 7
# archive = pylibsrcml.srcMLArchiveRead("project.xml")
# unit = archive.unit_create()

# try:
#     unit.unparse_filename("project.c")
#     assert False
# except pylibsrcml.srcMLException as e:
#     assert e.error_code == pylibsrcml.srcMLStatus.UNINITIALIZED_UNIT
# ################################################# 8
# archive = pylibsrcml.srcMLArchive()
# unit = archive.unit_create()

# try:
#     unit.unparse_filename("")
#     assert False
# except pylibsrcml.srcMLException as e:
#     assert e.error_code == pylibsrcml.srcMLStatus.INVALID_IO_OPERATION
# ################################################# 9
# archive = pylibsrcml.srcMLArchiveRead("project.xml")
# unit = archive.read_unit()

# try:
#     unit.unparse_filename(0)
#     assert False
# except pylibsrcml.srcMLTypeError:
#     pass
# #################################################








print("DEL")


"""
################################################# X
archive = pylibsrcml.srcMLArchiveRead("")
unit = archive.read_unit()

unit.unparse_filename("")
with open("",'r') as file:
    assert file.read() == 



"""
