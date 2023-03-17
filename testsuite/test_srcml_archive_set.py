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





################################################# 1
archive = pylibsrcml.srcMLArchive()

archive.close()
#################################################
