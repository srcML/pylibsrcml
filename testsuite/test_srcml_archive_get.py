import pylibsrcml


#################################################
# srcml_archive_get_src_encoding
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_src_encoding() == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_src_encoding("foo")
assert archive.get_src_encoding() == "foo"
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_src_encoding(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_xml_encoding
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_xml_encoding() == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_xml_encoding("foo")
assert archive.get_xml_encoding() == "foo"
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_xml_encoding(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_revision
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_revision() == pylibsrcml.version_string()
archive.close()
#################################################


#################################################
# srcml_archive_get_language
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_language() == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_language("foo")
assert archive.get_language() == "foo"
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_language(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_url
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_url() == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_url("foo")
assert archive.get_url() == "foo"
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_url(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################

#################################################
# srcml_archive_get_version
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_version() == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_version("foo")
assert archive.get_version() == "foo"
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_version(0)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_options
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_options() == 0
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
try:
    archive.set_options("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_tabstop
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_tabstop() == 8
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_tabstop(4)
assert archive.get_tabstop() == 4
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_tabstop("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_namespace_size
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_size() == 1
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar1")
archive.register_namespace("foo2","bar2")
assert archive.get_namespace_size() == 3
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.register_namespace(0,1)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_namespace_prefix
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_prefix(0) == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_prefix(-1) == None
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_prefix(2) == None
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar1")
assert archive.get_namespace_prefix(1) == "foo1"
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchive()
try:
    archive.get_namespace_prefix("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_prefix_from_uri
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_prefix_from_uri("http://www.srcML.org/srcML/src") == None
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
assert archive.get_prefix_from_uri("bar3") == None
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar1")
assert archive.get_prefix_from_uri("bar1") == "foo1"
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
try:
    archive.get_prefix_from_uri(1)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_namespace_uri
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_uri(0) == "http://www.srcML.org/srcML/src"
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_uri(-1) == None
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
assert archive.get_namespace_uri(2) == None
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar1")
assert archive.get_namespace_uri(1) == "bar1"
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchive()
try:
    archive.get_namespace_uri("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################


#################################################
# srcml_archive_get_uri_from_prefix
################################################# 1
archive = pylibsrcml.srcMLArchive()
assert archive.get_uri_from_prefix("") == "http://www.srcML.org/srcML/src"
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
assert archive.get_uri_from_prefix("foo3") == None
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
archive.register_namespace("foo1","bar1")
assert archive.get_uri_from_prefix("foo1") == "bar1"
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchive()
try:
    archive.get_prefix_from_uri(1)
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################

#################################################
# srcml_archive_get_srcdiff_revision
################################################# 1
archive = pylibsrcml.srcMLArchive()
try:
    archive.get_srcdiff_revision()
except pylibsrcml.srcDiffRevisionInvalid:
    pass
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchive()
archive.set_srcdiff_revision(pylibsrcml.srcDiffRevision.ORIGINAL)
assert archive.get_srcdiff_revision() == pylibsrcml.srcDiffRevision.ORIGINAL
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchive()
try:
    archive.set_srcdiff_revision("foo")
except pylibsrcml.srcMLTypeError:
    pass
archive.close()
#################################################
