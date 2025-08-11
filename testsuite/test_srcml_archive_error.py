# SPDX-License-Identifier: GPL-3.0-only
"""
@file test_srcml_archive_error.py

@copyright Copyright (C) 2014-2025 srcML, LLC. (www.srcML.org)

This file is part of the pylibsrcml testsuite
"""

import pylibsrcml


#################################################
# srcml_archive_error_number
################################################# 1
archive = pylibsrcml.srcMLArchiveRead("data_small.xml")
try:
    archive.append_transform_xslt_filename("na.xsl")
    assert False
except pylibsrcml.srcMLException as e:
    assert e.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT
    print("|",archive.error_number())
    assert archive.error_number() == pylibsrcml.srcMLStatus.INVALID_ARGUMENT
