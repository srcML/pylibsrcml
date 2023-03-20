import pylibsrcml

#################################################
# srcml_archive_set_src_encoding
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_src_encoding(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_src_encoding("ISO-8859-1")
assert archive.get_src_encoding() == "ISO-8859-1"
archive.close()
#################################################


#################################################
# srcml_archive_set_xml_encoding
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_xml_encoding(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_xml_encoding("ISO-8859-1")
assert archive.get_xml_encoding() == "ISO-8859-1"
archive.close()
#################################################


#################################################
# srcml_archive_set_language
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_language(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_language("Java")
assert archive.get_language() == "Java"
archive.close()
#################################################


#################################################
# srcml_archive_set_url
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_url(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_url("https://srcML.org")
assert archive.get_url() == "https://srcML.org"
archive.close()
#################################################


#################################################
# srcml_archive_set_version
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_version(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_version("foo")
assert archive.get_version() == "foo"
archive.close()
#################################################


#################################################
# srcml_archive_set_options
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_options("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP)
archive.set_options(pylibsrcml.srcMLOption.NO_XML_DECL)
assert archive.get_options() == pylibsrcml.srcMLOption.NO_XML_DECL
archive.close()
#################################################

#################################################
# srcml_archive_enable_option
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.enable_option("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.enable_option(pylibsrcml.srcMLOption.CPP)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.enable_option(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
archive.enable_option(pylibsrcml.srcMLOption.CPP)
archive.enable_option(pylibsrcml.srcMLOption.NO_XML_DECL)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP)
archive.enable_option(pylibsrcml.srcMLOption.NO_XML_DECL)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL
archive.close()
#################################################


#################################################
# srcml_archive_disable_option
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.disable_option("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL | pylibsrcml.srcMLOption.STORE_ENCODING)
archive.disable_option(0)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL | pylibsrcml.srcMLOption.STORE_ENCODING
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL | pylibsrcml.srcMLOption.STORE_ENCODING)
archive.disable_option(pylibsrcml.srcMLOption.CPP)
assert archive.get_options() == pylibsrcml.srcMLOption.NO_XML_DECL | pylibsrcml.srcMLOption.STORE_ENCODING
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL | pylibsrcml.srcMLOption.STORE_ENCODING)
archive.disable_option(pylibsrcml.srcMLOption.NO_XML_DECL)
assert archive.get_options() == pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.STORE_ENCODING
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.set_options(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.NO_XML_DECL | pylibsrcml.srcMLOption.STORE_ENCODING)
archive.disable_option(pylibsrcml.srcMLOption.CPP | pylibsrcml.srcMLOption.STORE_ENCODING)
assert archive.get_options() == pylibsrcml.srcMLOption.NO_XML_DECL
archive.close()
#################################################


#################################################
# srcml_archive_set_tabstop
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_tabstop("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_tabstop(4)
assert archive.get_tabstop() == 4
archive.close()
#################################################


#################################################
# srcml_archive_register_file_extension
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.register_file_extension(1,"C++")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
try:
    archive.register_file_extension("foo",1)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.register_file_extension("foo","C+")
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
archive.register_file_extension("foo","C++")
assert archive.check_extension("main.foo") == "C++"
archive.close()
#################################################


#################################################
# srcml_archive_register_namespace
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.register_namespace(1,"bar")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
try:
    archive.register_namespace("foo",1)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo","http://www.srcML.org/srcML/src")
assert archive.get_namespace_size() == 1
assert archive.get_namespace_prefix(0) == "foo"
assert archive.get_namespace_uri(0) == "http://www.srcML.org/srcML/src"
assert archive.get_uri_from_prefix("foo") == "http://www.srcML.org/srcML/src"
assert archive.get_prefix_from_uri("http://www.srcML.org/srcML/src") == "foo"
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo","bar")
assert archive.get_namespace_size() == 2
assert archive.get_namespace_prefix(1) == "foo"
assert archive.get_namespace_uri(1) == "bar"
assert archive.get_uri_from_prefix("foo") == "bar"
assert archive.get_prefix_from_uri("bar") == "foo"
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar")
archive.register_namespace("foo2","http://www.srcML.org/srcML/test")
assert archive.get_namespace_size() == 3
assert archive.get_namespace_prefix(1) == "foo1"
assert archive.get_namespace_uri(1) == "bar"
assert archive.get_uri_from_prefix("foo1") == "bar"
assert archive.get_prefix_from_uri("bar") == "foo1"
assert archive.get_namespace_prefix(2) == "foo2"
assert archive.get_namespace_uri(2) == "http://www.srcML.org/srcML/test"
assert archive.get_uri_from_prefix("foo2") == "http://www.srcML.org/srcML/test"
assert archive.get_prefix_from_uri("http://www.srcML.org/srcML/test") == "foo2"
archive.close()
################################################# 6
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar")
archive.register_namespace("foo2","bar")
assert archive.get_namespace_size() == 2
assert archive.get_namespace_prefix(1) == "foo2"
assert archive.get_namespace_uri(1) == "bar"
assert archive.get_uri_from_prefix("foo2") == "bar"
assert archive.get_prefix_from_uri("bar") == "foo2"
archive.close()
#################################################


#################################################
# srcml_archive_set_srcdiff_revision
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_srcdiff_revision("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_srcdiff_revision(pylibsrcml.srcDiffRevision.ORIGINAL)
assert archive.get_srcdiff_revision() == pylibsrcml.srcDiffRevision.ORIGINAL
archive.close()
#################################################
