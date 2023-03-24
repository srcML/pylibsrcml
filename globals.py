from .exceptions import srcMLNotFoundError

from ctypes import cdll
from ctypes.util import find_library
from ctypes import c_int, c_char_p, c_size_t, c_void_p, c_double, CFUNCTYPE
write_callback_t = CFUNCTYPE(c_int, c_void_p, c_char_p, c_size_t)
read_callback_t  = CFUNCTYPE(c_int, c_char_p, c_size_t)
close_callback_t = CFUNCTYPE(c_int, c_void_p)

LIBSRCML_PATH = find_library("srcml") if find_library("srcml") != None else find_library("libsrcml")
if(LIBSRCML_PATH == None):
    raise srcMLNotFoundError

libsrcml = cdll.LoadLibrary(LIBSRCML_PATH)

# UTILITY

# int srcml_version_number();
libsrcml.srcml_version_number.restype = c_int
libsrcml.srcml_version_number.argtypes = []

# const char* srcml_version_string();
libsrcml.srcml_version_string.restype = c_char_p
libsrcml.srcml_version_string_argtypes = []

# int srcml_check_language(const char* language);
libsrcml.srcml_check_language.restype = c_int
libsrcml.srcml_check_language.argtypes = [c_char_p]

# const char* srcml_check_extension(const char* filename);
libsrcml.srcml_check_extension.restype = c_char_p
libsrcml.srcml_check_extension.argtypes = [c_char_p]

# size_t srcml_get_language_list_size();
libsrcml.srcml_get_language_list_size.restype = c_size_t
libsrcml.srcml_get_language_list_size.argtypes = []

# const char* srcml_get_language_list(size_t pos);
libsrcml.srcml_get_language_list.restype = c_char_p
libsrcml.srcml_get_language_list.argtypes = [c_size_t]

# int srcml_check_encoding(const char* encoding);
libsrcml.srcml_check_encoding.restype = c_int
libsrcml.srcml_check_encoding.argtypes = [c_char_p]

# int srcml_check_xslt();
libsrcml.srcml_check_xslt.restype = c_int
libsrcml.srcml_check_xslt.argtypes = []

# int srcml_check_exslt();
libsrcml.srcml_check_exslt.restype = c_int
libsrcml.srcml_check_exslt.argtypes = []

# const char* srcml_error_string();
libsrcml.srcml_error_string.restype = c_char_p
libsrcml.srcml_error_string.argtypes = []

# void srcml_memory_free(char * buffer);
libsrcml.srcml_memory_free.restype = None
libsrcml.srcml_memory_free.argtypes = [c_char_p]

# CONVENIENCE

# int srcml(const char* input_filename, const char* output_filename);
libsrcml.srcml.restype = c_int
libsrcml.srcml.argtypes = [c_char_p, c_char_p]

# int srcml_set_src_encoding(const char* encoding);
libsrcml.srcml_set_src_encoding.restype = c_int
libsrcml.srcml_set_src_encoding.argtypes = [c_char_p]

# int srcml_set_xml_encoding(const char* encoding);
libsrcml.srcml_set_xml_encoding.restype = c_int
libsrcml.srcml_set_xml_encoding.argtypes = [c_char_p]

# int srcml_set_language(const char* language);
libsrcml.srcml_set_language.restype = c_int
libsrcml.srcml_set_language.argtypes = [c_char_p]

# int srcml_set_filename(const char* filename);
libsrcml.srcml_set_filename.restype = c_int
libsrcml.srcml_set_filename.argtypes = [c_char_p]

# int srcml_set_url(const char* url);
libsrcml.srcml_set_url.restype = c_int
libsrcml.srcml_set_url.argtypes = [c_char_p]

# int srcml_set_version(const char* version);
libsrcml.srcml_set_version.restype = c_int
libsrcml.srcml_set_version.argtypes = [c_char_p]  

# int srcml_set_timestamp(const char* timestamp);
libsrcml.srcml_set_timestamp.restype = c_int
libsrcml.srcml_set_timestamp.argtypes = [c_char_p]

# int srcml_set_options(size_t option);
libsrcml.srcml_set_options.restype = c_int
libsrcml.srcml_set_options.argtypes = [c_size_t]

# int srcml_enable_option(size_t option);
libsrcml.srcml_enable_option.restype = c_int
libsrcml.srcml_enable_option.argtypes = [c_size_t]

# int srcml_disable_option(size_t option);
libsrcml.srcml_disable_option.restype = c_int
libsrcml.srcml_disable_option.argtypes = [c_size_t]

# int srcml_set_tabstop(size_t tabstop);
libsrcml.srcml_set_tabstop.restype = c_int
libsrcml.srcml_set_tabstop.argtypes = [c_size_t]

# int srcml_register_file_extension(const char* extension, const char* language);
libsrcml.srcml_register_file_extension.restype = c_int
libsrcml.srcml_register_file_extension.argtypes = [c_char_p, c_char_p]

# int srcml_register_namespace(const char* prefix, const char* ns);
libsrcml.srcml_register_namespace.restype = c_int
libsrcml.srcml_register_namespace.argtypes = [c_char_p, c_char_p]

# int srcml_set_processing_instruction(const char* target, const char* data);
libsrcml.srcml_set_processing_instruction.restype = c_int
libsrcml.srcml_set_processing_instruction.argtypes = [c_char_p, c_char_p]

# int srcml_set_eol(size_t eol);
libsrcml.srcml_set_eol.restype = c_int
libsrcml.srcml_set_eol.argtypes = [c_size_t]

# int srcml_set_srcdiff_revision(size_t revision_number);
libsrcml.srcml_set_srcdiff_revision.restype = c_int
libsrcml.srcml_set_srcdiff_revision.argtypes = [c_size_t]

# const char* srcml_get_src_encoding();
libsrcml.srcml_get_src_encoding.restype = c_char_p
libsrcml.srcml_get_src_encoding.argtypes = []

# const char* srcml_get_xml_encoding();
libsrcml.srcml_get_xml_encoding.restype = c_char_p
libsrcml.srcml_get_xml_encoding.argtypes = []

# const char* srcml_get_revision();
libsrcml.srcml_get_revision.restype = c_char_p
libsrcml.srcml_get_revision.argtypes = []

# const char* srcml_get_language();
libsrcml.srcml_get_language.restype = c_char_p
libsrcml.srcml_get_language.argtypes = []

# const char* srcml_get_filename();
libsrcml.srcml_get_filename.restype = c_char_p
libsrcml.srcml_get_filename.argtypes = []

# const char* srcml_get_url();
libsrcml.srcml_get_url.restype = c_char_p
libsrcml.srcml_get_url.argtypes = []

# const char* srcml_get_version();
libsrcml.srcml_get_version.restype = c_char_p
libsrcml.srcml_get_version.argtypes = []

# const char* srcml_get_timestamp();
libsrcml.srcml_get_timestamp.restype = c_char_p
libsrcml.srcml_get_timestamp.argtypes = []

# const char* srcml_get_hash();
libsrcml.srcml_get_hash.restype = c_char_p
libsrcml.srcml_get_hash.argtypes = []

# int srcml_get_loc();
libsrcml.srcml_get_loc.restype = c_int
libsrcml.srcml_get_loc.argtypes = []

# size_t srcml_get_eol();
libsrcml.srcml_get_eol.restypes = c_size_t
libsrcml.srcml_get_eol.argtypes = []

# size_t srcml_get_srcdiff_revision();
libsrcml.srcml_get_srcdiff_revision.restype = c_size_t
libsrcml.srcml_get_srcdiff_revision.argtypes = []

# int srcml_get_options();
libsrcml.srcml_get_options.restype = c_int
libsrcml.srcml_get_options.argtypes = []

# size_t srcml_get_tabstop();
libsrcml.srcml_get_tabstop.restype = c_size_t
libsrcml.srcml_get_tabstop.argtypes = []

# const char* srcml_get_processing_instruction_target();
libsrcml.srcml_get_processing_instruction_target.restype = c_char_p
libsrcml.srcml_get_processing_instruction_target.argtypes = []

# const char* srcml_get_processing_instruction_data();
libsrcml.srcml_get_processing_instruction_data.restype = c_char_p
libsrcml.srcml_get_processing_instruction_data.argtypes = []

# size_t srcml_get_namespace_size();
libsrcml.srcml_get_namespace_size.restype = c_size_t
libsrcml.srcml_get_namespace_size.argtypes = []

# const char* srcml_get_namespace_prefix(size_t pos);
libsrcml.srcml_get_namespace_prefix.restype = c_char_p
libsrcml.srcml_get_namespace_prefix.argtypes = [c_size_t]

# const char* srcml_get_prefix_from_uri(const char* namespace_uri);
libsrcml.srcml_get_prefix_from_uri.restype = c_char_p
libsrcml.srcml_get_prefix_from_uri.argtypes = [c_char_p]

# const char* srcml_get_namespace_uri(size_t pos);
libsrcml.srcml_get_namespace_uri.restype = c_char_p
libsrcml.srcml_get_namespace_uri.argtypes = [c_size_t]

# const char* srcml_get_uri_from_prefix(const char* prefix);
libsrcml.srcml_get_uri_from_prefix.restype = c_char_p
libsrcml.srcml_get_uri_from_prefix.argtypes = [c_char_p]

# void srcml_cleanup_globals();
libsrcml.srcml_cleanup_globals.restype = None
libsrcml.srcml_cleanup_globals.argtypes = []

# ARCHIVE

# struct srcml_archive* srcml_archive_create();
libsrcml.srcml_archive_create.restype = c_void_p
libsrcml.srcml_archive_create.argtypes = []

# struct srcml_archive* srcml_archive_clone(const struct srcml_archive* archive);
libsrcml.srcml_archive_clone.restype = c_void_p
libsrcml.srcml_archive_clone.argtypes = [c_void_p]

# int srcml_archive_error_number(const struct srcml_archive* archive);
libsrcml.srcml_archive_error_number.restype = c_int
libsrcml.srcml_archive_error_number.argtypes = [c_void_p]

# const char* srcml_archive_error_string(const struct srcml_archive* archive);
libsrcml.srcml_archive_error_string.restype = c_char_p
libsrcml.srcml_archive_error_string.argtypes = [c_void_p]

# int srcml_archive_write_unit(struct srcml_archive* archive, struct srcml_unit* unit);
libsrcml.srcml_archive_write_unit.restype = c_int
libsrcml.srcml_archive_write_unit.argtypes = [c_void_p, c_void_p]

# int srcml_archive_write_string(struct srcml_archive* archive, const char* s, int len);
libsrcml.srcml_archive_write_string.restype = c_int
libsrcml.srcml_archive_write_string.argtypes = [c_void_p, c_char_p, c_int]

# void srcml_archive_close(struct srcml_archive* archive);
libsrcml.srcml_archive_close.restype = None
libsrcml.srcml_archive_close.argtypes = [c_void_p]

# void srcml_archive_free(struct srcml_archive* archive);
libsrcml.srcml_archive_free.restype = None
libsrcml.srcml_archive_free.argtypes = [c_void_p]

# int srcml_archive_write_open_filename(struct srcml_archive* archive, const char* srcml_filename);
libsrcml.srcml_archive_write_open_filename.restype = c_int
libsrcml.srcml_archive_write_open_filename.argtypes = [c_void_p, c_char_p]

# int srcml_archive_write_open_memory(struct srcml_archive* archive, char** buffer, size_t * size);
libsrcml.srcml_archive_write_open_memory.restype = c_int
libsrcml.srcml_archive_write_open_memory.argtypes = [c_void_p, c_void_p, c_void_p]

# int srcml_archive_write_open_FILE(struct srcml_archive* archive, FILE* srcml_file);
libsrcml.srcml_archive_write_open_FILE.restype = c_int
libsrcml.srcml_archive_write_open_FILE.argtypes = [c_void_p, c_void_p]

# int srcml_archive_write_open_fd(struct srcml_archive* archive, int srcml_fd);
libsrcml.srcml_archive_write_open_fd.restype = c_int
libsrcml.srcml_archive_write_open_fd.argtypes = [c_void_p, c_int]

# int srcml_archive_write_open_io(struct srcml_archive* archive, void * context, int (*write_callback)(void * context, const char* buffer, int len), int (*close_callback)(void * context));
libsrcml.srcml_archive_write_open_io.restype = c_int
libsrcml.srcml_archive_write_open_io.argtypes = [c_void_p, c_void_p, write_callback_t, close_callback_t]

# int srcml_archive_read_open_filename(struct srcml_archive* archive, const char* srcml_filename);
libsrcml.srcml_archive_read_open_filename.restype = c_int
libsrcml.srcml_archive_read_open_filename.argtypes = [c_void_p, c_char_p]

# int srcml_archive_read_open_memory(struct srcml_archive* archive, const char* buffer, size_t buffer_size);
libsrcml.srcml_archive_read_open_memory.restype = c_int
libsrcml.srcml_archive_read_open_memory.argtypes = [c_void_p, c_char_p, c_size_t]

# int srcml_archive_read_open_FILE(struct srcml_archive* archive, FILE* srcml_file);
libsrcml.srcml_archive_read_open_FILE.restype = c_int
libsrcml.srcml_archive_read_open_FILE.argtypes = [c_void_p, c_void_p]

# int srcml_archive_read_open_fd(struct srcml_archive* archive, int srcml_fd);
libsrcml.srcml_archive_read_open_fd.restype = c_int
libsrcml.srcml_archive_read_open_fd.argtypes = [c_void_p, c_int]

# int srcml_archive_read_open_io(struct srcml_archive* archive, void * context, int (*read_callback)(void * context, char* buffer, int len), int (*close_callback)(void * context));
libsrcml.srcml_archive_read_open_io.restype = c_int
libsrcml.srcml_archive_read_open_io.argtypes = [c_void_p, c_void_p, read_callback_t, close_callback_t]

# int srcml_archive_is_solitary_unit(const struct srcml_archive* archive);
libsrcml.srcml_archive_is_solitary_unit.restype = c_int
libsrcml.srcml_archive_is_solitary_unit.argtypes = [c_void_p]

# int srcml_archive_enable_solitary_unit(struct srcml_archive* archive);
libsrcml.srcml_archive_enable_solitary_unit.restype = c_int
libsrcml.srcml_archive_enable_solitary_unit.argtypes = [c_void_p]

# int srcml_archive_disable_solitary_unit(struct srcml_archive* archive);
libsrcml.srcml_archive_disable_solitary_unit.restype = c_int
libsrcml.srcml_archive_disable_solitary_unit.argtypes = [c_void_p]

# int srcml_archive_has_hash(const struct srcml_archive* archive);
libsrcml.srcml_archive_has_hash.restype = c_int
libsrcml.srcml_archive_has_hash.argtypes = [c_void_p]

# int srcml_archive_enable_hash(struct srcml_archive* archive);
libsrcml.srcml_archive_enable_hash.restype = c_int
libsrcml.srcml_archive_enable_hash.argtypes = [c_void_p]

# int srcml_archive_disable_hash(struct srcml_archive* archive);
libsrcml.srcml_archive_disable_hash.restype = c_int
libsrcml.srcml_archive_disable_hash.argtypes = [c_void_p]

# int srcml_archive_set_xml_encoding(struct srcml_archive* archive, const char* encoding);
libsrcml.srcml_archive_set_xml_encoding.restype = c_int
libsrcml.srcml_archive_set_xml_encoding.argtypes = [c_void_p, c_char_p]

# int srcml_archive_set_src_encoding(struct srcml_archive* archive, const char* encoding);
libsrcml.srcml_archive_set_src_encoding.restype = c_int
libsrcml.srcml_archive_set_src_encoding.argtypes = [c_void_p, c_char_p]

# int srcml_archive_set_language(struct srcml_archive* archive, const char* language);
libsrcml.srcml_archive_set_language.restype = c_int
libsrcml.srcml_archive_set_language.argtypes = [c_void_p, c_char_p]

# int srcml_archive_set_options(struct srcml_archive* archive, size_t option);
libsrcml.srcml_archive_set_options.restype = c_int
libsrcml.srcml_archive_set_options.argtypes = [c_void_p, c_size_t]

# int srcml_archive_enable_option(struct srcml_archive* archive, size_t option);
libsrcml.srcml_archive_enable_option.restype = c_int
libsrcml.srcml_archive_enable_option.argtypes = [c_void_p, c_size_t]

# int srcml_archive_disable_option(struct srcml_archive* archive, size_t option);
libsrcml.srcml_archive_disable_option.restype = c_int
libsrcml.srcml_archive_disable_option.argtypes = [c_void_p, c_size_t]

# int srcml_archive_set_tabstop(struct srcml_archive* archive, size_t tabstop);
libsrcml.srcml_archive_set_tabstop.restype = c_int
libsrcml.srcml_archive_set_tabstop.argtypes = [c_void_p, c_size_t]

# int srcml_archive_register_file_extension(struct srcml_archive* archive, const char* extension, const char* language);
libsrcml.srcml_archive_register_file_extension.restype = c_int
libsrcml.srcml_archive_register_file_extension.argtypes = [c_void_p, c_char_p, c_char_p]

# int srcml_archive_register_namespace(struct srcml_archive* archive, const char* prefix, const char* uri);
libsrcml.srcml_archive_register_namespace.restype = c_int
libsrcml.srcml_archive_register_namespace.argtypes = [c_void_p, c_char_p, c_char_p]

# int srcml_archive_set_processing_instruction(struct srcml_archive* archive, const char* target, const char* data);
libsrcml.srcml_archive_set_processing_instruction.restype = c_int
libsrcml.srcml_archive_set_processing_instruction.argtypes = [c_void_p, c_char_p, c_char_p]

# int srcml_archive_set_url(struct srcml_archive* archive, const char* url);
libsrcml.srcml_archive_set_url.restype = c_int
libsrcml.srcml_archive_set_url.argtypes = [c_void_p, c_char_p]

# int srcml_archive_set_version(struct srcml_archive* archive, const char* version);
libsrcml.srcml_archive_set_version.restype = c_int
libsrcml.srcml_archive_set_version.argtypes = [c_void_p, c_char_p]

# const char* srcml_archive_get_xml_encoding(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_xml_encoding.restype = c_char_p
libsrcml.srcml_archive_get_xml_encoding.argtypes = [c_void_p]

# const char* srcml_archive_get_src_encoding(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_src_encoding.restype = c_char_p
libsrcml.srcml_archive_get_src_encoding.argtypes = [c_void_p]

# const char* srcml_archive_get_revision(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_revision.restype = c_char_p
libsrcml.srcml_archive_get_revision.argtypes = [c_void_p]

# const char* srcml_archive_get_language(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_language.restype = c_char_p
libsrcml.srcml_archive_get_language.argtypes = [c_void_p]

# const char* srcml_archive_get_url(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_url.restype = c_char_p
libsrcml.srcml_archive_get_url.argtypes = [c_void_p]

# const char* srcml_archive_get_version(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_version.restype = c_char_p
libsrcml.srcml_archive_get_version.argtypes = [c_void_p]

# int srcml_archive_get_options(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_options.restype = c_int
libsrcml.srcml_archive_get_options.argtypes = [c_void_p]

# size_t srcml_archive_get_tabstop(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_tabstop.restype = c_size_t
libsrcml.srcml_archive_get_tabstop.argtypes = [c_void_p]

# size_t srcml_archive_get_namespace_size(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_namespace_size.restype = c_size_t
libsrcml.srcml_archive_get_namespace_size.argtypes = [c_void_p]

# const char* srcml_archive_get_namespace_prefix(const struct srcml_archive* archive, size_t pos);
libsrcml.srcml_archive_get_namespace_prefix.restype = c_char_p
libsrcml.srcml_archive_get_namespace_prefix.argtypes = [c_void_p, c_size_t]

# const char* srcml_archive_get_prefix_from_uri(const struct srcml_archive* archive, const char* namespace_uri);
libsrcml.srcml_archive_get_prefix_from_uri.restype = c_char_p
libsrcml.srcml_archive_get_prefix_from_uri.argtypes = [c_void_p, c_char_p]

# const char* srcml_archive_get_namespace_uri(const struct srcml_archive* archive, size_t pos);
libsrcml.srcml_archive_get_namespace_uri.restype = c_char_p
libsrcml.srcml_archive_get_namespace_uri.argtypes = [c_void_p, c_size_t]

# const char* srcml_archive_get_uri_from_prefix(const struct srcml_archive* archive, const char* prefix);
libsrcml.srcml_archive_get_uri_from_prefix.restype = c_char_p
libsrcml.srcml_archive_get_uri_from_prefix.argtypes = [c_void_p, c_char_p]

# const char* srcml_archive_get_processing_instruction_target(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_processing_instruction_target.restype = c_char_p
libsrcml.srcml_archive_get_processing_instruction_target.argtypes = [c_void_p]

# const char* srcml_archive_get_processing_instruction_data(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_processing_instruction_data.restype = c_char_p
libsrcml.srcml_archive_get_processing_instruction_data.argtypes = [c_void_p]

# const char* srcml_archive_check_extension(const struct srcml_archive* archive, const char* filename);
libsrcml.srcml_archive_check_extension.restype = c_char_p
libsrcml.srcml_archive_check_extension.argtypes = [c_void_p, c_char_p]

# struct srcml_unit* srcml_unit_create(struct srcml_archive* archive);
libsrcml.srcml_unit_create.restype = c_void_p
libsrcml.srcml_unit_create.argtypes = [c_void_p]

# NOT WORKING
## struct srcml_unit* srcml_archive_read_unit_header(struct srcml_archive* archive);
## libsrcml.srcml_archive_read_unit_header.restype = c_void_p
## libsrcml.srcml_archive_read_unit_header.argtypes = [c_void_p]

# struct srcml_unit* srcml_archive_read_unit(struct srcml_archive* archive);
libsrcml.srcml_archive_read_unit.restype = c_void_p
libsrcml.srcml_archive_read_unit.argtypes = [c_void_p]

# int srcml_archive_skip_unit(struct srcml_archive* archive);
libsrcml.srcml_archive_skip_unit.restype = c_int
libsrcml.srcml_archive_skip_unit.argtypes = [c_void_p]

# int srcml_append_transform_xpath(struct srcml_archive* archive, const char* xpath_string);
libsrcml.srcml_append_transform_xpath.restype = c_int
libsrcml.srcml_append_transform_xpath.argtypes = [c_void_p, c_char_p]

# int srcml_append_transform_xpath_attribute(struct srcml_archive* archive, const char* xpath_string,
#                                                             const char* prefix, const char* namespace_uri,
#                                                             const char* attr_name, const char* attr_value);
libsrcml.srcml_append_transform_xpath_attribute.restype = c_int
libsrcml.srcml_append_transform_xpath_attribute.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

# LIBSRCML_DECL int srcml_append_transform_xpath_element(struct srcml_archive* archive, const char* xpath_string,
#                                                             const char* prefix, const char* namespace_uri,
#                                                             const char* element);
libsrcml.srcml_append_transform_xpath_element.restype = c_int
libsrcml.srcml_append_transform_xpath_element.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p, c_char_p]

# int srcml_append_transform_xslt_filename(struct srcml_archive* archive, const char* xslt_filename);
libsrcml.srcml_append_transform_xslt_filename.restype = c_int
libsrcml.srcml_append_transform_xslt_filename.argtypes = [c_void_p, c_char_p]

# int srcml_append_transform_xslt_memory(struct srcml_archive* archive, const char* xslt_buffer, size_t size);
libsrcml.srcml_append_transform_xslt_memory.restype = c_int
libsrcml.srcml_append_transform_xslt_memory.argtypes = [c_void_p, c_char_p, c_size_t]

# int srcml_append_transform_xslt_FILE(struct srcml_archive* archive, FILE* xslt_file);
libsrcml.srcml_append_transform_xslt_FILE.restype = c_int
libsrcml.srcml_append_transform_xslt_FILE.argtypes = [c_void_p, c_void_p]

# int srcml_append_transform_xslt_fd(struct srcml_archive* archive, int xslt_fd);
libsrcml.srcml_append_transform_xslt_fd.restype = c_int
libsrcml.srcml_append_transform_xslt_fd.argtypes = [c_void_p, c_int]

# int srcml_append_transform_relaxng_filename(struct srcml_archive* archive, const char* relaxng_filename);
libsrcml.srcml_append_transform_relaxng_filename.restype = c_int
libsrcml.srcml_append_transform_relaxng_filename.argtypes = [c_void_p, c_char_p]

# int srcml_append_transform_relaxng_memory(struct srcml_archive* archive, const char* relaxng_buffer, size_t size);
libsrcml.srcml_append_transform_relaxng_memory.restype = c_int
libsrcml.srcml_append_transform_relaxng_memory.argtypes = [c_void_p, c_char_p, c_size_t]

# int srcml_append_transform_relaxng_FILE(struct srcml_archive* archive, FILE* relaxng_file);
libsrcml.srcml_append_transform_relaxng_FILE.restype = c_int
libsrcml.srcml_append_transform_relaxng_FILE.argtypes = [c_void_p, c_void_p]

# int srcml_append_transform_relaxng_fd(struct srcml_archive* archive, int relaxng_fd);
libsrcml.srcml_append_transform_relaxng_fd.restype = c_int
libsrcml.srcml_append_transform_relaxng_fd.argtypes = [c_void_p, c_int]

# int srcml_append_transform_param(struct srcml_archive* archive, const char* param_name, const char* param_value);
libsrcml.srcml_append_transform_param.restype = c_int
libsrcml.srcml_append_transform_param.argtypes = [c_void_p, c_char_p, c_char_p]

# int srcml_append_transform_stringparam(struct srcml_archive* archive, const char* param_name, const char* param_value);
libsrcml.srcml_append_transform_stringparam.restype = c_int
libsrcml.srcml_append_transform_stringparam.argtypes = [c_void_p, c_char_p, c_char_p]

# int srcml_unit_apply_transforms(struct srcml_archive* archive, struct srcml_unit* unit, struct srcml_transform_result** result);
libsrcml.srcml_unit_apply_transforms.restype = c_int
libsrcml.srcml_unit_apply_transforms.argtypes = [c_void_p, c_void_p, c_void_p]

# int srcml_clear_transforms(struct srcml_archive* archive);
libsrcml.srcml_clear_transforms.restype = c_int
libsrcml.srcml_clear_transforms.argtypes = [c_void_p]

# size_t srcml_archive_get_srcdiff_revision(const struct srcml_archive* archive);
libsrcml.srcml_archive_get_srcdiff_revision.restype = c_size_t
libsrcml.srcml_archive_get_srcdiff_revision.argtypes =[c_void_p]

# int srcml_archive_set_srcdiff_revision(struct srcml_archive* archive, size_t revision_number);
libsrcml.srcml_archive_set_srcdiff_revision.restype = c_int
libsrcml.srcml_archive_set_srcdiff_revision.argtypes = [c_void_p, c_size_t]

# TRANSFORM RESULT

# int srcml_transform_get_type(struct srcml_transform_result* result);
libsrcml.srcml_transform_get_type.restype = c_int
libsrcml.srcml_transform_get_type.argtypes = [c_void_p]

# int srcml_transform_get_unit_size(struct srcml_transform_result* result);
libsrcml.srcml_transform_get_unit_size.restype = c_int
libsrcml.srcml_transform_get_unit_size.argtype = [c_void_p]

# struct srcml_unit* srcml_transform_get_unit(struct srcml_transform_result* result, int index);
libsrcml.srcml_transform_get_unit.restype = c_void_p
libsrcml.srcml_transform_get_unit.argtypes = [c_void_p, c_int]

# const char* srcml_transform_get_string(struct srcml_transform_result* result);
libsrcml.srcml_transform_get_string.restype = c_char_p
libsrcml.srcml_transform_get_string.argtypes = [c_void_p]

# double srcml_transform_get_number(struct srcml_transform_result* result);
libsrcml.srcml_transform_get_number.restype = c_double
libsrcml.srcml_transform_get_number.argtypes = [c_void_p]

# int srcml_transform_get_bool(struct srcml_transform_result* result);
libsrcml.srcml_transform_get_bool.restype = c_int
libsrcml.srcml_transform_get_bool.argtypes = [c_void_p]

# UNIT

# struct srcml_unit* srcml_unit_clone(const struct srcml_unit* unit);
libsrcml.srcml_unit_clone.restype = c_void_p
libsrcml.srcml_unit_clone.argtypes = [c_void_p]

# int srcml_unit_error_number(const struct srcml_unit* unit);
libsrcml.srcml_unit_error_number.restype = c_int
libsrcml.srcml_unit_error_number.argtypes = [c_void_p]

# const char* srcml_unit_error_string(const struct srcml_unit* unit);
libsrcml.srcml_unit_error_string.restype = c_char_p
libsrcml.srcml_unit_error_string.argtypes = [c_void_p]

# void srcml_unit_free(struct srcml_unit* unit);
libsrcml.srcml_unit_free.restype = None
libsrcml.srcml_unit_free.argtypes = [c_void_p]

# int srcml_unit_set_src_encoding(struct srcml_unit* unit, const char* encoding);
libsrcml.srcml_unit_set_src_encoding.restype = c_int
libsrcml.srcml_unit_set_src_encoding.argtypes = [c_void_p, c_char_p]

# int srcml_unit_set_language(struct srcml_unit* unit, const char* language);
libsrcml.srcml_unit_set_language.restype = c_int
libsrcml.srcml_unit_set_language.argtypes = [c_void_p, c_char_p]

# int srcml_unit_set_filename(struct srcml_unit* unit, const char* filename);
libsrcml.srcml_unit_set_filename.restype = c_int
libsrcml.srcml_unit_set_filename.argtypes = [c_void_p, c_char_p]

# int srcml_unit_set_version(struct srcml_unit* unit, const char* version);
libsrcml.srcml_unit_set_version.restype = c_int
libsrcml.srcml_unit_set_version.argtypes = [c_void_p, c_char_p]

# int srcml_unit_set_timestamp(struct srcml_unit* unit, const char* timestamp);
libsrcml.srcml_unit_set_timestamp.restype = c_int
libsrcml.srcml_unit_set_timestamp.argtypes = [c_void_p, c_char_p]

# int srcml_unit_set_eol(struct srcml_unit* unit, size_t eol);
libsrcml.srcml_unit_set_eol.restype = c_int
libsrcml.srcml_unit_set_eol.argtypes = [c_void_p, c_size_t]

# const char* srcml_unit_get_src_encoding(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_src_encoding.restype = c_char_p
libsrcml.srcml_unit_get_src_encoding.argtypes = [c_void_p]

# const char* srcml_unit_get_revision(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_revision.restype = c_char_p
libsrcml.srcml_unit_get_revision.argtypes = [c_void_p]

# const char* srcml_unit_get_language(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_language.restype = c_char_p
libsrcml.srcml_unit_get_language.argtypes = [c_void_p]

# const char* srcml_unit_get_filename(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_filename.restype = c_char_p
libsrcml.srcml_unit_get_filename.argtypes = [c_void_p]

# const char* srcml_unit_get_version(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_version.restype = c_char_p
libsrcml.srcml_unit_get_version.argtypes = [c_void_p]

# const char* srcml_unit_get_timestamp(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_timestamp.restype = c_char_p
libsrcml.srcml_unit_get_timestamp.argtypes = [c_void_p]

# const char* srcml_unit_get_hash(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_hash.restype = c_char_p
libsrcml.srcml_unit_get_hash.argtypes = [c_void_p]

# int srcml_unit_get_loc(const struct srcml_unit* unit);
libsrcml.srcml_unit_get_loc.restype = c_int
libsrcml.srcml_unit_get_loc.argtypes = [c_void_p]

# size_t srcml_unit_get_eol(struct srcml_unit* unit);
libsrcml.srcml_unit_get_eol.restype = c_size_t
libsrcml.srcml_unit_get_eol.argtypes = [c_void_p]

# const char* srcml_unit_get_srcml(struct srcml_unit* unit);
libsrcml.srcml_unit_get_srcml.restype = c_char_p
libsrcml.srcml_unit_get_srcml.argtypes = [c_void_p]

# const char* srcml_unit_get_srcml_outer(struct srcml_unit* unit);
libsrcml.srcml_unit_get_srcml_outer.restype = c_char_p
libsrcml.srcml_unit_get_srcml_outer.argtypes = [c_void_p]

# const char* srcml_unit_get_srcml_inner(struct srcml_unit* unit);
libsrcml.srcml_unit_get_srcml_inner.restype = c_char_p
libsrcml.srcml_unit_get_srcml_inner.argtypes = [c_void_p]

# int srcml_unit_parse_filename(struct srcml_unit* unit, const char* src_filename);
libsrcml.srcml_unit_parse_filename.restype = c_int
libsrcml.srcml_unit_parse_filename.argtypes = [c_void_p, c_char_p]

# int srcml_unit_parse_memory(struct srcml_unit* unit, const char* src_buffer, size_t buffer_size);
libsrcml.srcml_unit_parse_memory.restype = c_int
libsrcml.srcml_unit_parse_memory.argtypes = [c_void_p, c_char_p, c_size_t]

# int srcml_unit_parse_FILE(struct srcml_unit* unit, FILE* src_file);
libsrcml.srcml_unit_parse_FILE.restype = c_int
libsrcml.srcml_unit_parse_FILE.argtypes = [c_void_p, c_void_p]

# int srcml_unit_parse_fd(struct srcml_unit* unit, int src_fd);
libsrcml.srcml_unit_parse_fd.restype = c_int
libsrcml.srcml_unit_parse_fd.argtypes = [c_void_p, c_int]

# int srcml_unit_parse_io(struct srcml_unit* unit, void * context, ssize_t (*read_callback)(void * context, void * buffer, size_t len), int (*close_callback)(void * context));
libsrcml.srcml_unit_parse_io.restype = c_int
libsrcml.srcml_unit_parse_io.argtypes = [c_void_p, c_void_p, read_callback_t, close_callback_t]

# int srcml_unit_unparse_filename(struct srcml_unit* unit, const char* src_filename);
libsrcml.srcml_unit_unparse_filename.restype = c_int
libsrcml.srcml_unit_unparse_filename.argtypes = [c_void_p, c_char_p]

# int srcml_unit_unparse_memory(struct srcml_unit* unit, char** src_buffer, size_t * src_size);
libsrcml.srcml_unit_unparse_memory.restype = c_int
libsrcml.srcml_unit_unparse_memory.argtypes = [c_void_p, c_void_p, c_void_p]

# int srcml_unit_unparse_FILE(struct srcml_unit* unit, FILE* file);
libsrcml.srcml_unit_unparse_FILE.restype = c_int
libsrcml.srcml_unit_unparse_FILE.argtypes = [c_void_p, c_void_p]

# int srcml_unit_unparse_fd(struct srcml_unit* unit, int fd);
libsrcml.srcml_unit_unparse_fd.restype = c_int
libsrcml.srcml_unit_unparse_fd.argtypes = [c_void_p, c_int]

# int srcml_unit_unparse_io(struct srcml_unit* unit, void * context, int (*write_callback)(void * context, const char* buffer, int len), int (*close_callback)(void * context));
libsrcml.srcml_unit_unparse_io.restype = c_int
libsrcml.srcml_unit_unparse_io.argtypes = [c_void_p, c_void_p, read_callback_t, close_callback_t]

# int srcml_write_start_unit(struct srcml_unit* unit);
libsrcml.srcml_write_start_unit.restype = c_int
libsrcml.srcml_write_start_unit.argtypes = [c_void_p]

# int srcml_write_end_unit(struct srcml_unit* unit);
libsrcml.srcml_write_end_unit.restype = c_int
libsrcml.srcml_write_end_unit.argtypes = [c_void_p]

# int srcml_write_start_element(struct srcml_unit* unit, const char* prefix, const char* name, const char* uri);
libsrcml.srcml_write_start_element.restype = c_int
libsrcml.srcml_write_start_element.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]

# int srcml_write_end_element(struct srcml_unit* unit);
libsrcml.srcml_write_end_element.restype = c_int
libsrcml.srcml_write_end_element.argtypes = [c_void_p]

# int srcml_write_namespace(struct srcml_unit* unit, const char* prefix, const char* uri);
libsrcml.srcml_write_namespace.restype = c_int
libsrcml.srcml_write_namespace.argtypes = [c_void_p, c_char_p, c_char_p]

# int srcml_write_attribute(struct srcml_unit* unit, const char* prefix, const char* name, const char* uri, const char* content);
libsrcml.srcml_write_attribute.restype = c_int
libsrcml.srcml_write_attribute.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p, c_char_p]

# int srcml_write_string(struct srcml_unit* unit, const char* content);
libsrcml.srcml_write_string.restype = c_int
libsrcml.srcml_write_string.argtypes = [c_void_p, c_char_p]
