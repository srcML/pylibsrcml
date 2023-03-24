import pylibsrcml

archive = pylibsrcml.srcMLArchive()

#################################################
# srcml_unit_set_encoding
################################################# 1
unit = archive.unit_create()
unit.set_src_encoding("")

assert unit.get_src_encoding() == None
################################################# 2
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")

assert unit.get_src_encoding() == "ISO-8859-1"
################################################# 3
unit = archive.unit_create()
try:
    unit.set_src_encoding(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_unit_set_language
################################################# 1
unit = archive.unit_create()
unit.set_language("")

assert unit.get_language() == None
################################################# 2
unit = archive.unit_create()
unit.set_language("C++")

assert unit.get_language() == "C++"
################################################# 3
unit = archive.unit_create()
try:
    unit.set_language(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_unit_set_filename
################################################# 1
unit = archive.unit_create()
unit.set_filename("")

assert unit.get_filename() == None
################################################# 2
unit = archive.unit_create()
unit.set_filename("main.cpp")

assert unit.get_filename() == "main.cpp"
################################################# 3
unit = archive.unit_create()
try:
    unit.set_filename(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_unit_set_version
################################################# 1
unit = archive.unit_create()
unit.set_version("")

assert unit.get_version() == None
################################################# 2
unit = archive.unit_create()
unit.set_version("0.9.5")

assert unit.get_version() == "0.9.5"
################################################# 3
unit1 = archive.unit_create()
unit1.set_version("v1")
assert unit1.get_version() == "v1"

unit2 = archive.unit_create()
unit2.set_version("v2")
assert unit2.get_version() == "v2"

archive.set_version("archiveVersion")

assert unit1.get_version() == "v1"
assert unit2.get_version() == "v2"
#################################################
unit = archive.unit_create()
try:
    unit.set_version(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_unit_set_timestamp
################################################# 1
unit = archive.unit_create()
unit.set_timestamp("")

assert unit.get_timestamp() == None
################################################# 2
unit = archive.unit_create()
unit.set_timestamp("Wed Jul  3 16:38:14 EDT 2019")

assert unit.get_timestamp() == "Wed Jul  3 16:38:14 EDT 2019"
################################################# 3
unit = archive.unit_create()
try:
    unit.set_timestamp(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_unit_set_eol
################################################# 1
unit = archive.unit_create()
unit.set_eol(pylibsrcml.SourceOutputEOL.AUTO)

assert unit.get_eol() == pylibsrcml.SourceOutputEOL.AUTO
################################################# 2
unit = archive.unit_create()
unit.set_eol(pylibsrcml.SourceOutputEOL.LF)

assert unit.get_eol() == pylibsrcml.SourceOutputEOL.LF
################################################# 3
unit = archive.unit_create()
unit.set_eol(pylibsrcml.SourceOutputEOL.CR)

assert unit.get_eol() == pylibsrcml.SourceOutputEOL.CR
################################################# 4
unit = archive.unit_create()
unit.set_eol(pylibsrcml.SourceOutputEOL.CRLF)

assert unit.get_eol() == pylibsrcml.SourceOutputEOL.CRLF
################################################# 5
unit = archive.unit_create()
try:
    unit.set_eol(pylibsrcml.SourceOutputEOL.CRLF + 1)
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT
archive.close()
################################################# 6
text = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0" language="C++">
<expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

archive = pylibsrcml.srcMLArchiveRead(text)
unit = archive.read_unit()

unit.set_eol(pylibsrcml.SourceOutputEOL.LF)
buf = unit.unparse_string()
assert buf == "\na;\n"

unit.set_eol(pylibsrcml.SourceOutputEOL.CRLF)
buf = unit.unparse_string()
assert buf == "\r\na;\r\n"

unit.set_eol(pylibsrcml.SourceOutputEOL.CR)
buf = unit.unparse_string()
assert buf == "\ra;\r"

archive.close()


"""
################################################# X
unit = archive.unit_create()
unit.

assert



"""
