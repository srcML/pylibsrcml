import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()


srcml_a = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""


srcml_b = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>"""


srcml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}">

<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>"""


srcml_a_after = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}">

<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>"""


srcml_b_after = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" version="1">

<s:unit revision="{SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>"""


srcml_full = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}">

<s:unit revision="{SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>"""


srcml_full_python = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}">

<s:unit revision="{SRCML_VERSION_STRING}" language="Python" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
</s:unit>

</s:unit>"""


string_xsl = """<xsl:stylesheet
    xmlns="http://www.srcML.org/srcML/src"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:cpp="http://www.srcML.org/srcML/cpp"
    version="1.0">
<xsl:output method="text"/>
<xsl:template match="/"><xsl:value-of select="'srcML'"/></xsl:template>
</xsl:stylesheet>"""

with open("copy.xsl",'r') as file:
    copy = file.read()
with open("copy.xsl",'r') as file:
    inlang = file.read()
with open("schema.rng",'r') as file:
    schema = file.read()


#################################################
# xpath
################################################# 1
iarchive = pylibsrcml.srcMLArchiveRead(srcml)
iarchive.append_transform_xpath("//src:unit")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
output_unit = result.get_unit(0)
oarchive.write_unit(output_unit)


iarchive.close()
s = oarchive.close()
assert s == srcml
assert oarchive.get_output_string() == srcml
assert oarchive.get_output_string() == s
################################################# 2
iarchive = pylibsrcml.srcMLArchiveRead(srcml_full)
iarchive.append_transform_xpath("//src:unit")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_full
assert oarchive.get_output_string() == srcml_full
assert oarchive.get_output_string() == s
################################################# 3
iarchive = pylibsrcml.srcMLArchiveRead(srcml_a)
iarchive.append_transform_xpath("//src:unit")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)
oarchive.disable_solitary_unit()

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_a_after
assert oarchive.get_output_string() == s
assert oarchive.get_output_string() == srcml_a_after
################################################# 4
iarchive = pylibsrcml.srcMLArchiveRead(srcml_b)
iarchive.append_transform_xpath("//src:unit")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)
oarchive.disable_solitary_unit()

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_b_after
assert oarchive.get_output_string() == s
assert oarchive.get_output_string() == srcml_b_after
################################################# 5


#################################################
# xpath number result
################################################# 1
iarchive = pylibsrcml.srcMLArchiveRead(srcml)
iarchive.append_transform_xpath("count(//src:unit)")

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.NUMBER
assert result.get_number() == 1.0

iarchive.close()
#################################################


#################################################
# xpath boolean result
################################################# 1
iarchive = pylibsrcml.srcMLArchiveRead(srcml)
iarchive.append_transform_xpath("count(//src:unit)!=1")

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.BOOLEAN
assert result.get_bool() == False

iarchive.close()
#################################################


#################################################
# xpath boolean string
################################################# 1
iarchive = pylibsrcml.srcMLArchiveRead(srcml)
iarchive.append_transform_xpath("string(//src:unit/@language)")

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.STRING
assert result.get_string() == "C++"

iarchive.close()
#################################################


#################################################
# xslt_filename
################################################# 1
iarchive = pylibsrcml.srcMLArchiveRead(srcml)
iarchive.append_transform_xslt_filename("copy.xsl")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
assert (not result.get_unit(0)) == False

oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml
assert oarchive.get_output_string() == srcml
assert oarchive.get_output_string() == s
################################################# 2
iarchive = pylibsrcml.srcMLArchiveRead(srcml_full)
iarchive.append_transform_xslt_filename("copy.xsl")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
assert (not result.get_unit(0)) == False

oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_full
assert oarchive.get_output_string() == srcml_full
assert oarchive.get_output_string() == s
################################################# 3
iarchive = pylibsrcml.srcMLArchiveRead(srcml_a)
iarchive.append_transform_xslt_filename("copy.xsl")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
assert (not result.get_unit(0)) == False

oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_a
assert oarchive.get_output_string() == srcml_a
assert oarchive.get_output_string() == s
################################################# 4
iarchive = pylibsrcml.srcMLArchiveRead(srcml_b)
iarchive.append_transform_xslt_filename("copy.xsl")
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
assert (not result.get_unit(0)) == False

oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_b
assert oarchive.get_output_string() == srcml_b
assert oarchive.get_output_string() == s
#################################################
iarchive = pylibsrcml.srcMLArchiveRead(srcml_full)
iarchive.append_transform_xslt_filename("setlanguage.xsl")
iarchive.append_transform_param("language",'"Python"')
oarchive = pylibsrcml.srcMLArchiveWriteString.clone(iarchive)

unit = iarchive.read_unit()
result = pylibsrcml.srcMLTransformResult()
iarchive.unit_apply_transforms(unit,result)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
assert result.get_unit_size() == 1
assert (not result.get_unit(0)) == False

oarchive.write_unit(result.get_unit(0))

iarchive.close()
s = oarchive.close()

assert s == srcml_full_python
assert oarchive.get_output_string() == srcml_full_python
assert s == oarchive.get_output_string()
#################################################


#################################################
# xslt_memory
################################################# 1
iarchive = pylibsrcml.srcMLArchiveRead(srcml)
iarchive.append_transform_xslt_memory()

"""
#################################################
archive = pylibsrcml.srcml_archive()
archive.close()
#################################################
"""
