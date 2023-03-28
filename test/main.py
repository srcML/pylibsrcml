import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()

srcml_a = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

archive = pylibsrcml.srcMLArchiveRead(srcml_a)

archive.x = "hello"

unit = archive.read_unit()

unit2 = unit.clone()

print(str(unit2) )



with open("../testsuite/Makefile",'r') as file:
    print(file.readline())
    print("|||")
    print(file.read())

print("Done")
