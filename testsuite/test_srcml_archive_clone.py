import pylibsrcml

empty = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><unit/>'

srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{pylibsrcml.version_string()}">

<unit revision="{pylibsrcml.version_string()}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>"""

template_archive = pylibsrcml.srcMLArchive()
template_archive.set_src_encoding("e")
template_archive.set_url("u")
template_archive.set_version("v")
template_archive.set_options(1 | 2)
template_archive.set_tabstop(4)
template_archive.register_namespace("s","http://www.srcML.org/srcML/src")
template_archive.register_namespace("foo","bar")

archives = [pylibsrcml.srcMLArchiveRead(empty, string_read_mode = "source", clone_from = template_archive),
            pylibsrcml.srcMLArchiveWrite("output1.xml", clone_from = template_archive),
            pylibsrcml.srcMLArchiveWriteString(clone_from = template_archive)]

for archive in archives:
    assert archive.get_src_encoding() == "e"
    assert archive.get_url() == "u"
    assert archive.get_version() == "v"
    assert archive.get_options() == 1 | 2
    assert archive.get_tabstop() == 4
    assert archive.get_namespace_prefix(0) == "s"
    assert archive.get_namespace_uri(0) == "http://www.srcML.org/srcML/src"
    assert archive.get_namespace_prefix(1) == "foo"
    assert archive.get_namespace_uri(1) == "bar"
    assert archive.get_namespace_size() == 2
    archive.close()


template_archive = pylibsrcml.srcMLArchiveRead(srcml)
template_archive.append_transform_xpath("string(//src:unit/@language)")


copy_archive = pylibsrcml.srcMLArchiveRead(srcml, clone_from = template_archive)
unit = copy_archive.read_unit()
result = copy_archive.unit_apply_transforms(unit)

assert result.get_type() == pylibsrcml.srcMLResult.STRING
assert result.get_string() == "C++"


template_archive.close()
copy_archive.close()
