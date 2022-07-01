##
# @file srcml_archive.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# The srcML Toolkit is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# The srcML Toolkit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with the srcML Toolkit; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#

from pylibsrcml.globals import libsrcml
from ctypes import c_ushort, c_int, c_double, c_size_t, c_void_p, c_char_p, pointer, c_ulonglong, CFUNCTYPE
import ctypes

from pylibsrcml.srcml_unit import srcml_unit
from pylibsrcml.exception import *

write_callback_t = CFUNCTYPE(c_int, c_void_p, c_char_p, c_size_t)
read_callback_t  = CFUNCTYPE(c_int, c_char_p, c_size_t)
close_callback_t = CFUNCTYPE(c_int, c_void_p)

SRCML_RESULT_NONE    = 0
SRCML_RESULT_UNITS   = 1
SRCML_RESULT_BOOLEAN = 2
SRCML_RESULT_NUMBER  = 3
SRCML_RESULT_STRING  = 4

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

# int srcml_transform_free(struct srcml_transform_result* result);
libsrcml.srcml_transform_free.restype = c_int
libsrcml.srcml_transform_free.argtypes = [c_void_p]

# int srcml_clear_transforms(struct srcml_archive* archive);
libsrcml.srcml_clear_transforms.restype = c_int
libsrcml.srcml_clear_transforms.argtypes = [c_void_p]

# Encapsulates multiple srcml units into one srcml archive
class srcml_archive :

    # -------------------------------------------------------------------------------------------
    # Create a new srcml archive (constructor)
    # -------------------------------------------------------------------------------------------
    def __init__(self, archive = 0) :
        self.archive = archive
        if self.archive == 0 :
            self.archive = libsrcml.srcml_archive_create()

    # -------------------------------------------------------------------------------------------
    # Clones the setup of the archive
    # Return: The cloned archive
    # -------------------------------------------------------------------------------------------
    def clone(self) :
        return srcml_archive(libsrcml.srcml_archive_clone(self.archive))

    # -------------------------------------------------------------------------------------------
    # Provides the code of the last error to occur for the archive
    # Return: Error code for the last recorded error
    # -------------------------------------------------------------------------------------------
    def error_number(self) :
        return libsrcml.srcml_archive_error_number(self.archive)

    # -------------------------------------------------------------------------------------------
    # Provides a description of the last error to occur for an archive
    # Return: A string describing last recorded error
    # -------------------------------------------------------------------------------------------
    def error_string(self) :
        result = libsrcml.srcml_archive_error_string(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Append the srcml unit to the srcml archive
    # Parameter: unit -> A srcml unit to output
    # Note: Can not mix with by element mode
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def write_unit(self, unit) :
        check_return(libsrcml.srcml_archive_write_unit(self.archive, unit.unit))

    # -------------------------------------------------------------------------------------------
    # Append the string to the srcml archive
    # Parameter: s -> String to write
    # Parameter: len -> Length of the string to write
    # Note: Can not mix with by element mode
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def write_string(self, s, len) :
        if s != None :
            s = str.encode(s)

        check_return(libsrcml.srcml_archive_write_string(self.archive, s, len))

    # -------------------------------------------------------------------------------------------
    # Close a srcml archive opened using archive.read_open_*() or archive.write_open_*()
    # Note: Archive can be reopened
    # -------------------------------------------------------------------------------------------
    def close(self) :
        libsrcml.srcml_archive_close(self.archive)

    # -------------------------------------------------------------------------------------------
    # Free a srcml archive that was previously allocated (destructor)
    # Note: The archive must be reallocated/re-created to use again
    # -------------------------------------------------------------------------------------------
    def __del__(self) :
        libsrcml.srcml_archive_free(self.archive)

    # -------------------------------------------------------------------------------------------
    # Translate to and from the srcML format
    # Translates from source code to srcML if the input_filename extension is for source code,
    # e.g., .c, .cpp, .java Language determined by file extension if language is not set with
    # srcml_set_language(). Translates from srcML to source code if the input_filename extension is '.xml'
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def srcML(self) :
        result = self.buffer.value
        if result != None:
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Open up a srcml archive for writing to a given output file
    # Parameter: srcml_filename -> Name of an output file
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def write_open_filename(self, srcml_filename) :
        if srcml_filename != None :
            srcml_filename = str.encode(srcml_filename)

        check_return(libsrcml.srcml_archive_write_open_filename(self.archive, srcml_filename))

    # -------------------------------------------------------------------------------------------
    # Open up a srcml archive for writing to its buffer
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def write_open_memory(self) :
        self.buffer = c_char_p()
        self.size = c_size_t()
        check_return(libsrcml.srcml_archive_write_open_memory(self.archive, pointer(self.buffer), pointer(self.size)))

    # -------------------------------------------------------------------------------------------
    # Open up a srcml archive for writing to a given FILE pointer
    # Parameter: srcml_file -> FILE opened for writing
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def write_open_FILE(self, srcml_file) :
        check_return(libsrcml.srcml_archive_write_open_FILE(self.archive, srcml_file))

    # -------------------------------------------------------------------------------------------
    # Open up a srcml archive for writing to a file descriptor
    # Parameter: srcml_fd -> Output file descriptor
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def write_open_fd(self, srcml_fd) :
        check_return(libsrcml.srcml_archive_write_open_fd(self.archive, srcml_fd))

    # -------------------------------------------------------------------------------------------
    # Open up a srcml archive for writing to an io context using writeand close callbacks
    # Parameter: context -> An io context
    # Parameter: write_callback -> A write callback function
    # Parameter: close_callback -> A close callback function
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def write_open_io(self, context, write_callback, close_callback) :
        check_return(libsrcml.srcml_archive_write_open_io(self.archive, context, write_callback, close_callback))

    # -------------------------------------------------------------------------------------------
    # Open a srcML archive for reading from a filename
    # Parameter: srcml_filename -> Name of an input file
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def read_open_filename(self, srcml_filename) :
        if srcml_filename != None :
            srcml_filename = str.encode(srcml_filename)

        check_return(libsrcml.srcml_archive_read_open_filename(self.archive, srcml_filename))

    # -------------------------------------------------------------------------------------------
    # Open a srcML archive for reading from a buffer
    # Parameter: buffer -> An input buffer
    # Return: SRCML_STATUS_OK on success
    # Return: Status error on failure
    # -------------------------------------------------------------------------------------------
    def read_open_memory(self, buffer) :
        length = len(buffer)
        if buffer != None :
            buffer = str.encode(buffer)

        check_return(libsrcml.srcml_archive_read_open_memory(self.archive, buffer, length))

    # -------------------------------------------------------------------------------------------
    # Open a srcML archive for reading from a FILE
    # Parameter: srcml_file -> A FILE opened for reading
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_IO_ERROR
    # -------------------------------------------------------------------------------------------
    def read_open_FILE(self, srcml_file) :
        check_return(libsrcml.srcml_archive_read_open_FILE(self.archive, srcml_file))

    # -------------------------------------------------------------------------------------------
    # Open a srcML archive for reading from a file descriptor
    # Parameter: srcml_fd -> A file descriptor opened for reading
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_IO_ERROR
    # -------------------------------------------------------------------------------------------
    def read_open_fd(self, srcml_fd) :
        check_return(libsrcml.srcml_archive_read_open_fd(self.archive, srcml_fd))

    # -------------------------------------------------------------------------------------------
    # Open a srcML archive for reading from the opened context, accessed via read and close callbacks
    # Parameter: context -> An io context
    # Parameter: read_callback -> A read callback function
    # Parameter: close_callback -> A close callback function
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_IO_ERROR
    # -------------------------------------------------------------------------------------------
    def read_open_io(self, context, read_callback, close_callback) :
        check_return(libsrcml.srcml_archive_read_open_io(self.archive, context, read_callback, close_callback))

    # -------------------------------------------------------------------------------------------
    # Whether the archive is a single, non-nested unit, or an archive
    # Return: 1 if is a solitary unit
    # Return: 0 if an archive that contains other units
    # -------------------------------------------------------------------------------------------
    def is_solitary_unit(self) :
        check_return(libsrcml.srcml_archive_is_solitary_unit(self.archive))

    # -------------------------------------------------------------------------------------------
    # Enable a single, solitary unit. This is only needed when each source-code file is to be
    # represented by an individual srcML file. Note that writing multiple units to this archive is an error.
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def enable_solitary_unit(self) :
        check_return(libsrcml.srcml_archive_enable_solitary_unit(self.archive))

    # -------------------------------------------------------------------------------------------
    # Disable the solitary unit. The full archive format allows for multiple units, and
    # is the default.
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def disable_solitary_unit(self) :
        check_return(libsrcml.srcml_archive_disable_solitary_unit(self.archive))

    # -------------------------------------------------------------------------------------------
    # Whether the hash attribute exists (in the case of a read), or would be added (in case of a write)
    # Return: 1 will include hash attribute
    # Return: 0 does not include the hash attribute
    # -------------------------------------------------------------------------------------------
    def has_hash(self) :
        return libsrcml.srcml_archive_has_hash(self.archive)

    # -------------------------------------------------------------------------------------------
    # Enable the hash attribute. This is the default
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def enable_hash(self) :
        check_return(libsrcml.srcml_archive_enable_hash(self.archive))

    # -------------------------------------------------------------------------------------------
    # Disable the hash attribute
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def disable_hash(self) :
        check_return(libsrcml.srcml_archive_disable_hash(self.archive))

    # -------------------------------------------------------------------------------------------
    # Set the XML encoding of the srcML archive
    # Parameter: encoding -> The encoding of the archive
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_xml_encoding(self, encoding) :
        if encoding != None :
            encoding = str.encode(encoding)

        check_return(libsrcml.srcml_archive_set_xml_encoding(self.archive, encoding))

    # -------------------------------------------------------------------------------------------
    # Set the default source encoding for the srcML archive
    # Parameter: encoding -> A source-code encoding
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_src_encoding(self, encoding) :
        if encoding != None :
            encoding = str.encode(encoding)

        check_return(libsrcml.srcml_archive_set_src_encoding(self.archive, encoding))

    # -------------------------------------------------------------------------------------------
    # Set the language of the srcML archive
    # Parameter: language -> A source-code language
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_language(self, language) :
        if language != None :
            language = str.encode(language)

        check_return(libsrcml.srcml_archive_set_language(self.archive, language))

    # -------------------------------------------------------------------------------------------
    # Set all options for processing an archive, erasing all previously set options
    # Note: Erases all previously set options
    # Parameter: option -> A set of srcml options
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_options(self, option) :
        check_return(libsrcml.srcml_archive_set_options(self.archive, option))

    # -------------------------------------------------------------------------------------------
    # Enable/set an option or options on an archive
    # Parameter: option -> An option, or multiple options by |ing each, to set on the archive
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def enable_option(self, option) :
        check_return(libsrcml.srcml_archive_enable_option(self.archive, option))

    # -------------------------------------------------------------------------------------------
    # Remove an option or options from an archive
    # Parameter: option -> The option, or multiple options by |ing each, to clear from the archive
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def disable_option(self, option) :
        check_return(libsrcml.srcml_archive_disable_option(self.archive, option))

    # -------------------------------------------------------------------------------------------
    # Set the tabstop size for position and column calculation
    # Parameter: tabstop -> Size of a tabstop
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_tabstop(self, tabstop) :
        check_return(libsrcml.srcml_archive_set_tabstop(self.archive, tabstop))

    # -------------------------------------------------------------------------------------------
    # Set an extension to be associated with a given source-code language
    # Parameter: extension -> A file extension
    # Parameter: language -> A supported source-code language
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def register_file_extension(self, extension, language) :
        if extension != None :
            extension = str.encode(extension)
        if language != None :
            language = str.encode(language)

        check_return(libsrcml.srcml_archive_register_file_extension(self.archive, extension, language))

    # -------------------------------------------------------------------------------------------
    # Create a new namespace or change the prefix of an existing namespace
    # Parameter: prefix -> An XML namespace prefix
    # Parameter: uri -> An XML namespace uri
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def register_namespace(self, prefix, uri) :
        if prefix != None :
            prefix = str.encode(prefix)
        if uri != None :
            uri = str.encode(uri)

        check_return(libsrcml.srcml_archive_register_namespace(self.archive, prefix, uri))

    # -------------------------------------------------------------------------------------------
    # Set a processing instruction that will be output before the root element of the archive
    # Parameter: target -> The processing instruction's target
    # Parameter: data -> The processing instruction's data
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def set_processing_instruction(self, target, data) :
        if target != None :
            target = str.encode(target)
        if data != None :
            data = str.encode(data)

        check_
        return(libsrcml.srcml_archive_set_processing_instruction(self.archive, target, data))

    # -------------------------------------------------------------------------------------------
    # Set the root URL attribute of the srcML archive
    # Parameter: url -> A url path
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_url(self, url) :
        if url != None :
            url = str.encode(url)

        check_return(libsrcml.srcml_archive_set_url(self.archive, url))

    # -------------------------------------------------------------------------------------------
    # Set the root version attribute of the srcML archive
    # Parameter: version -> A version string
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_version(self, version) :
        if version != None :
            version = str.encode(version)

        check_return(libsrcml.srcml_archive_set_version(self.archive, version))

    # -------------------------------------------------------------------------------------------
    # Return: The currently default XML encoding, or NULL
    # -------------------------------------------------------------------------------------------
    def get_xml_encoding(self) :
        result = libsrcml.srcml_archive_get_xml_encoding(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The currently default source encoding, or NULL
    # -------------------------------------------------------------------------------------------
    def get_src_encoding(self) :
        result = libsrcml.srcml_archive_get_src_encoding(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The currently set revision, or NULL
    # -------------------------------------------------------------------------------------------
    def get_revision(self) :
        result = libsrcml.srcml_archive_get_revision(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The currently set language, or NULL
    # -------------------------------------------------------------------------------------------
    def get_language(self) :
        result = libsrcml.srcml_archive_get_language(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The currently set root url attribute, or NULL
    # -------------------------------------------------------------------------------------------
    def get_url(self) :
        result = libsrcml.srcml_archive_get_url(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The currently set root version attribute, or NULL
    # -------------------------------------------------------------------------------------------
    def get_version(self) :
        result = libsrcml.srcml_archive_get_version(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The currently set options
    # -------------------------------------------------------------------------------------------
    def get_options(self) :
        return libsrcml.srcml_archive_get_options(self.archive)

    # -------------------------------------------------------------------------------------------
    # Return: The currently set tabstop size
    # -------------------------------------------------------------------------------------------
    def get_tabstop(self) :
        return libsrcml.srcml_archive_get_tabstop(self.archive)

    # -------------------------------------------------------------------------------------------
    # Return: The number of currently defined namespaces or 0 if archive is NULL
    # -------------------------------------------------------------------------------------------
    def get_namespace_size(self) :
        return libsrcml.srcml_archive_get_namespace_size(self.archive)

    # -------------------------------------------------------------------------------------------
    # Parameter: pos -> The namespace position
    # Return: The prefix for the given position, or NULL
    # -------------------------------------------------------------------------------------------
    def get_namespace_prefix(self, pos) :
        result = libsrcml.srcml_archive_get_namespace_prefix(self.archive, pos)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Parameter: namespace_uri -> An XML namespace URI
    # Return: The registered prefix for the given namespace, or NULL
    # -------------------------------------------------------------------------------------------
    def get_prefix_from_uri(self, namespace_uri) :
        if namespace_uri != None :
            namespace_uri = str.encode(namespace_uri)

        result = libsrcml.srcml_archive_get_prefix_from_uri(self.archive, namespace_uri)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Parameter: pos -> The namespace position
    # Return: The namespace at the given position, or NULL
    # -------------------------------------------------------------------------------------------
    def get_namespace_uri(self, pos) :
        result = libsrcml.srcml_archive_get_namespace_uri(self.archive, pos)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Parameter: prefix -> An XML prefix
    # Return: The first namespace for the given prefix on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_uri_from_prefix(self, prefix) :
        if prefix != None :
            prefix = str.encode(prefix)

        result = libsrcml.srcml_archive_get_uri_from_prefix(self.archive, prefix)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The processing instruction target
    # -------------------------------------------------------------------------------------------
    def get_processing_instruction_target(self) :
        result = libsrcml.srcml_archive_get_processing_instruction_target(self.archive)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The processing instruction data
    # -------------------------------------------------------------------------------------------
    def get_processing_instruction_data(self) :
        result = libsrcml.srcml_archive_get_processing_instruction_data(self.data)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Retrieve the currently registered language for a file extension
    # Parameter: filename -> Name of a file. Given the full filename, the extension is extracted
    # Return: The language for extension, or if 0 if no language.
    # -------------------------------------------------------------------------------------------
    def check_extension(self, filename) :
        if filename != None :
            filename = str.encode(filename)

        result = libsrcml.srcml_archive_check_extension(self.archive, filename)
        if result != None :
            result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Read the next unit header from the archive
    # Return: The read srcml_unit, with header information only, on success
    # Return: NULL on failure
    # -------------------------------------------------------------------------------------------
    def read_unit_header(self) :
        unit = libsrcml.srcml_archive_read_unit_header(self.archive)

        if unit != None :
            return srcml_unit(0, unit)
        return None

    # -------------------------------------------------------------------------------------------
    # Read the next unit from the archive
    # Return: The read srcml_unit on success
    # Return: NULL on failure
    # -------------------------------------------------------------------------------------------
    def read_unit(self) :
        unit = libsrcml.srcml_archive_read_unit(self.archive)
        if unit is None :
            return None
        return srcml_unit(self, unit)

    # -------------------------------------------------------------------------------------------
    # Skip the next unit from the archive
    # Return: 1 if successfully skipped
    # Return: NULL on failure
    # -------------------------------------------------------------------------------------------
    def skip_unit(self) :
        check_return(libsrcml.srcml_archive_skip_unit(self.archive))

    # -------------------------------------------------------------------------------------------
    # Append the XPath expression to the list of transformations/queries
    # Note: Currently, there is no way to specify context to the expression.
    # Parameter: xpath_string -> An XPath expression
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xpath(self, xpath_string) :
        if xpath_string != None :
            xpath_string = str.encode(xpath_string)

        check_return(libsrcml.srcml_append_transform_xpath(self.archive, xpath_string))

    # -------------------------------------------------------------------------------------------
    # Append the XPath expression to the list of transformations/queries.
    # Instead of outputting the results in a separate unit tag, output the complete
    # archive marking the XPath results with a user provided attribute
    # Parameter: xpath_string -> An XPath expression
    # Parameter: prefix -> Attribute prefix
    # Parameter: namespace_uri -> Attribute namespace
    # Parameter: attr_name -> Attribute name
    # Parameter: attr_value -> Attribute value
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xpath_attribute(self, xpath_string, prefix, namespace_uri, attr_name, attr_value) :
        if xpath_string != None :
            xpath_string = str.encode(xpath_string)
        if prefix != None :
            prefix = str.encode(prefix)
        if namespace_uri != None :
            namespace_uri = str.encode(namespace_uri)
        if attr_name != None :
            attr_name = str.encode(attr_name)
        if attr_value != None :
            attr_value = str.encode(attr_value)

        check_return(libsrcml.srcml_append_transform_xpath_attribute(self.archive, xpath_string, prefix, namespace_uri, attr_name, attr_value))

    # -------------------------------------------------------------------------------------------
    # Append the XPath expression to the list of transformations/queries.
    # Instead of outputting the results in a separate unit tag, output the complete
    # archive marking the XPath results with a user provided element
    # Parameter: xpath_string -> An XPath expression
    # Parameter: prefix -> Element prefix
    # Parameter: namespace_uri -> Element namespace
    # Parameter: element -> Element name
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xpath_element(self, xpath_string, prefix, namespace_uri, element) :
        if xpath_string != None :
            xpath_string = str.encode(xpath_string)
        if prefix != None :
            prefix = str.encode(prefix)
        if namespace_uri != None :
            namespace_uri = str.encode(namespace_uri)
        if element != None :
            element = str.encode(element)

        check_return(libsrcml.srcml_append_transform_xpath_element(self.archive, xpath_string, prefix, namespace_uri, element))

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program at the designated filename path to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_filename -> An XSLT program filename path
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_filename(self, xslt_filename) :
        if xslt_filename != None :
            xslt_filename = str.encode(xslt_filename)

        check_return(libsrcml.srcml_append_transform_xslt_filename(self.archive, xslt_filename))

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program from a buffer to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_buffer -> A buffer holding an XSLT
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_memory(self, xslt_buffer) :
        length = len(xslt_buffer)
        if xslt_buffer != None :
            xslt_buffer = str.encode(xslt_buffer)

        check_return(libsrcml.srcml_append_transform_xslt_memory(self.archive, xslt_buffer, length))

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program in a FILE to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_file -> A FILE containing an XSLT program
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_FILE(self, xslt_file) :
        check_return(libsrcml.srcml_append_transform_xslt_FILE(self.archive, xslt_file))

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program from a file descriptor to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_fd -> A file descriptor containing an XSLT program
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_fd(self, xslt_fd) :
        check_return(libsrcml.srcml_append_transform_xslt_fd(self.archive, xslt_fd))

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema from a filename path to the list of transformations/queries
    # Parameter: relaxng_filename -> A RelaxNG schema filename path
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_filename(self, relaxng_filename) :
        if relaxng_filename != None :
            relaxng_filename = str.encode(relaxng_filename)

        check_return(libsrcml.srcml_append_transform_relaxng_filename(self.archive, relaxng_filename))

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema in the buffer to the list of transformations/queries
    # Parameter: relaxng_buffer -> A buffer holding a RelaxNG schema
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_memory(self, relaxng_buffer) :
        length = len(relaxng_buffer)
        if relaxng_buffer != None :
            relaxng_buffer = str.encode(relaxng_buffer)

        check_return(libsrcml.srcml_append_transform_relaxng_memory(self.archive, relaxng_buffer, length))

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema in a FILE to the list of transformations/queries
    # Parameter: relaxng_file -> A FILE containing a RelaxNG schema
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_FILE(self, relaxng_file) :
        check_return(libsrcml.srcml_append_transform_relaxng_FILE(self.archive, relaxng_file))

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema in a file descriptor to the list of transformations/queries
    # Parameter: relaxng_fd -> A file descriptor containing a RelaxNG schema
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_fd(self, relaxng_fd) :
        check_return(libsrcml.srcml_append_transform_relaxng_fd(self.archive, relaxng_fd))

    # -------------------------------------------------------------------------------------------
    # Append an XSLT parameter to the last transformation
    # Parameter: param_name -> Name of a parameter
    # Parameter: param_value -> Value of the parameter
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_param(self, param_name, param_value) :
        if param_name != None :
            param_name = str.encode(param_name)
        if param_value != None :
            param_value = str.encode(param_value)

        check_return(libsrcml.srcml_append_transform_param(self.archive, param_name, param_value))

    # -------------------------------------------------------------------------------------------
    # Append a string XSLT parameter to the last transformation, with the value wrapped in quotes
    # Parameter: param_name -> Name of a parameter
    # Parameter: param_value -> Value of the named parameter wrapped in quotes (")
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_stringparam(self, param_name, param_value) :
        if param_name != None :
            param_name = str.encode(param_name)
        if param_value != None :
            param_value = str.encode(param_value)

        check_return(libsrcml.srcml_append_transform_stringparam(self.archive, param_name, param_value))

    # -------------------------------------------------------------------------------------------
    # Apply appended transformations from the archive to the unit consecutively in order. If parameter result is NULL,
    # result replaces the unit that the transformation was performed on. If parameter result is not NULL, results
    # are places in the proper field of the result, with the result_type parameter indicating which is appropriate.
    # If the result of the transformation is not a single unit, and the parameter result is NULL, that is considered an error.
    # Parameter: unit -> Unit to perform the transformation on
    # Parameter: results -> Optional struct of different results types
    # Return: Returns SRCML_STATUS_OK on success and a status error codes on failure.
    # -------------------------------------------------------------------------------------------
    def unit_apply_transforms(self, unit, result) :
        check_return(libsrcml.srcml_unit_apply_transforms(self.archive, unit, result))

    # -------------------------------------------------------------------------------------------
    # Remove all appended transformations from the archive
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def clear_transforms(self) :
        check_return(libsrcml.srcml_clear_transforms(self.archive))
