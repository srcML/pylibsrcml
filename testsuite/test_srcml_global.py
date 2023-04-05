import pylibsrcml


#################################################
# srcml_check_language
################################################# 1
assert pylibsrcml.check_language("C") == 1
assert pylibsrcml.check_language("C++") == 2
assert pylibsrcml.check_language("Java") == 4
assert pylibsrcml.check_language("C#") == 8
assert pylibsrcml.check_language("Objective-C") == 17
#################################################


#################################################
# srcml_get_language_list_size
################################################# 1
assert pylibsrcml.get_language_list_size() == 5
#################################################


#################################################
# srcml_get_language_list
################################################# 1
langs = pylibsrcml.get_language_list()
assert langs == ["C","C++","C#","Java","Objective-C"]
#################################################


#################################################
# srcml_get_language_from_list_pos
################################################# 1
assert pylibsrcml.get_language_from_list_pos(0) == "C"
assert pylibsrcml.get_language_from_list_pos(1) == "C++"
assert pylibsrcml.get_language_from_list_pos(2) == "C#"
assert pylibsrcml.get_language_from_list_pos(3) == "Java"
assert pylibsrcml.get_language_from_list_pos(4) == "Objective-C"
try:
    pylibsrcml.get_language_from_list_pos(-1)
    assert False
except IndexError:
    pass
try:
    pylibsrcml.get_language_from_list_pos(6)
    assert False
except IndexError:
    pass
#################################################


#################################################
# srcml_check_extension
################################################# 1
assert pylibsrcml.check_extension("a.cpp") == "C++"
################################################# 2
assert pylibsrcml.check_extension("a.cpp.gz") == "C++"
################################################# 3
pylibsrcml.register_file_extension("foo","C++")
assert pylibsrcml.check_extension("a.foo") == "C++"
################################################# 4
# print(pylibsrcml.check_extension("a.foo.gz"))
# assert pylibsrcml.check_extension("a.foo.gz") == "C++"
################################################# 5
assert pylibsrcml.check_extension("a.bar") == None
################################################# 6
try:
    pylibsrcml.check_extension(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 7
assert pylibsrcml.check_extension("a.c") == "C"
################################################# 8
assert pylibsrcml.check_extension("a.h") == "C"
################################################# 9
assert pylibsrcml.check_extension("a.i") == "C"
################################################# 10
assert pylibsrcml.check_extension("a.cpp") == "C++"
################################################# 11
assert pylibsrcml.check_extension("a.CPP") == "C++"
################################################# 12
assert pylibsrcml.check_extension("a.cp") == "C++"
################################################# 13
assert pylibsrcml.check_extension("a.hpp") == "C++"
################################################# 14
assert pylibsrcml.check_extension("a.cxx") == "C++"
################################################# 15
assert pylibsrcml.check_extension("a.hxx") == "C++"
################################################# 16
assert pylibsrcml.check_extension("a.cc") == "C++"
################################################# 17
assert pylibsrcml.check_extension("a.hh") == "C++"
################################################# 18
assert pylibsrcml.check_extension("a.c++") == "C++"
################################################# 19
assert pylibsrcml.check_extension("a.h++") == "C++"
################################################# 20
assert pylibsrcml.check_extension("a.C") == "C++"
################################################# 21
assert pylibsrcml.check_extension("a.H") == "C++"
################################################# 22
assert pylibsrcml.check_extension("a.tcc") == "C++"
################################################# 23
assert pylibsrcml.check_extension("a.ii") == "C++"
################################################# 24
assert pylibsrcml.check_extension("a.java") == "Java"
################################################# 25
assert pylibsrcml.check_extension("a.aj") == "Java"
################################################# 26
assert pylibsrcml.check_extension("a.cs") == "C#"
#################################################


#################################################
# srcml_check_encoding
################################################# 1
assert pylibsrcml.check_encoding("UTF-8") == 1
################################################# 2
assert pylibsrcml.check_encoding("UTF-64") == 0
################################################# 3
try:
    pylibsrcml.check_encoding(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################
