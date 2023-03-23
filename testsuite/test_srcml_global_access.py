import pylibsrcml

#################################################
# srcml_set_src_encoding
################################################# 1
try:
    pylibsrcml.set_src_encoding(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_src_encoding("foo")
assert pylibsrcml.get_src_encoding() == "foo"
#################################################


#################################################
# srcml_set_xml_encoding
################################################# 1
try:
    pylibsrcml.set_xml_encoding(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_xml_encoding("foo")
assert pylibsrcml.get_xml_encoding() == "foo"
#################################################


#################################################
# srcml_set_language
################################################# 1
try:
    pylibsrcml.set_language(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_language("foo")
assert pylibsrcml.get_language() == "foo"
#################################################


#################################################
# srcml_set_filename
################################################# 1
try:
    pylibsrcml.set_filename(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_filename("foo")
assert pylibsrcml.get_filename() == "foo"
#################################################


#################################################
# srcml_set_url
################################################# 1
try:
    pylibsrcml.set_url(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_url("foo")
assert pylibsrcml.get_url() == "foo"
#################################################


#################################################
# srcml_set_version
################################################# 1
try:
    pylibsrcml.set_version(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_version("foo")
assert pylibsrcml.get_version() == "foo"
#################################################


#################################################
# srcml_set_timestamp
################################################# 1
try:
    pylibsrcml.set_timestamp(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_timestamp("foo")
assert pylibsrcml.get_timestamp() == "foo"
#################################################


#################################################
# srcml_set_timestamp
################################################# 1
try:
    pylibsrcml.set_timestamp(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_timestamp("foo")
assert pylibsrcml.get_timestamp() == "foo"
#################################################


#################################################
# srcml_set_options
################################################# 1
try:
    pylibsrcml.set_options("foo")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_options(1 | 2 | 3)
assert pylibsrcml.get_options() == 1 | 2 | 3
################################################# 3
pylibsrcml.set_options(1 | 2 | 3)
pylibsrcml.set_options(1)
assert pylibsrcml.get_options() == 1
#################################################


#################################################
# srcml_enable_option
################################################# 1
try:
    pylibsrcml.enable_option("foo")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.enable_option(0)
pylibsrcml.enable_option(1)
assert pylibsrcml.get_options() == 1
################################################# 3
pylibsrcml.set_options(1 | 2)
pylibsrcml.enable_option(4)
assert pylibsrcml.get_options() == 1 | 2 | 4
################################################# 4
pylibsrcml.set_options(1)
pylibsrcml.enable_option(2 | 4)
assert pylibsrcml.get_options() == 1 | 2 | 4
#################################################


#################################################
# srcml_disable_option
################################################# 1
try:
    pylibsrcml.disable_option("foo")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_options(0)
pylibsrcml.disable_option(0)
assert pylibsrcml.get_options() == 0
################################################# 3
pylibsrcml.set_options(1 | 2 | 4)
pylibsrcml.disable_option(0)
assert pylibsrcml.get_options() == 1 | 2 | 4
################################################# 4
pylibsrcml.set_options(1 | 2 | 4)
pylibsrcml.disable_option(2)
assert pylibsrcml.get_options() == 1 | 4
################################################# 5
pylibsrcml.set_options(1 | 2 | 4)
pylibsrcml.disable_option(1 | 2)
assert pylibsrcml.get_options() == 4
#################################################


#################################################
# srcml_set_tabstop
################################################# 1
try:
    pylibsrcml.set_tabstop("foo")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 2
pylibsrcml.set_tabstop(2)
assert pylibsrcml.get_tabstop() == 2
#################################################


#################################################
# srcml_register_file_extension
################################################# 1
try:
    pylibsrcml.register_file_extension("foo","C+")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_INPUT
################################################# 2
try:
    pylibsrcml.register_file_extension("foo",0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 3
try:
    pylibsrcml.register_file_extension(0,"C++")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_register_namespace
################################################# 1
pylibsrcml.register_namespace("foo","bar")
assert pylibsrcml.get_namespace_prefix(pylibsrcml.get_namespace_size() - 1) == "foo"
assert pylibsrcml.get_namespace_uri(pylibsrcml.get_namespace_size() - 1) == "bar"
################################################# 2
pylibsrcml.register_namespace("foo2","bar")
assert pylibsrcml.get_namespace_prefix(pylibsrcml.get_namespace_size() - 1) == "foo2"
assert pylibsrcml.get_namespace_uri(pylibsrcml.get_namespace_size() - 1) == "bar"
################################################# 3
try:
    pylibsrcml.register_namespace("foo",0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
################################################# 4
try:
    pylibsrcml.register_namespace(0,"bar")
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_set_eol
################################################# 1
pylibsrcml.set_eol(pylibsrcml.SourceOutputEOL.CRLF)
assert pylibsrcml.get_eol() == pylibsrcml.SourceOutputEOL.CRLF
################################################# 2
pylibsrcml.set_eol(pylibsrcml.SourceOutputEOL.CRLF)
pylibsrcml.set_eol(pylibsrcml.SourceOutputEOL.AUTO)
assert pylibsrcml.get_eol() == pylibsrcml.SourceOutputEOL.AUTO
################################################# 3
try:
    pylibsrcml.set_eol(pylibsrcml.SourceOutputEOL.CRLF + 1)
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT
#################################################


#################################################
# srcml_set_srcdiff_revision
################################################# 1
pylibsrcml.set_srcdiff_revision(pylibsrcml.srcDiffRevision.ORIGINAL)
assert pylibsrcml.get_srcdiff_revision() == pylibsrcml.srcDiffRevision.ORIGINAL
################################################# 2
pylibsrcml.set_srcdiff_revision(pylibsrcml.srcDiffRevision.ORIGINAL)
pylibsrcml.set_srcdiff_revision(pylibsrcml.srcDiffRevision.MODIFIED)
assert pylibsrcml.get_srcdiff_revision() == pylibsrcml.srcDiffRevision.MODIFIED
################################################# 3
try:
    pylibsrcml.set_srcdiff_revision(pylibsrcml.srcDiffRevision.INVALID)
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT
#################################################


#################################################
# srcml_get_src_encoding
################################################# 1
pylibsrcml.set_src_encoding("")
assert pylibsrcml.get_src_encoding() == None
################################################# 2
pylibsrcml.set_src_encoding("foo")
assert pylibsrcml.get_src_encoding() == "foo"
#################################################


#################################################
# srcml_get_xml_encoding
################################################# 1
pylibsrcml.set_xml_encoding("")
assert pylibsrcml.get_xml_encoding() == None
################################################# 2
pylibsrcml.set_xml_encoding("foo")
assert pylibsrcml.get_xml_encoding() == "foo"
#################################################


#################################################
# srcml_get_revision
################################################# 1
assert pylibsrcml.get_revision() != ""
#################################################


#################################################
# srcml_get_language
################################################# 1
pylibsrcml.set_language("")
assert pylibsrcml.get_language() == None
################################################# 2
pylibsrcml.set_language("foo")
assert pylibsrcml.get_language() == "foo"
#################################################


#################################################
# srcml_get_filename
################################################# 1
pylibsrcml.set_filename("")
assert pylibsrcml.get_filename() == None
################################################# 2
pylibsrcml.set_filename("foo")
assert pylibsrcml.get_filename() == "foo"
#################################################


#################################################
# srcml_get_url
################################################# 1
pylibsrcml.set_url("")
assert pylibsrcml.get_url() == None
################################################# 2
pylibsrcml.set_url("foo")
assert pylibsrcml.get_url() == "foo"
#################################################


#################################################
# srcml_get_version
################################################# 1
pylibsrcml.set_version("")
assert pylibsrcml.get_version() == None
################################################# 2
pylibsrcml.set_version("foo")
assert pylibsrcml.get_version() == "foo"
#################################################


#################################################
# srcml_get_timestamp
################################################# 1
pylibsrcml.set_timestamp("")
assert pylibsrcml.get_timestamp() == None
################################################# 2
pylibsrcml.set_timestamp("foo")
assert pylibsrcml.get_timestamp() == "foo"
#################################################


#################################################
# srcml_get_hash
################################################# 1
assert pylibsrcml.get_hash() == None
################################################# 2


#################################################
# srcml_get_options
################################################# 1
pylibsrcml.set_options(1)
assert pylibsrcml.get_options() == 1
################################################# 2
pylibsrcml.set_options(1 | 2)
assert pylibsrcml.get_options() == 1 | 2
#################################################


#################################################
# srcml_get_tabstop
################################################# 1
pylibsrcml.set_tabstop(4)
assert pylibsrcml.get_tabstop() == 4
#################################################


#################################################
# srcml_get_namespace_size
################################################# 1
assert pylibsrcml.get_namespace_size() == 2
################################################# 2
pylibsrcml.register_namespace("foo2","bar2")
pylibsrcml.register_namespace("foo3","bar3")
assert pylibsrcml.get_namespace_size() == 4
#################################################


#################################################
# srcml_get_namespace_prefix
################################################# 1
assert pylibsrcml.get_namespace_prefix(1) == "foo2"
################################################# 2
assert pylibsrcml.get_namespace_prefix(-1) == None
################################################# 3
assert pylibsrcml.get_namespace_prefix(5) == None
#################################################


#################################################
# srcml_get_prefix_from_uri
################################################# 1
assert pylibsrcml.get_prefix_from_uri("bar2") == "foo2"
################################################# 2
assert pylibsrcml.get_prefix_from_uri("bar4") == None
################################################# 3
try:
    pylibsrcml.get_prefix_from_uri(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_get_namespace_uri
################################################# 1
assert pylibsrcml.get_namespace_uri(1) == "bar"
################################################# 2
assert pylibsrcml.get_namespace_uri(-1) == None
################################################# 3
assert pylibsrcml.get_namespace_uri(4) == None
#################################################


#################################################
# srcml_get_uri_from_prefix
################################################# 1
assert pylibsrcml.get_uri_from_prefix("foo2") == "bar2"
################################################# 2
assert pylibsrcml.get_uri_from_prefix("foo4") == None
################################################# 3
try:
    pylibsrcml.get_uri_from_prefix(0)
    assert False
except pylibsrcml.srcMLTypeError:
    pass
#################################################


#################################################
# srcml_get_srcdiff_revision
################################################# 1
pylibsrcml.set_srcdiff_revision(0)
assert pylibsrcml.get_srcdiff_revision() == 0
################################################# 2
pylibsrcml.set_srcdiff_revision(pylibsrcml.srcDiffRevision.ORIGINAL)
assert pylibsrcml.get_srcdiff_revision() == pylibsrcml.srcDiffRevision.ORIGINAL
#################################################
