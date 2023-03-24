import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()

src = "a;\n"
src_bom = "\xEF\xBB\xBFa;\n"
utf8_src = "/* \u2713 */\n"
latin_src = "/* \xfe\xff */\n"

srcml = f"""<unit revision="{SRCML_VERSION_STRING}" language="C"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""
srcml_full = f"""<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""
utf8_srcml = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" url="test" filename="project" version="1"><comment type="block">/* ✓ */</comment>
</unit>"""
latin_srcml = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" url="test" filename="project" version="1"><comment type="block">/* þÿ */</comment>
</unit>"""
srcml_timestamp = f"""<unit revision="{SRCML_VERSION_STRING}" language="C" timestamp="today"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""
srcml_hash = f"""<unit revision="{SRCML_VERSION_STRING}" language="C" hash="aa2a72b26cf958d8718a2e9bc6b84679a81d54cb"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""
srcml_hash_generated = f"""<unit revision="{SRCML_VERSION_STRING}" language="C" hash="aa2a72b26cf958d8718a2e9bc6b84679a81d54cb"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""
srcml_encoding = f"""<unit revision="{SRCML_VERSION_STRING}" language="C" src-encoding="UTF-8"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""


with open("project.c",'w') as file:
    file.write(src)
with open("project_bom.c",'w') as file:
    file.write(src_bom)
with open("project.foo",'w') as file:
    file.write(src)
with open("project_utf8.cpp",'wb') as file:
    file.write(utf8_src.encode())
with open("project_latin.cpp",'w') as file:
    file.write(latin_src)

#################################################
# srcml_unit_parse_filename
################################################# 1
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.enable_solitary_unit()
archive.disable_hash()
unit = archive.unit_create()
unit.set_language("C")
unit.parse_filename("project.c")

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.enable_solitary_unit()
archive.disable_hash()
unit = archive.unit_create()
unit.set_language("C")
unit.parse_filename("project.foo")
archive.write_unit(unit)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.enable_solitary_unit()
archive.disable_hash()
archive.set_language("C")
unit = archive.unit_create()
unit.parse_filename("project.foo")
assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.register_file_extension("foo","C++")
archive.set_url("test")
unit = archive.unit_create()
unit.set_filename("project")
unit.set_version("1")
unit.set_language("C++")
unit.parse_filename("project.foo")

assert unit.get_srcml_outer() == srcml_full
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_language("C++")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_filename("project.foo")

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 6
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_filename("project.c")

assert unit.get_srcml_outer() == srcml_full
archive.close()
################################################# 7
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_solitary_unit()
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("UTF-8")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_filename("project_utf8.cpp")

assert unit.get_srcml() == utf8_srcml
archive.close()
################################################# 8
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_solitary_unit()
archive.set_xml_encoding("ISO-8859-1")
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("UTF-8")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_filename("project_utf8.cpp")

assert unit.get_srcml() == utf8_srcml
archive.close()
################################################# 9
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_solitary_unit()
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_filename("project_latin.cpp")

assert unit.get_srcml() == latin_srcml
archive.close()
################################################# 10
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_solitary_unit()
archive.set_xml_encoding("ISO-8859-1")
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_filename("project_latin.cpp")

assert unit.get_srcml() == latin_srcml

archive.write_unit(unit)
archive.close()
################################################# 11
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.parse_filename("project.c")

assert unit.get_timestamp() == None
archive.close()
################################################# 12
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
unit = archive.unit_create()
unit.set_timestamp("today")
unit.set_language("C")
unit.parse_filename("project.c")

assert unit.get_srcml_outer() == srcml_timestamp
archive.close()
################################################# 13
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_filename("project.c")

assert unit.get_srcml_outer() == srcml_hash_generated
archive.close()
################################################# 14
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_option(pylibsrcml.srcMLOption.STORE_ENCODING)
archive.set_src_encoding("UTF-8")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_filename("project_bom.c")

assert unit.get_srcml_outer() == srcml_encoding
archive.close()
################################################# 15
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.enable_solitary_unit()
unit = archive.unit_create()
unit.set_language("C")
unit.parse_filename("project.c")

assert unit.get_srcml_outer() == srcml_hash
archive.close()
################################################# 16
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
try:
    unit.parse_filename("project.cpp")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.IO_ERROR
archive.close()
################################################# 17
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
try:
    unit.parse_filename("project.c")
except:
    assert False
archive.close()
################################################# 18
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
try:
    unit.parse_filename(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 19
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
try:
    unit.parse_filename("project.foo")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.UNSET_LANGUAGE
archive.close()
#################################################


#################################################
# srcml_unit_parse_memory
################################################# 1
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_language("C")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_language("C++")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml_full
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml_full
archive.close()
################################################# 6
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("UTF-8")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_memory(utf8_src)

assert unit.get_srcml() == utf8_srcml
archive.close()
################################################# 7
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_xml_encoding("ISO-8859-1")
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("UTF-8")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_memory(utf8_src)

assert unit.get_srcml() == utf8_srcml
archive.close()
################################################# 8
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_memory(latin_src)

assert unit.get_srcml() == latin_srcml
archive.close()
################################################# 9
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_xml_encoding("ISO-8859-1")
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
unit.parse_memory(latin_src)

assert unit.get_srcml() == latin_srcml
archive.close()
################################################# 10
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_timestamp() == None
archive.close()
################################################# 11
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
unit = archive.unit_create()
unit.set_timestamp("today")
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml_timestamp
archive.close()
################################################# 12
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml_hash
archive.close()
################################################# 13
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory(src)

assert unit.get_srcml_outer() == srcml_hash_generated
archive.close()
################################################# 14
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_option(pylibsrcml.srcMLOption.STORE_ENCODING)
unit = archive.unit_create()
# print("?",unit.get_src_encoding())
unit.set_language("C")
unit.parse_memory(src_bom)
# print("!",unit.get_src_encoding())
# print(unit.get_srcml_outer())
# print("|")
# print(srcml_encoding)

# assert unit.get_srcml_outer() == srcml_encoding
archive.close()
################################################# 15
archive = pylibsrcml.srcMLArchive()
unit = archive.unit_create()
unit.set_language("C")

try:
    unit.parse_memory(src)
except:
    assert False
archive.close()
################################################# 16
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")

try:
    unit.parse_memory(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 17
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
unit = archive.unit_create()
unit.set_language("C")
unit.parse_memory("")

assert unit.get_srcml_outer() == f'<unit revision="{SRCML_VERSION_STRING}" language="C"/>'
archive.close()
################################################# 18
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()

try:
    unit.parse_memory(src)
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.UNSET_LANGUAGE
archive.close()
#################################################


#################################################
# srcml_unit_parse_file
################################################# 1
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_language("C")
unit = archive.unit_create()

with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_language("C++")
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml_full
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml_full
archive.close()
################################################# 6
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("UTF-8")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
with open("project_utf8.cpp",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml() == utf8_srcml
archive.close()
################################################# 7
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_xml_encoding("ISO-8859-1")
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("UTF-8")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
with open("project_utf8.cpp",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml() == utf8_srcml
archive.close()
################################################# 8
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
with open("project_latin.cpp",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml() == latin_srcml
archive.close()
################################################# 9
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.set_xml_encoding("ISO-8859-1")
archive.set_url("test")
unit = archive.unit_create()
unit.set_src_encoding("ISO-8859-1")
unit.set_language("C++")
unit.set_filename("project")
unit.set_version("1")
with open("project_latin.cpp",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml() == latin_srcml
archive.close()
################################################# 10
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_timestamp() == None
archive.close()
################################################# 11
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
unit = archive.unit_create()
unit.set_timestamp("today")
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml_timestamp
archive.close()
################################################# 12
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)
# print("A",unit.get_srcml_outer())
# print("|")
# print("B",srcml_hash_generated)
# assert unit.get_srcml_outer() == srcml_hash_generated
archive.close()
################################################# 13
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
archive.disable_hash()
archive.enable_option(pylibsrcml.srcMLOption.STORE_ENCODING)
unit = archive.unit_create()
unit.set_language("C")
with open("project_bom.c",'r') as file:
    unit.parse_file(file)

assert unit.get_srcml_outer() == srcml_encoding
archive.close()
################################################# 14
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)
# print("A",unit.get_srcml_outer())
# print("|")
# print("B",srcml_hash)
# assert unit.get_srcml_outer() == srcml_hash
archive.close()
################################################# 15
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    unit.parse_file(file)

# assert unit.get_srcml_outer() == srcml_hash_generated
archive.close()
################################################# 16
archive = pylibsrcml.srcMLArchive()
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    try:
        unit.parse_file(file)
    except:
        assert False
archive.close()
################################################# 17
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
unit.set_language("C")
with open("project.c",'r') as file:
    try:
        unit.parse_file(0)
        assert False
    except pylibsrcml.srcMLTypeError:
        pass
archive.close()
################################################# 18
archive = pylibsrcml.srcMLArchiveWrite("project.xml")
unit = archive.unit_create()
with open("project.c",'r') as file:
    try:
        unit.parse_file(file)
        assert False
    except pylibsrcml.srcMLException as e:
        assert e.error_code == pylibsrcml.srcMLStatus.UNSET_LANGUAGE
archive.close()
#################################################
