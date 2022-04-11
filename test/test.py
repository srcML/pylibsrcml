# ********************************************************************************************************************************************************
# @file test.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

import sys
sys.path.append("../src/libsrcml")
from pylibsrcml import srcml
import difflib
import os
import ctypes

test_count = 0
error_count = 0

LIBC_PATH = ""
if sys.platform == "darwin" :
    LIBC_PATH = "libc.dylib"
elif sys.platform == "linux" :
    LIBC_PATH = "libc.so.6"
else :
    LIBC_PATH = "msvcrt.dll"

libc = ctypes.cdll.LoadLibrary(LIBC_PATH)

if sys.platform == "win32" or sys.platform == "cygin" :
    os.open = libc._open
    os.close = libc._close
    os.O_WRONLY = 1
    os.O_CREAT = 256
    os.O_RDONLY = 0

libc.fopen.restype = ctypes.c_void_p
libc.fopen.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

libc.fclose.restype = ctypes.c_int
libc.fclose.argtypes = [ctypes.c_void_p]

def verify_test(correct, output) :
    globals()['test_count'] += 1

    if sys.platform == "win32" or sys.platform == "cygwin" :
        correct = str(correct).replace("\r", "")
        output = str(output).replace("\r", "")

    if str(correct) != str(output) :
        print(str(globals()['test_count']) + "\t")
        for line in difflib.unified_diff(str(correct).split("\n"), str(output).split("\n")) :
            print(line)
        globals()['error_count'] += 1
        print("\nERROR:\n" + str(output) + "\n\n!=\n\n" + str(correct) + "\n\n")

    return

def read_callback_f(context, buffer, len):
    return libc.fread(buffer, 1, len, context)

def write_callback_f(context, buffer, len):
    return libc.fwrite(buffer, 1, len, context)

def close_callback_f(context):
    return 0

read_callback = srcml.read_callback_t(read_callback_f)
write_callback = srcml.write_callback_t(write_callback_f)
close_callback = srcml.close_callback_t(close_callback_f)

# -----------------------------------------------------------------
# test_srcml_append_transform
# -----------------------------------------------------------------

# Variable Definitions
asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision=\"""" + srcml.SRCML_VERSION_STRING + """\">
<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" revision=\"""" + srcml.SRCML_VERSION_STRING + """\" language="C++"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" revision=\"""" + srcml.SRCML_VERSION_STRING + """\" language="C++"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>
</unit>
"""
f = open("copy.xsl", "r")
copy = f.read()
f.close()

# append_transform_xpath
archive = srcml.srcml_archive()
archive.append_transform_xpath("//src:unit")
archive.close()

# append_transform_xpath_attribute
archive = srcml.srcml_archive()
archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", "supplement")
archive.close()

# append_transform_xpath_element
archive = srcml.srcml_archive()
archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", "contain")
archive.close()

# append_transform_xslt_filename
archive = srcml.srcml_archive()
archive.append_transform_xslt_filename("copy.xsl")
archive.close()

# append_transform_xslt_memory
archive = srcml.srcml_archive()
archive.append_transform_xslt_memory(copy)
archive.close()

# append_transform_xslt_FILE
archive = srcml.srcml_archive()
f = libc.fopen(b"copy.xsl", b"r")
archive.append_transform_xslt_FILE(f)
libc.fclose(f)
archive.close()

# append_transform_xslt_fd
archive = srcml.srcml_archive()
fd = os.open("copy.xsl", os.O_RDONLY, 0)
archive.append_transform_xslt_fd(fd)
os.close(fd)
archive.close()

# append_transform_telaxng
archive = srcml.srcml_archive()
archive.append_transform_relaxng_filename("schema.rng")
archive.close()

# append_transform_relaxng_memory
archive = srcml.srcml_archive()
f = open("schema.rng", "r")
schema = f.read()
f.close()
archive.append_transform_relaxng_memory(schema)
archive.close()

# append_transform_relaxng_FILE
archive = srcml.srcml_archive()
f = libc.fopen(b"schema.rng", b"r")
archive.append_transform_relaxng_FILE(f)
libc.fclose(f)
archive.close()

# append_transform_relaxng_fd
archive = srcml.srcml_archive()
fd = os.open("schema.rng", os.O_RDONLY, 0)
archive.append_transform_relaxng_fd(fd)
os.close(fd)
archive.close()

# append_transform_param
archive = srcml.srcml_archive()
archive.append_transform_xslt_filename("copy.xsl")
archive.append_transform_param("sup", "http://srcML.org/Supplement")
archive.close()

# append_transform_stringparam
archive = srcml.srcml_archive()
archive.append_transform_xslt_filename("copy.xsl")
archive.append_transform_stringparam("sup", "http://srcML.org/Supplement")
archive.close()

srcml.cleanup_globals()

print("Append transform bindings tested...")

# -----------------------------------------------------------------
# test_srcml_archive_check_extension
# -----------------------------------------------------------------

archive = srcml.srcml_archive()
archive.register_file_extension("h", "C++")

verify_test("C++", archive.check_extension("a.h"))
verify_test("C++", archive.check_extension("a.h.gz"))
verify_test(None, archive.check_extension("a.foo"))

print("Check extension binding tested...")

# -----------------------------------------------------------------
# test_srcml_archive_clone
# -----------------------------------------------------------------

archive = srcml.srcml_archive()
archive.set_src_encoding("e")
archive.set_url("u")
archive.set_version("v")

new_archive = archive.clone()

verify_test("e", new_archive.get_src_encoding())
verify_test("u", new_archive.get_url())
verify_test("v", new_archive.get_version())

print("Archive clone binding tested...")

# -----------------------------------------------------------------
# test_srcml_archive_create
# -----------------------------------------------------------------

archive = srcml.srcml_archive()
verify_test(None, archive.get_language())
verify_test(None, archive.get_xml_encoding())
verify_test(None, archive.get_src_encoding())
verify_test(None, archive.get_url())

print("Archive create binding tested...")

# -----------------------------------------------------------------
# test_srcml_archive_get
# -----------------------------------------------------------------

archive = srcml.srcml_archive()

# src encoding
archive.set_src_encoding("foo")
verify_test("foo", archive.get_src_encoding())

# xml encoding
archive.set_xml_encoding("foo")
verify_test("foo", archive.get_xml_encoding())

# revision
verify_test(srcml.SRCML_VERSION_STRING, archive.get_revision())

# language
archive.set_language("foo")
verify_test("foo", archive.get_language())

# url
archive.set_url("foo")
verify_test("foo", archive.get_url())

# version
archive.set_version("foo")
verify_test("foo", archive.get_version())

# option
archive.set_options(srcml.SRCML_OPTION_CPP)
verify_test(srcml.SRCML_OPTION_CPP, archive.get_options())

# tabstop
archive.set_tabstop(4)
verify_test(4, archive.get_tabstop())

# namespace prefix
verify_test(None, archive.get_namespace_prefix(2))

# namespace size
archive.register_namespace("foo1", "bar1")
archive.register_namespace("foo2", "bar2")
verify_test(3, archive.get_namespace_size())

# prefix from uri
verify_test("foo2", archive.get_prefix_from_uri("bar2"))

# namespace uri
verify_test("bar2", archive.get_namespace_uri(2))

# uri from prefix
verify_test("bar1", archive.get_uri_from_prefix("foo1"))

archive.close()

print("Archive get bindings tested...")

# -----------------------------------------------------------------
# test_srcml_archive_read_open
# -----------------------------------------------------------------

# Variable Definitions
asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" url="test" filename="project" version="1">
<unit language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
<unit language="C++" filename="b.cpp"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>
</unit>
"""

# filename
archive = srcml.srcml_archive()
file = open("project.xml", "w+")
file.write(asrcml)
file.close()

archive.read_open_filename("project.xml")
verify_test("test", archive.get_url())
verify_test("1", archive.get_version())
verify_test(0, archive.get_options())

archive.close()

# memory
archive = srcml.srcml_archive()
archive.read_open_memory(asrcml)

verify_test("test", archive.get_url())
verify_test("1", archive.get_version())
verify_test(0, archive.get_options())

archive.close()

# fd
archive = srcml.srcml_archive()
file = open("project.xml", "w")
file.write(asrcml)
file.close()

fd = os.open("project.xml", os.O_RDONLY)
archive.read_open_fd(fd)

verify_test("test", archive.get_url())
verify_test("1", archive.get_version())
verify_test(0, archive.get_options())

archive.close()
os.close(fd)
os.remove("project.xml")

# FILE
archive = srcml.srcml_archive()
file = open("project.xml", "w")
file.write(asrcml)
file.close()

file = libc.fopen(str.encode("project.xml"), str.encode("r"))
archive.read_open_FILE(file)

verify_test("test", archive.get_url())
verify_test("1", archive.get_version())
verify_test(0, archive.get_options())

archive.close()
libc.fclose(file)
os.remove("project.xml")

# io
archive = srcml.srcml_archive()
file = open("project.xml", "w")
file.write(asrcml)
file.close()

file = libc.fopen(str.encode("project.xml"), str.encode("r"))

# archive.read_open_io(file, srcml.read_callback_t, srcml.close_callback_t)

os.remove("project.xml")
archive.close()

print("Archive read open bindings tested...")

# -----------------------------------------------------------------
# test_srcml_archive_set
# -----------------------------------------------------------------

# src encoding
archive = srcml.srcml_archive()
archive.set_src_encoding("ISO-8859-1")
verify_test("ISO-8859-1", archive.get_src_encoding())

# xml encoding
archive = srcml.srcml_archive()
archive.set_xml_encoding("ISO-8859-1")
verify_test("ISO-8859-1", archive.get_xml_encoding())

# language
archive = srcml.srcml_archive()
archive.set_language("Java")
verify_test("Java", archive.get_language())

# url
archive = srcml.srcml_archive()
archive.set_url("https://srcML.org")
verify_test("https://srcML.org", archive.get_url())

# version
archive = srcml.srcml_archive()
archive.set_version("foo")
verify_test("foo", archive.get_version())

# options
archive = srcml.srcml_archive()
archive.set_options(srcml.SRCML_OPTION_CPP)
verify_test(srcml.SRCML_OPTION_CPP, archive.get_options())

# enable option
archive = srcml.srcml_archive()
archive.enable_option(srcml.SRCML_OPTION_CPP)
verify_test(srcml.SRCML_OPTION_CPP, archive.get_options())

# disable option
archive = srcml.srcml_archive()
archive.enable_option(srcml.SRCML_OPTION_CPP)
archive.disable_option(srcml.SRCML_OPTION_CPP)
verify_test(0, archive.get_options())

# tabstop
archive = srcml.srcml_archive()
archive.set_tabstop(4)
verify_test(4, archive.get_tabstop())

# register file extension
archive = srcml.srcml_archive()
archive.register_file_extension("foo", "C++")
verify_test("C++", archive.check_extension("main.foo"))

# register namespace
archive = srcml.srcml_archive()
archive.register_namespace("foo", "bar")
pos = archive.get_namespace_size() - 1
verify_test("foo", archive.get_namespace_prefix(pos))
verify_test("bar", archive.get_namespace_uri(pos))

print("Archive set bindings tested...")

# -----------------------------------------------------------------
# test_srcml_archive_write_open
# -----------------------------------------------------------------

# Variable Declarations
src = "a;\n"
asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision=\"""" + srcml.SRCML_VERSION_STRING + """\">
<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" revision=\"""" + srcml.SRCML_VERSION_STRING + """\" language="C++"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
</unit>
"""

# filename
archive = srcml.srcml_archive()
archive.write_open_filename("project.xml")
archive.close()

file = open("project.xml", "r")
gen = file.read()
file.close()
verify_test(False, gen == "")

os.remove("project.xml")

# memory
archive = srcml.srcml_archive()
archive.write_open_memory()
archive.close()

# FILE
archive = srcml.srcml_archive()
file = libc.fopen(str.encode("project.xml"), str.encode("w"))
archive.write_open_FILE(file)

archive.close()
libc.fclose(file)

file = open("project.xml", "r")
gen = file.read()
file.close()
verify_test(False, gen == "")

os.remove("project.xml")

# fd
archive = srcml.srcml_archive()
fd = os.open("project.xml", os.O_WRONLY | os.O_CREAT)
archive.write_open_fd(fd)

archive.close()
os.close(fd)

file = open("project.xml", "r")
gen = file.read()
file.close()
verify_test(False, gen == "")

os.remove("project.xml")

# io
archive = srcml.srcml_archive()
file = open("project.xml", "w")
# archive.write_open_io(file, write_callback, close_callback)
gen = file.write(src)

file.close()
archive.close()

file = open("project.xml", "r")
gen = file.read()
file.close()
verify_test(False, gen == "")

os.remove("project.xml")

print("Archive write open bindings tested...")

# -----------------------------------------------------------------
# test_srcml_archive_write_unit
# -----------------------------------------------------------------

asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision=")" SRCML_VERSION_STRING R"(" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

archive = srcml.srcml_archive()
archive.enable_solitary_unit()
archive.disable_hash()
archive.write_open_memory()

unit = srcml.srcml_unit(archive)
unit.set_filename("a.cpp")
unit.set_language("C++")
unit.parse_memory("a;\n")
archive.write_unit(unit)
archive.close()

print("Archive write unit binding tested...")

# -----------------------------------------------------------------
# test_srcml_clear_transforms
# -----------------------------------------------------------------

archive = srcml.srcml_archive()
archive.clear_transforms()

archive = srcml.srcml_archive()
archive.append_transform_xpath("//src:unit")
archive.append_transform_xslt_filename("copy.xsl")
archive.clear_transforms()

print("Archive clear transform binding tested...")

# -----------------------------------------------------------------
# test_srcml_convenience && test_global_access
# -----------------------------------------------------------------

# Variable Declarations
asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision=\"""" + srcml.SRCML_VERSION_STRING + """\" language="C++" filename="a.cpp" hash="56f54d1636dfec63c3e1586e5e4bdc9a455bb9f6"><decl_stmt><decl><type><name>int</name></type> <name>a</name></decl>;</decl_stmt>
</unit>
"""

# srcml
file = open("a.cpp", "w")
file.write("int a;\n")
file.close()

srcml.srcml("a.cpp", "project.xml")
file = open("project.xml", "r")
xml = file.read()
file.close()

verify_test(asrcml, xml)

srcml.set_language("C++")
srcml.set_filename("a.cpp")
srcml.set_url("url")
srcml.set_version("version")
srcml.set_timestamp("timestamp")

verify_test("C++", srcml.get_language())
verify_test(srcml.SRCML_VERSION_STRING, srcml.get_revision())
verify_test("a.cpp", srcml.get_filename())
verify_test("url", srcml.get_url())
verify_test("version", srcml.get_version())
verify_test("timestamp", srcml.get_timestamp())

srcml.set_options(0)
srcml.enable_option(1)
verify_test(1, srcml.get_options())

srcml.set_options(2)
verify_test(2, srcml.get_options())

srcml.set_options(1 | 2)
srcml.disable_option(2)
verify_test(1, srcml.get_options())

srcml.set_tabstop(4)
verify_test(4, srcml.get_tabstop())

os.remove("project.xml")

archive = srcml.srcml_archive();
archive.register_file_extension("foo", "C++")
archive.register_namespace("s", "http://www.srcML.org/srcML/src")

verify_test(2, srcml.check_language("C++"))
verify_test("C++", srcml.check_extension("a.cpp"))
verify_test(1, srcml.check_encoding("UTF-8"))
verify_test(1, srcml.check_xslt())
verify_test(1, srcml.check_exslt())

srcml.cleanup_globals()

print("Convenience and global access bindings tested...")

# -----------------------------------------------------------------
# test_srcml_global
# -----------------------------------------------------------------

# check_language
verify_test(1, srcml.check_language("C"))
verify_test(2, srcml.check_language("C++"))
verify_test(4, srcml.check_language("Java"))
verify_test(8, srcml.check_language("C#"))
verify_test(17, srcml.check_language("Objective-C"))

# get_language_list_size
verify_test(5, srcml.get_language_list_size())

# get_language_list
verify_test("C", srcml.get_language_list(0))
verify_test("C++", srcml.get_language_list(1))
verify_test("C#", srcml.get_language_list(2))
verify_test("Java", srcml.get_language_list(3))
verify_test("Objective-C", srcml.get_language_list(4))
verify_test(None, srcml.get_language_list(5))

# check_extension
verify_test("C++", srcml.check_extension("a.cpp"))
verify_test("C++", srcml.check_extension("a.cpp.gz"))
srcml.register_file_extension("foo", "C++")
verify_test("C++", srcml.check_extension("a.foo"))
verify_test("C++", srcml.check_extension("a.foo.gz"))
verify_test(None, srcml.check_extension("a.bar"))

# check_encoding
verify_test(1, srcml.check_encoding("UTF-8"))
verify_test(None, srcml.check_encoding("UTF-64"))
verify_test(None, srcml.check_encoding(""))

srcml.cleanup_globals()

print("Global bindings tested...")

# -----------------------------------------------------------------
# test_srcml_read_unit
# -----------------------------------------------------------------

# Variable Declaration
asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision=\"""" + srcml.SRCML_VERSION_STRING + """\">
<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" revision=\"""" + srcml.SRCML_VERSION_STRING + """\" language="C++"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
</unit>
"""

file = open("project.xml", "w")
gen = file.write(asrcml)
file.close()
archive = srcml.srcml_archive()
archive.read_open_filename("project.xml")
unit = archive.read_unit()
unit.unparse_filename("a.cpp")
archive.close()

file = open("a.cpp", "r")
gen = file.read()
file.close()
verify_test(src, gen)

os.remove("a.cpp")

print("Read unit bindings tested...")

# -----------------------------------------------------------------
# test_srcml_unit_create
# -----------------------------------------------------------------

archive = srcml.srcml_archive()
unit = srcml.srcml_unit(archive)

verify_test(None, unit.get_language())
verify_test(None, unit.get_filename())
verify_test(None, unit.get_version())
verify_test(None, unit.get_timestamp())
verify_test(None, unit.get_hash())
verify_test(None, unit.get_srcml())
verify_test(None, unit.get_srcml_outer())
verify_test(None, unit.get_srcml_inner())

print("Create unit bindings tested...")

# -----------------------------------------------------------------
# test_srcml_unit_get && test_srcml_unit_set
# -----------------------------------------------------------------

archive = srcml.srcml_archive()
unit = srcml.srcml_unit(archive)

unit.set_src_encoding("foo")
unit.set_language("C++")
unit.set_filename("main.cpp")
unit.set_version("1.5")
unit.set_timestamp("Fri Nov 30 14:15:27 EST 2018")

verify_test("foo", unit.get_src_encoding())
verify_test(srcml.SRCML_VERSION_STRING, unit.get_revision())
verify_test("C++", unit.get_language())
verify_test("main.cpp", unit.get_filename())
verify_test("1.5", unit.get_version())
verify_test("Fri Nov 30 14:15:27 EST 2018", unit.get_timestamp())

# unparse_memory()

text = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0" language="C++">
<expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

archive.read_open_memory(text)
unit = archive.read_unit()
unit.set_eol(srcml.SOURCE_OUTPUT_EOL_LF)
unit.unparse_memory()

verify_test("\na;\n", unit.src())

# parse_memory()
archive = srcml.srcml_archive()
archive.enable_hash()

unit = srcml.srcml_unit(archive)
unit.set_language("C++")
unit.parse_memory("a;")

verify_test(1, archive.has_hash())
verify_test("a301d91aac4aa1ab4e69cbc59cde4b4fff32f2b8", unit.get_hash())

srcml.cleanup_globals()

print("Unit get, set, parse, unparse bindings tested...")

# -----------------------------------------------------------------
# test_srcml_write_by_element
# -----------------------------------------------------------------

# Variable Declaration
asrcml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0">

<unit revision="1.0.0" language="C++"><f:foo xmlns:s="srcML" s:src="ML" xmlns:f="bar">source</f:foo>
</unit>

</unit>
"""

archive = srcml.srcml_archive()
archive.disable_hash()
archive.write_open_memory()

unit = srcml.srcml_unit(archive)
unit.set_language("C++")

unit.write_start_unit()
unit.write_start_element("f", "foo", "bar")
unit.write_namespace("s", "srcML")
unit.write_attribute("s", "src", None, "ML")
unit.write_string("source")
unit.write_end_element()
unit.write_string("\n")
unit.write_end_unit()

archive.write_unit(unit)
archive.close()

verify_test(asrcml, archive.srcML())

print("Write by element bindings tested...")

print("------------------------------------------------------")
print("All bindings have been tested: " + str(error_count) + " errors / " + str(test_count) + " tests")
