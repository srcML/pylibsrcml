import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()


srcml_a = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""


srcml_b = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<s:unit xmlns:s="http://www.srcML.org/srcML/src" revision=")"{SRCML_VERSION_STRING}" language="C++" filename="project" version="1"><s:expr_stmt><s:expr><s:name>b</s:name></s:expr>;</s:expr_stmt>
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
#################################################
iarchive = pylibsrcml.srcml_archive()
iarchive.read_open_memory(srcml)
iarchive.append_transform_xpath("//src:unit")
oarchive = iarchive.clone()
#s = iarchive.write_open_string()
#oarchive.write_open_string()

unit = iarchive.read_unit()
result = pylibsrcml.srcml_transform_result()
print("BEF",result.c_res)
iarchive.unit_apply_transforms(unit,result)
print("AFT",result.c_res)

assert result.get_type() == pylibsrcml.srcMLResult.UNITS
print("AFT2",result.c_res)
x = result.get_unit(0)
print("OG Unit",unit.c_unit)
print("X  Unit",x.c_unit)
print("AFT3",result.c_res)
print("UNIT",x.c_unit)
print("BUFBEF",oarchive.buffer)
#oarchive.write_unit(x)
print("BUFAFT",oarchive.buffer)
print("AFT4",result.c_res)

print("ID1",id(x))
print("ID2",id(unit))


print("Closing")
iarchive.close()
print("AFT5",result.c_res)
oarchive.close()
print("AFT6",result.c_res)

print("MANUAL DELETES")
#del x
del unit

del result

del x

print("AUTO DELETES HAPPEN NOW!!!")

#print(globals())
#################################################










"""
#################################################
archive = pylibsrcml.srcml_archive()
archive.close()
#################################################
"""
