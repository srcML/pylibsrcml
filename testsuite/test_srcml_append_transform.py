import pylibsrcml

# with open("copy.xsl",'r') as file:
#     copy_str = file.read()
# with open("copy.xsl",'rb') as file:
#     copy_byt = file.read()

# with open("schema.rng",'r') as file:
#     schema_str = file.read()
# with open("schema.rng",'rb') as file:
#     schema_byt = file.read()

# #with open("schema.rng",'r') as file:
# #    schema = file.read()

# #################################################
# # archive.append_transform_xpath
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath("//src:unit")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath("//src:unit")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath(0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_xpath("//src:unit")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_xpath("//src:unit")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_xpath_attribute
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", "supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", "supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_attribute(0, "sup", "http://srcML.org/Supplement", "type", "supplement")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_attribute("//src:unit", 0, "http://srcML.org/Supplement", "type", "supplement")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_attribute("//src:unit", "sup", 0, "type", "supplement")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", 0, "supplement")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", 0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", "supplement")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", "supplement")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_xpath_element
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", "contain")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", "contain")
# archive.append_transform_xpath_attribute("//src:unit", "sup", "http://srcML.org/Supplement", "type", "supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", "contain")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_element(0, "sup", "http://srcML.org/Supplement", "contain")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_element("//src:unit", 0, "http://srcML.org/Supplement", "contain")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_element("//src:unit", "sup", 0, "contain")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", 0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", "contain")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_xpath_element("//src:unit", "sup", "http://srcML.org/Supplement", "contain")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_xslt_filename
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_filename(0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_filename("")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_filename("none.txt")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_xslt_filename("copy.xsl")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_xslt_filename("copy.xsl")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_filename("empty.txt")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_filename("wrong.txt")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_xslt_file
# #################################################
# with open("copy.xsl",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     archive.append_transform_xslt_file(copy)
#     archive.close()
# #################################################
# with open("copy.xsl",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     archive.append_transform_xslt_file(copy)
#     archive.close()
# #################################################
# with open("copy.xsl",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     try:
#         archive.append_transform_xslt_file(0)
#     except pylibsrcml.srcMLTypeError:
#         pass
#     archive.close()
# #################################################
# with open("copy.xsl",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     archive.c_archive = 0
#     try:
#         archive.append_transform_xslt_file(copy)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################
# with open("copy.xsl",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     archive.c_archive = None
#     try:
#         archive.append_transform_xslt_file(copy)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################
# with open("empty.txt",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     try:
#         archive.append_transform_xslt_file(copy)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################
# with open("wrong.txt",'r') as copy:
#     archive = pylibsrcml.srcml_archive()
#     try:
#         archive.append_transform_xslt_file(copy)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################



# #################################################
# # archive.append_transform_xslt_memory
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_memory(copy_byt)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_memory(copy_str)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_memory(copy_byt)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_memory(copy_str)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_memory(0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_memory(b"")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_xslt_memory("")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_xslt_memory(copy_byt)
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_xslt_memory(copy_byt)
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_xslt_memory(copy_str)
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_xslt_memory(copy_str)
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_xslt_FILE
# #################################################
# # DOES NOT EXIST IN PYTHON
# #################################################



# #################################################
# # archive.append_transform_xslt_fd
# #################################################
# # DOES NOT EXIST IN PYTHON - USED IN append_transform_xslt_file INSTEAD
# #################################################



# #################################################
# # archive.append_transform_relaxng_filename
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_relaxng_filename("schema.rng")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_relaxng_filename("schema.rng")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# try:
#     archive.append_transform_relaxng_filename(0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_relaxng_filename("schema.rng")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_relaxng_filename("schema.rng")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_relaxng_file
# #################################################
# with open("schema.rng",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     archive.append_transform_relaxng_file(schema)
#     archive.close()
# #################################################
# with open("schema.rng",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     archive.append_transform_relaxng_file(schema)
#     archive.close()
# #################################################
# with open("schema.rng",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     try:
#         archive.append_transform_relaxng_file(0)
#     except pylibsrcml.srcMLTypeError:
#         pass
#     archive.close()
# #################################################
# with open("schema.rng",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     archive.c_archive = 0
#     try:
#         archive.append_transform_relaxng_file(schema)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################
# with open("schema.rng",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     archive.c_archive = None
#     try:
#         archive.append_transform_relaxng_file(schema)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################
# with open("empty.txt",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     try:
#         archive.append_transform_relaxng_file(schema)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################
# with open("wrong.txt",'r') as schema:
#     archive = pylibsrcml.srcml_archive()
#     try:
#         archive.append_transform_relaxng_file(schema)
#     except pylibsrcml.srcMLException as err:
#         assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
#     archive.close()
# #################################################



# #################################################
# # archive.append_transform_relaxng_FILE
# #################################################
# # DOES NOT EXIST IN PYTHON
# #################################################



# #################################################
# # archive.append_transform_relaxng_fd
# #################################################
# # DOES NOT EXIST IN PYTHON - USED IN append_transform_relaxng_file INSTEAD
# #################################################



# #################################################
# # archive.append_transform_param
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# archive.append_transform_param("sup","http://srcML.org/Supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# archive.append_transform_param("sup","http://srcML.org/Supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_param("sup","http://srcML.org/Supplement")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_param("sup","http://srcML.org/Supplement")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# try:
#     archive.append_transform_param(0,"http://srcML.org/Supplement")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# try:
#     archive.append_transform_param("sup",0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_stringparam
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# archive.append_transform_stringparam("sup","http://srcML.org/Supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# archive.append_transform_stringparam("sup","http://srcML.org/Supplement")
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = 0
# try:
#     archive.append_transform_stringparam("sup","http://srcML.org/Supplement")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.c_archive = None
# try:
#     archive.append_transform_stringparam("sup","http://srcML.org/Supplement")
# except pylibsrcml.srcMLException as err:
#     assert(err.error_code == pylibsrcml.srcMLStatus.INVALID_ARGUMENT)
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# try:
#     archive.append_transform_stringparam(0,"http://srcML.org/Supplement")
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xslt_filename("copy.xsl")
# try:
#     archive.append_transform_stringparam("sup",0)
# except pylibsrcml.srcMLTypeError:
#     pass
# archive.close()
# #################################################



# #################################################
# # archive.append_transform_*
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.append_transform_xpath("//src:unit")
# archive.append_transform_xslt_filename("copy.xsl")
# archive.append_transform_xslt_memory(copy_byt)
# archive.append_transform_xslt_memory(copy_str)

# with open("copy.xsl",'r') as copy:
#     archive.append_transform_xslt_file(copy)

# archive.append_transform_param("sup","http://srcML.org/Supplement")
# archive.append_transform_stringparam("sup","http://srcML.org/Supplement")

# archive.append_transform_relaxng_filename("schema.rng")
# archive.append_transform_relaxng_memory(schema_str)
# archive.append_transform_relaxng_memory(schema_byt)

# with open("schema.rng",'r') as schema:
#     archive.append_transform_relaxng_file(schema)

# archive.close()
# #################################################

# """
# #################################################
# archive = pylibsrcml.srcml_archive()
# archive.close()
# #################################################
# """
