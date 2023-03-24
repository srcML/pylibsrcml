import pylibsrcml

srcml_a = f"""<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_b = f"""<s:unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>"""

srcml_b_single = f"""<s:unit xmlns:s="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C++" url="test" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>"""

srcml_b_two = f"""<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C" filename="project.c"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>"""

srcml_timestamp_inner = f"""<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" timestamp="today" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_timestamp_single_inner = f"""<unit xmlns="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" timestamp="today" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_hash_inner = f"""<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" hash="aa2a72b26cf958d8718a2e9bc6b84679a81d54cb" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_hash_single_inner = f"""<unit xmlns="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" hash="aa2a72b26cf958d8718a2e9bc6b84679a81d54cb" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src">

<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_soleunit = f"""<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_full = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" url="test">

<s:unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>
"""

srcml_single = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C++" url="test" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>
"""

srcml_two = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src">

<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" language="C" filename="project.c"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_timestamp = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src">

<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" timestamp="today" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_timestamp_single = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" timestamp="today" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

srcml_hash = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src">

<unit xmlns:cpp="http://www.srcML.org/srcML/cpp" hash="aa2a72b26cf958d8718a2e9bc6b84679a81d54cb" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_hash_single = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" xmlns:cpp="http://www.srcML.org/srcML/cpp" hash="aa2a72b26cf958d8718a2e9bc6b84679a81d54cb" language="C" filename="project.c"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>
"""

#################################################
# srcml_archive_read_unit
################################################# 1
archive = pylibsrcml.srcMLArchiveRead(srcml)
unit = archive.read_unit()
assert unit.get_srcml_outer() == srcml_a
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveRead(srcml_full)
unit = archive.read_unit()
assert unit.get_language() == "C++"
assert unit.get_filename() == "project"
assert unit.get_version() == "1"
assert unit.get_srcml_outer() == srcml_b
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveRead(srcml_single)
unit = archive.read_unit()
assert unit.get_language() == "C++"
assert unit.get_filename() == "project"
assert archive.get_url() == "test"
assert unit.get_version() == "1"
assert unit.get_srcml() == srcml_b_single
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveRead(srcml_two)
unit = archive.read_unit()
assert unit.get_language() == "C"
assert unit.get_filename() == "project.c"
assert archive.get_url() == None
assert unit.get_version() == None
assert unit.get_srcml_outer() == srcml_a
unit = archive.read_unit()
assert unit.get_language() == "C"
assert unit.get_filename() == "project.c"
assert archive.get_url() == None
assert unit.get_version() == None
assert unit.get_srcml_outer() == srcml_b_two
unit = archive.read_unit()
assert unit == None
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchiveRead(srcml_timestamp)
unit = archive.read_unit()
assert unit.get_timestamp() == "today"
archive.close()
################################################# 6
archive = pylibsrcml.srcMLArchiveRead(srcml_timestamp_single)
unit = archive.read_unit()
assert unit.get_timestamp() == "today"
archive.close()
################################################# 7
archive = pylibsrcml.srcMLArchiveRead(srcml_hash)
unit = archive.read_unit()
assert unit.get_hash() == "aa2a72b26cf958d8718a2e9bc6b84679a81d54cb"
archive.close()
################################################# 8
archive = pylibsrcml.srcMLArchiveRead(srcml_hash_single)
unit = archive.read_unit()
assert unit.get_hash() == "aa2a72b26cf958d8718a2e9bc6b84679a81d54cb"
archive.close()
################################################# 9
archive = pylibsrcml.srcMLArchiveRead(srcml)
unit = archive.read_unit()
assert unit.get_language() == "C"
assert unit.get_filename() == "project.c"
assert archive.get_url() == None
assert unit.get_version() == None
assert unit.get_srcml_outer() == srcml_soleunit
archive.close()
################################################# 10
archive = pylibsrcml.srcMLArchiveRead(srcml_full)
unit = archive.read_unit()
assert unit.get_language() == "C++"
assert unit.get_filename() == "project"
assert archive.get_url() == "test"
assert unit.get_version() == "1"
assert unit.get_srcml_inner() == "<s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>\n"
archive.close()
################################################# 11
archive = pylibsrcml.srcMLArchiveRead(srcml_single)
unit = archive.read_unit()
assert unit.get_language() == "C++"
assert unit.get_filename() == "project"
assert archive.get_url() == "test"
assert unit.get_version() == "1"
assert unit.get_srcml_inner() == "<s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>\n"
archive.close()
################################################# 12
archive = pylibsrcml.srcMLArchiveRead(srcml_two)
unit = archive.read_unit()
assert unit.get_language() == "C"
assert unit.get_filename() == "project.c"
assert archive.get_url() == None
assert unit.get_version() == None
assert unit.get_srcml_inner() == "<expr_stmt><expr><name>a</name></expr>;</expr_stmt>\n"
unit = archive.read_unit()
assert unit.get_language() == "C"
assert unit.get_filename() == "project.c"
assert archive.get_url() == None
assert unit.get_version() == None
assert unit.get_srcml_inner() == "<expr_stmt><expr><name>b</name></expr>;</expr_stmt>\n"
unit = archive.read_unit()
assert unit == None
archive.close()
#################################################
