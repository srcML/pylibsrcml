# ********************************************************************************************************************************************************
# @file srcml_unit.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

from .globals import libsrcml
from ctypes import c_ushort, c_int, c_size_t, c_void_p, c_char_p, pointer, CFUNCTYPE
from .exception import *

write_callback_t = CFUNCTYPE(c_int, c_void_p, c_char_p, c_size_t)
read_callback_t  = CFUNCTYPE(c_int, c_void_p, c_char_p, c_size_t)
close_callback_t = CFUNCTYPE(c_int, c_void_p)

# struct srcml_unit* srcml_unit_create(struct srcml_archive* archive);
libsrcml.srcml_unit_create.restype = c_void_p
libsrcml.srcml_unit_create.argtypes = [c_void_p]

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

class srcml_unit :

    # -------------------------------------------------------------------------------------------
    # Create a new srcml_unit tied to the srcml archive
    # Parameter: archive -> A srcml archive
    # -------------------------------------------------------------------------------------------
    def __init__(self, archive, unit = 0) :
        self.unit = unit
        if self.unit == 0 :
            self.unit = libsrcml.srcml_unit_create(archive.archive)

    # -------------------------------------------------------------------------------------------
    # Clone the setup of an existing unit
    # Parameter: unit -> A srcml unit
    # Return: The cloned unit
    # -------------------------------------------------------------------------------------------
    def clone(self) :
        return srcml_unit(self.unit, self.archive)

    # -------------------------------------------------------------------------------------------
    # Provides a code of the last error to occur for a unit
    # Parameter: unit -> A srcml_unit
    # Return: A code for the last recorded error
    # -------------------------------------------------------------------------------------------
    def error_number(self) :
        return libsrcml.srcml_unit_error_number(self.unit)

    # -------------------------------------------------------------------------------------------
    # Provides a description of the last error to occur for a unit
    # Parameter: unit -> A srcml unit
    # Return: A string describing last recorded error
    # -------------------------------------------------------------------------------------------
    def error_string(self) :
       result = libsrcml.srcml_unit_error_string(self.unit)
       if result != None :
           result = bytes.decode(result)

       return result

    # -------------------------------------------------------------------------------------------
    # Free an allocated unit
    # -------------------------------------------------------------------------------------------
    def unit_free(self) :
        check_return(libsrcml.srcml_unit_free(self.unit))

    # -------------------------------------------------------------------------------------------
    # Set the source-code encoding for the srcml unit
    # Parameter: encoding -> A source-code encoding
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_src_encoding(self, encoding) :
        if encoding != None :
            encoding = str.encode(encoding)

        check_return(libsrcml.srcml_unit_set_src_encoding(self.unit, encoding))

    # -------------------------------------------------------------------------------------------
    # Set the source-code language for the srcml unit
    # Parameter: language -> A supported source-code language
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_language(self, language) :
        if language != None :
            language = str.encode(language)

        check_return(libsrcml.srcml_unit_set_language(self.unit, language))

    # -------------------------------------------------------------------------------------------
    # Set the filename attribute for the srcml unit
    # Parameter: filename -> The name of a file
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_filename(self, filename) :
        if filename != None :
            filename = str.encode(filename)

        check_return(libsrcml.srcml_unit_set_filename(self.unit, filename))

    # -------------------------------------------------------------------------------------------
    # Set the version attribute for the srcml unit
    # Parameter: version -> A version string
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_version(self, version) :
        if version != None :
            version = str.encode(version)

        check_return(libsrcml.srcml_unit_set_version(self.unit, version))

    # -------------------------------------------------------------------------------------------
    # Set the timestamp attribute for the srcml unit
    # Parameter: timestamp -> A timestamp string
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_timestamp(self, timestamp) :
        if timestamp != None :
            timestamp = str.encode(timestamp)

        check_return(libsrcml.srcml_unit_set_timestamp(self.unit, timestamp))

    # -------------------------------------------------------------------------------------------
    # Set the type of end of line to be used for unparse
    # Parameter: eol -> The kind of eol to use for unparse
    # Return: SRCML_STATUS_OK on success
    # Return: SRCML_STATUS_INVALID_ARGUMENT
    # -------------------------------------------------------------------------------------------
    def set_eol(self, eol) :
        check_return(libsrcml.srcml_unit_set_eol(self.unit, eol))

    # -------------------------------------------------------------------------------------------
    # Return: The source-code encoding for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_src_encoding(self) :
        return bytes.decode(libsrcml.srcml_unit_get_src_encoding(self.unit))

    # -------------------------------------------------------------------------------------------
    # Return: The revision for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_revision(self) :
        result = libsrcml.srcml_unit_get_revision(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The source-code language for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_language(self) :
        result = libsrcml.srcml_unit_get_language(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The filename attribute on the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_filename(self) :
        result = libsrcml.srcml_unit_get_filename(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # The version for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_version(self) :
        result = libsrcml.srcml_unit_get_version(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The timestamp attribute on the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_timestamp(self) :
        result = libsrcml.srcml_unit_get_timestamp(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The hash attribute on the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_hash(self) :
        result = libsrcml.srcml_unit_get_hash(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Return: The loc of the source code in the unit, or -1 on failure
    # -------------------------------------------------------------------------------------------
    def get_loc(self) :
        check_return(libsrcml.srcml_unit_get_loc(self.unit))

    # -------------------------------------------------------------------------------------------
    # Return: The eol for to-src output (unparse), or NULL
    # -------------------------------------------------------------------------------------------
    def get_eol(self) :
        check_return(libsrcml.srcml_unit_get_eol(self.unit))

    # -------------------------------------------------------------------------------------------
    # Get a complete, valid XML of the srcML from this unit
    # The XML returned is a complete solo srcML unit
    # Note: Do not free
    # Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
    # Return: The standalone unit srcML on success and NULL on failure.
    # -------------------------------------------------------------------------------------------
    def get_srcml(self) :
        result = libsrcml.srcml_unit_get_srcml(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Get a fragment of the srcML from this unit
    # The XML returned is UTF-8 encoded XML. It is not well-formed XML, e.g., it is missing
    # the archive namespace declarations
    # Note: Do not free
    # Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
    # Return: The fragment unit srcML on success and NULL on failure.
    # -------------------------------------------------------------------------------------------
    def get_srcml_outer(self) :
        result = libsrcml.srcml_unit_get_srcml_outer(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Get the srcML without the enclosing unit tags
    # The XML fragment returned is UTF-8 encoded XML. It is not well-formed XML, e.g., it is missing
    # the archive namespace declarations and may not have a single root.
    # Note: Do not free
    # Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
    # Return: The fragment unit srcML on success and NULL on failure.
    # -------------------------------------------------------------------------------------------
    def get_srcml_inner(self) :
        result = libsrcml.srcml_unit_get_srcml_inner(self.unit)
        if result != None :
           result = bytes.decode(result)

        return result

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the file with the name src_filename to srcML and store in the unit
    # Parameter: src_filename -> Name of a file to parse into srcML
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def parse_filename(self, src_filename) :
        if src_filename != None :
            src_filename = str.encode(src_filename)

        check_return(libsrcml.srcml_unit_parse_filename(self.unit, src_filename))

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the src_buffer to srcML and store in the unit
    # Parameter: src_buffer -> Buffer containing source code to parse into srcML
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def parse_memory(self, src_buffer) :
        length = len(src_buffer)
        if src_buffer != None :
            src_buffer = str.encode(src_buffer)

        check_return(libsrcml.srcml_unit_parse_memory(self.unit, src_buffer, length))

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the source-code FILE* to srcML and store in the unit
    # Parameter: src_file -> A FILE* opened for reading
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def parse_FILE(self, src_file) :
        check_return(libsrcml.srcml_unit_parse_FILE(self.unit, src_file))

    # -------------------------------------------------------------------------------------------
    # Convert the contents of a file descriptor and stored in the unit
    # Parameter: unit -> A srcml_unit to parse the results to
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def parse_fd(self, src_fd) :
        check_return(libsrcml.srcml_unit_parse_fd(self.unit, src_fd))

    # -------------------------------------------------------------------------------------------
    # Convert to srcML the contents from the opened context accessed via read and close callbacks and place it into a unit
    # Return: context -> an io context
    # Return: read_callback -> a read callback function
    # Return: close_callback -> a close callback function
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def parse_io(self, context, read_callback, close_callback) :
        check_return(libsrcml.srcml_unit_parse_io(self.unit, context, read_callback, close_callback))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and place it into a filename
    # If the srcML was not read in, but the attributes were, the XML is read in and that value is unparsed
    # Parameter: src_filename -> Name of a file to output contents of unit as source
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def unparse_filename(self, src_filename) :
        if src_filename != None :
            src_filename = str.encode(src_filename)

        check_return(libsrcml.srcml_unit_unparse_filename(self.unit, src_filename))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and place it into a buffer
    # The buffer is allocated in the function and needs to be freed after using.
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def unparse_memory(self) :
        self.src_size = c_size_t()
        self.src_buffer = c_char_p()
        check_return(libsrcml.srcml_unit_unparse_memory(self.unit, pointer(self.src_buffer), pointer(self.src_size)))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and output to the FILE*
    # Parameter: file -> FILE* opened for writing to output the source file
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def unparse_FILE(self, file) :
        check_return(libsrcml.srcml_unit_unparse_FILE(self.unit, file))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and output to the file descriptor
    # Parameter: fd File descriptor opened for writing to output the source file
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def unparse_fd(self, fd) :
        check_return(libsrcml.srcml_unit_unparse_fd(self.unit, fd))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and output using write callbacks
    # Parameter: context -> an io context
    # Parameter: write_callback -> a write callback function
    # Parameter: close_callback -> a close callback function
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def unparse_io(self, context, write_callback, close_callback) :
        check_return(libsrcml.srcml_unit_unparse_io(self.unit, context, write_callback, close_callback))

    # -------------------------------------------------------------------------------------------
    # Write a start tag for a unit
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_start_unit(self) :
        check_return(libsrcml.srcml_write_start_unit(self.unit))

    # -------------------------------------------------------------------------------------------
    # Write an end tag for a unit
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_end_unit(self) :
        check_return(libsrcml.srcml_write_end_unit(self.unit))

    # -------------------------------------------------------------------------------------------
    # Write a start tag for a general element
    # Parameter: prefix -> Element prefix
    # Parameter: name -> Element name
    # Parameter: uri -> URI of the prefix
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_start_element(self, prefix, name, uri) :
        if prefix != None :
            prefix = str.encode(prefix)
        if name != None :
            name = str.encode(name)
        if uri != None :
            uri = str.encode(uri)

        check_return(libsrcml.srcml_write_start_element(self.unit, prefix, name, uri))

    # -------------------------------------------------------------------------------------------
    # Write an end tag for a general element
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_end_element(self) :
        check_return(libsrcml.srcml_write_end_element(self.unit))

    # -------------------------------------------------------------------------------------------
    # Write a namespace
    # Parameter: prefix -> Namespace prefix
    # Parameter: uri -> Namespace URI
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_namespace(self, prefix, uri) :
        if prefix != None :
            prefix = str.encode(prefix)
        if uri != None :
            uri = str.encode(uri)

        check_return(libsrcml.srcml_write_namespace(self.unit, prefix, uri))

    # -------------------------------------------------------------------------------------------
    # Write an attribute
    # Parameter: prefix -> Element prefix
    # Parameter: name -> Element name
    # Parameter: uri -> URI of the prefix
    # Parameter: content -> Value of the attribute
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_attribute(self, prefix, name, uri, content) :
        if prefix != None :
            prefix = str.encode(prefix)
        if name != None :
            name = str.encode(name)
        if uri != None :
            uri = str.encode(uri)
        if content != None :
            content = str.encode(content)

        check_return(libsrcml.srcml_write_attribute(self.unit, prefix, name, uri, content))

    # -------------------------------------------------------------------------------------------
    # Write a general string
    # Parameter: content -> Null-terminated string to write
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    def write_string(self, content) :
        if content != None :
            content = str.encode(content)

        check_return(libsrcml.srcml_write_string(self.unit, content))

    # -------------------------------------------------------------------------------------------
    # Return: the buffer of the srcml unit
    # -------------------------------------------------------------------------------------------
    def src(self) :
        result = self.src_buffer.value
        if result != None :
            result = bytes.decode(self.src_buffer.value)

        return result

    # -------------------------------------------------------------------------------------------
    # Free an allocated unit
    # -------------------------------------------------------------------------------------------
    def __del__(self) :
        libsrcml.srcml_unit_free(self.unit)
