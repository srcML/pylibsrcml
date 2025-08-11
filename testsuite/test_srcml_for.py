# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_for.py

@copyright Copyright (C) 2014-2024 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

import pylibsrcml

SRCML_VERSION_STRING = pylibsrcml.version_string()

srcml_a = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>"""

srcml_b = f"""<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}" language="C++" filename="b.cpp"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>"""

srcml_single = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}">

<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

</unit>
"""

srcml_double = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<unit xmlns="http://www.srcML.org/srcML/src" revision="{SRCML_VERSION_STRING}">

<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="a.cpp"><expr_stmt><expr><name>a</name></expr>;</expr_stmt>
</unit>

<unit revision="{SRCML_VERSION_STRING}" language="C++" filename="b.cpp"><expr_stmt><expr><name>b</name></expr>;</expr_stmt>
</unit>

</unit>
"""

with open("data_small.xml") as file:
    data_small = file.read()

data_small_unit_text = []
with pylibsrcml.srcMLArchiveRead("data_small.xml") as data_arch:
    unit = data_arch.read_unit()
    while unit != None:
        data_small_unit_text.append(unit.get_srcml())
        unit = data_arch.read_unit()

with open("data_big.xml") as file:
    data_big = file.read()

data_big_unit_text = []
with pylibsrcml.srcMLArchiveRead("data_big.xml") as data_arch:
    unit = data_arch.read_unit()
    while unit != None:
        data_big_unit_text.append(unit.get_srcml())
        unit = data_arch.read_unit()

#################################################
# srcMLArchive for loop
################################################# 1
archive = pylibsrcml.srcMLArchiveRead(srcml_single)
i = 0
for unit in archive:
    assert unit.get_srcml() == srcml_a
    i += 1
assert i == 1
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveRead(srcml_double)
i = 0
for unit in archive:
    assert unit.get_srcml() == srcml_a if i == 0 else srcml_b
    i += 1
assert i == 2
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveRead(data_small)
i = 0
for unit in archive:
    assert unit.get_srcml() == data_small_unit_text[i]
    i += 1
assert i == len(data_small_unit_text)
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveRead(data_big)
i = 0
for unit in archive:
    assert unit.get_srcml() == data_big_unit_text[i]
    i += 1
assert i == len(data_big_unit_text)
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchiveRead("data_small.xml")
i = 0
for unit in archive:
    assert unit.get_srcml() == data_small_unit_text[i]
    i += 1
assert i == len(data_small_unit_text)
archive.close()
################################################# 6
archive = pylibsrcml.srcMLArchiveRead("data_big.xml")
i = 0
for unit in archive:
    assert unit.get_srcml() == data_big_unit_text[i]
    i += 1
assert i == len(data_big_unit_text)
archive.close()
#################################################


small_if_count = []
with pylibsrcml.srcMLArchiveRead("data_small.xml") as archive:
    archive.append_transform_xpath("count(//src:if_stmt)")
    for unit in archive:
        result = archive.unit_apply_transforms(unit)
        small_if_count.append(result.get_number())
big_if_count = []
with pylibsrcml.srcMLArchiveRead("data_big.xml") as archive:
    archive.append_transform_xpath("count(//src:if_stmt)")
    for unit in archive:
        result = archive.unit_apply_transforms(unit)
        big_if_count.append(result.get_number())
#################################################
# srcMLTransform for loop
################################################# 1
archive = pylibsrcml.srcMLArchiveRead("data_small.xml")
archive.append_transform_xpath("//src:unit")
i = 0
for unit in archive:
    result = archive.unit_apply_transforms(unit)
    assert result.get_type() == pylibsrcml.srcMLResult.UNITS
    assert len(result) == 1
    assert data_small_unit_text[i] == result[0].get_srcml()
    i += 1
archive.close()
################################################# 2
archive = pylibsrcml.srcMLArchiveRead("data_big.xml")
archive.append_transform_xpath("//src:unit")
i = 0
for unit in archive:
    result = archive.unit_apply_transforms(unit)
    assert result.get_type() == pylibsrcml.srcMLResult.UNITS
    assert len(result) == 1
    assert data_big_unit_text[i] == result[0].get_srcml()
    i += 1
archive.close()
################################################# 3
archive = pylibsrcml.srcMLArchiveRead("data_small.xml")
archive.append_transform_xpath("//src:if_stmt")
i = 0
for unit in archive:
    result = archive.unit_apply_transforms(unit)
    if result.get_type() == pylibsrcml.srcMLResult.NONE:
        assert small_if_count[i] == 0
    else:
        assert result.get_type() == pylibsrcml.srcMLResult.UNITS
        assert len(result) == small_if_count[i]
    i += 1
archive.close()
################################################# 4
archive = pylibsrcml.srcMLArchiveRead("data_big.xml")
archive.append_transform_xpath("//src:if_stmt")
i = 0
for unit in archive:
    result = archive.unit_apply_transforms(unit)
    if result.get_type() == pylibsrcml.srcMLResult.NONE:
        assert big_if_count[i] == 0
    else:
        assert result.get_type() == pylibsrcml.srcMLResult.UNITS
        assert len(result) == big_if_count[i]
    i += 1
archive.close()
################################################# 5
archive = pylibsrcml.srcMLArchiveRead("data_small.xml")
archive.append_transform_xpath("//src:if_stmt")
for unit in archive:
    result = archive.unit_apply_transforms(unit)
    if result.get_type() != pylibsrcml.srcMLResult.NONE:
        i = 0
        for unit in result:
            assert str(unit).startswith("<if_stmt") and str(unit).endswith("</if_stmt>")
            i += 1
        assert i == len(result)
################################################# 6
archive = pylibsrcml.srcMLArchiveRead("data_big.xml")
archive.append_transform_xpath("//src:if_stmt")
i = 0
for unit in archive:
    result = archive.unit_apply_transforms(unit)
    if result.get_type() != pylibsrcml.srcMLResult.NONE:
        i = 0
        for unit in result:
            assert str(unit).startswith("<if_stmt") and str(unit).endswith("</if_stmt>")
            i += 1
        assert i == len(result)
#################################################
