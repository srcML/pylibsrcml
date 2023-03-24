import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()


xml_decl = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
"""

empty_unit = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp" version="1" timestamp="today"/>
"""

empty_inner_unit = f"""<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp" version="1" timestamp="today"/>
"""

start_root_unit_tag = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" url="url">

"""

end_root_unit_tag = """
</unit>
"""

start_unit = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++">"""

end_unit = """</unit>
"""


#################################################
# srcml_write_start_unit
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
archive.disable_hash()
archive.set_url("url")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("a.cpp")
unit.set_version("1")
unit.set_timestamp("today")
unit.write_start_unit()
unit.write_end_unit()
archive.write_unit(unit)
s = archive.close()

assert s == xml_decl + empty_unit
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.set_url("url")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("a.cpp")
unit.set_version("1")
unit.set_timestamp("today")
unit.write_start_unit()
unit.write_end_unit()
archive.write_unit(unit)
s = archive.close()

assert s == xml_decl + start_root_unit_tag + empty_inner_unit + end_root_unit_tag
################################################# 3
archive = pylibsrcml.srcMLArchiveWriteString()
archive.set_url("url")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("a.cpp")
unit.set_version("1")
unit.set_timestamp("today")
unit.write_start_unit()
unit.write_end_unit()
archive.write_unit(unit)
unit.write_start_unit()
unit.write_end_unit()
archive.write_unit(unit)
s = archive.close()

assert s == xml_decl + start_root_unit_tag + empty_inner_unit + "\n" + empty_inner_unit + end_root_unit_tag
#################################################


#################################################
# srcml_write_end_element
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
try:
    unit.write_end_unit()
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
#################################################


#################################################
# srcml_write_start_element
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None, "element", None)
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element/>" + end_unit
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.write_start_unit()
unit.set_language("C++")
unit.write_start_element(None, "element", None)
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element/>" + end_unit
################################################# 3
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element("foo","element",None)
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<foo:element/>" + end_unit








"""
################################################# X
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()

archive.write_unit(unit)

s = archive.close()

assert



"""
