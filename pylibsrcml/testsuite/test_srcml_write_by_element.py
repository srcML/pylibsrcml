# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_write_by_element.py

@copyright Copyright (C) 2014-2024 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

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
################################################# 4
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,'element',None)
unit.write_namespace(None,"bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element xmlns="bar"/>' + end_unit
################################################# 5
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_end_element()
unit.write_start_element(None,"element",None)
unit.write_end_element()
unit.write_end_unit()

archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element/><element/>" + end_unit
################################################# 7
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_end_element()
unit.write_start_element(None,"element",None)
unit.write_end_unit()

archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element/><element/>" + end_unit
################################################# 8
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_start_element(None,"element",None)
unit.write_end_element()
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element><element/></element>" + end_unit
################################################# 9
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_start_element(None,"element",None)
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element><element/></element>" + end_unit
################################################# 10
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
try:
    unit.write_start_element(None,None,None)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 11
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
try:
    unit.write_start_element(None,"element",None)
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
#################################################


#################################################
# srcml_write_end_element
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
try:
    unit.write_end_element()
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
#################################################


#################################################
# srcml_write_namespace
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_namespace("foo","bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element xmlns:foo="bar"/>' + end_unit
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
try:
    unit.write_namespace("foo",None)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)

unit.write_namespace(None,"bar")

unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element xmlns="bar"/>' + end_unit
################################################# 4
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
try:
    unit.write_namespace("foo","bar")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
#################################################


#################################################
# srcml_write_attribute
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_attribute(None,"foo",None,"bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element foo="bar"/>' + end_unit
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_attribute("f","foo",None,"bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element f:foo="bar"/>' + end_unit
################################################# 3
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_attribute(None,"foo","b","bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element foo="bar" xmlns="b"/>' + end_unit
################################################# 4
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_attribute("f","foo","b","bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element f:foo="bar" xmlns:f="b"/>' + end_unit
################################################# 5
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_attribute(None,"foo",None,"bar")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + '<element foo="bar"/>' + end_unit
################################################# 6
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.write_start_unit()
unit.write_start_element(None,"element",None)
try:
    unit.write_attribute("f",None,"b","bar")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 7
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
try:
    unit.write_attribute(None,"foo",None,"bar")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
#################################################


#################################################
# srcml_write_string
################################################# 1
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_string("foo")
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element>foo</element>" + end_unit
################################################# 2
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C++")
unit.write_start_unit()
unit.write_start_element(None,"element",None)
unit.write_start_element(None,"element",None)
unit.write_string("foo")
unit.write_end_element()
unit.write_end_element()
unit.write_end_unit()
archive.write_unit(unit)

s = archive.close()

assert s == xml_decl + start_unit + "<element><element>foo</element></element>" + end_unit
################################################# 3
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
try:
    unit.write_string("foo")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveWriteString()
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.write_start_unit()
unit.write_start_element(None,"element",None)
try:
    unit.write_string(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################
