#import sys

import pylibsrcml

print("hello world")
print(dir(pylibsrcml))

##print(dir(pylibsrcml))
##
##print(pylibsrcml.version_number())
##
##print(pylibsrcml.version_string())
##
##print(pylibsrcml.check_language("C++"))
##print(pylibsrcml.check_language("Python"))
##print(pylibsrcml.check_language("Python"))
##
##print(pylibsrcml.check_extension("file.cpp"))
##print(pylibsrcml.check_extension("file.py"))
##print(pylibsrcml.check_extension("file.java"))
##
##print(pylibsrcml.get_language_list_size())
##
##for i in range(pylibsrcml.get_language_list_size()):
##    print(pylibsrcml.get_language_from_list_pos(i))
##
###New Python Function
##print(pylibsrcml.get_language_list())
##
##print(pylibsrcml.check_encoding("UTF16"))
##print(pylibsrcml.check_encoding("blah"))
##
##print(pylibsrcml.check_xslt())
##
##print(pylibsrcml.check_exslt())
##
##pylibsrcml.srcml("test.cpp","test.cpp.xml")
##pylibsrcml.srcml("test.cpp.xml","test2.cpp")
##
##print(pylibsrcml.get_src_encoding())
##pylibsrcml.set_src_encoding("UTF16")
##print(pylibsrcml.get_src_encoding())
##
##print(pylibsrcml.get_xml_encoding())
##pylibsrcml.set_xml_encoding("UTF8")
##print(pylibsrcml.get_xml_encoding())
##
##arch_1 = pylibsrcml.srcml_archive()
##print(arch_1.c_archive)
##arch_2 = arch_1.clone()
##print(arch_2.c_archive)
##
##unit_1 = pylibsrcml.srcml_unit(arch_1)
##print(unit_1.c_unit)
##unit_2 = unit_1.clone()
##print(unit_2.c_unit)
##
##print("b1:",unit_1.get_src_encoding())
##print("b2:",unit_2.get_src_encoding())
##
###unit_1.set_src_encoding("UTF8")
###unit_2.set_src_encoding("blah")
##
##print("a1:",unit_1.get_src_encoding())
##print("a2:",unit_2.get_src_encoding())
##
##print(unit_1.get_language())
##print(unit_2.get_language())
##
##unit_1.set_language("C++")
##unit_2.set_language("Python")
##
##print(unit_1.get_language())
##print(unit_2.get_language())
##
##unit_1.parse_filename("test.cpp")
##
##print(unit_1.get_srcml())
##
##unit_1.unparse_filename("test2.cpp")
##
##print("Error:",pylibsrcml.error_string())
##print("Unit error:",unit_1.error_string())
##
##print(dir(pylibsrcml.srcml_unit))
