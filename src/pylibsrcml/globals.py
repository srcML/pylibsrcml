# ********************************************************************************************************************************************************
# @file globals.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

import os
from ctypes import cdll, c_int, c_size_t, c_char_p, POINTER, c_ulonglong
from pylibsrcml.exception import *

LIBSRCML_PATH = ""
if os.path.exists('../bin/libsrcml.dylib') :
    LIBSRCML_PATH = "../bin/libsrcml.dylib"
elif os.path.exists('../bin/libsrcml.so') :
    LIBSRCML_PATH = "../bin/libsrcml.so"
elif os.path.exists('../bin/libsrcml.dll') :
    LIBSRCML_PATH = "../bin/libsrcml.dll"
elif os.path.exists('../../bin/libsrcml.dylib') :
    LIBSRCML_PATH = "../../bin/libsrcml.dylib"
elif os.path.exists('../../bin/libsrcml.so') :
    LIBSRCML_PATH = "../../bin/libsrcml.so"
elif os.path.exists('../../bin/libsrcml.dll') :
    LIBSRCML_PATH = "../../bin/libsrcml.dll"
elif os.path.exists('../bin/Release/libsrcml.dylib') :
    LIBSRCML_PATH = "../bin/Release/libsrcml.dylib"
elif os.path.exists('../bin/Release/libsrcml.so') :
    LIBSRCML_PATH = "../bin/Release/libsrcml.so"
elif os.path.exists('../bin/Release/libsrcml.dll') :
    LIBSRCML_PATH = "../bin/Release/libsrcml.dll"
elif os.path.exists('../bin/Debug/libsrcml.dylib') :
    LIBSRCML_PATH = "../bin/Debug/libsrcml.dylib"
elif os.path.exists('../bin/Debug/libsrcml.so') :
    LIBSRCML_PATH = "../bin/Debug/libsrcml.so"
elif os.path.exists('../bin/Debug/libsrcml.dll') :
    LIBSRCML_PATH = "../bin/Debug/libsrcml.dll"
elif os.path.exists("/usr/lib/libsrcml.so") :
    LIBSRCML_PATH = "/usr/lib/libsrcml.so"
elif os.path.exists("/usr/local/lib/libsrcml.dylib") :
    LIBSRCML_PATH = "/usr/local/lib/libsrcml.dylib"

libsrcml = cdll.LoadLibrary(LIBSRCML_PATH)

def printPath(p = LIBSRCML_PATH) :
    print("PATH:" + p)

# UTILITY FUNCTIONS

# int srcml_version_number();
# -------------------------------------------------------------------------------------------
# The current version of the library
# Return: Version of libsrcml as a number
# -------------------------------------------------------------------------------------------
libsrcml.srcml_version_number.restype = c_int
libsrcml.srcml_version_number.argtypes = []

def version_number() :
    return libsrcml.srcml_version_number()

# const char* srcml_version_string();
# -------------------------------------------------------------------------------------------
# The current version of the library
# Return: Version of libsrcml as a string
# -------------------------------------------------------------------------------------------
libsrcml.srcml_version_string.restype = c_char_p
libsrcml.srcml_version_string_argtypes = []

def version_string() :
    result = libsrcml.srcml_version_string()
    if result != None :
        result = bytes.decode(result)

    return result

# int srcml_check_language(const char* language);
# -------------------------------------------------------------------------------------------
# Checks if a source-code language is supported.
# Parameter: language -> The language to check support for as a string
# Return Value: pos -> The numeric representation for that language
# Return Value: 0 -> If the language is not supported
# -------------------------------------------------------------------------------------------
libsrcml.srcml_check_language.restype = c_int
libsrcml.srcml_check_language.argtypes = [c_char_p]

def check_language(language) :
    if language != None :
        language = str.encode(language)

    result = libsrcml.srcml_check_language(language)
    if result == 0 :
        return None
    return result

# const char* srcml_check_extension(const char* filename);
# -------------------------------------------------------------------------------------------
# Check the current registered language for a file extension
# Parameter: filename -> The name of a file. When a full filename is given, the extension is extracted
# Return: The language name registered with that extension on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_check_extension.restype = c_char_p
libsrcml.srcml_check_extension.argtypes = [c_char_p]

def check_extension(filename) :
    if filename != None :
        filename = str.encode(filename)

    result = libsrcml.srcml_check_extension(filename)
    if result != None :
        result = bytes.decode(result)
    return result

# size_t srcml_get_language_list_size();
# -------------------------------------------------------------------------------------------
# Gets the number of supported source-code languages
# Return: The number of source-code languages supported
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_language_list_size.restype = c_size_t
libsrcml.srcml_get_language_list_size.argtypes = []

def get_language_list_size() :
    return libsrcml.srcml_get_language_list_size()

# const char* srcml_get_language_list(size_t pos);
# -------------------------------------------------------------------------------------------
# Gets the name of the supported language at a given position
# Parameter: pos -> The position of the language in the supported language list
# Return: The name of the supported source-code language on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_language_list.restype = c_char_p
libsrcml.srcml_get_language_list.argtypes = [c_size_t]

def get_language_list(pos) :
    res = libsrcml.srcml_get_language_list(pos)
    if res != None:
        res = bytes.decode(res)
    return res

# int srcml_check_encoding(const char* encoding);
# -------------------------------------------------------------------------------------------
# Check if a particular encoding is supported for input and output
# Parameter: encoding -> The name of the encoding
# -------------------------------------------------------------------------------------------
libsrcml.srcml_check_encoding.restype = c_int
libsrcml.srcml_check_encoding.argtypes = [c_char_p]

def check_encoding(encoding) :
    if encoding != None :
        encoding = str.encode(encoding)

    res = libsrcml.srcml_check_encoding(encoding)
    if res == 0:
        return None
    return res

# int srcml_check_xslt();
# -------------------------------------------------------------------------------------------
# Check if XSLT is available
# Return Value: 1 ->  if XSLT is available
# Return Value: 0 -> if it is unavailable
# -------------------------------------------------------------------------------------------
libsrcml.srcml_check_xslt.restype = c_int
libsrcml.srcml_check_xslt.argtypes = []

def check_xslt() :
    res = libsrcml.srcml_check_xslt()
    if res == 0:
        return None
    return res

# int srcml_check_exslt();
# -------------------------------------------------------------------------------------------
# Check if EXSLT is available
# Return Value: 1 ->  if EXSLT is available
# Return Value: 0 -> if it is unavailable
# -------------------------------------------------------------------------------------------
libsrcml.srcml_check_exslt.restype = c_int
libsrcml.srcml_check_exslt.argtypes = []

def check_exslt() :
    res = libsrcml.srcml_check_exslt()
    if res == 0:
        return None
    return res

# const char* srcml_error_string();
# -------------------------------------------------------------------------------------------
# Provides a description of the last error to occur
# Return: A string describing last recorded error
# -------------------------------------------------------------------------------------------
libsrcml.srcml_error_string.restype = c_char_p
libsrcml.srcml_error_string.argtypes = []

def error_string() :
    result = libsrcml.srcml_error_string()
    if result != None :
        result = bytes.decode(result)

    return result

# void srcml_memory_free(char * buffer);
# -------------------------------------------------------------------------------------------
# Free a memory buffer allocated by functions such as srcml_archive_write_open_memory()
# Parameter: buffer -> The allocated buffer
# -------------------------------------------------------------------------------------------
libsrcml.srcml_memory_free.restype = None
libsrcml.srcml_memory_free.argtypes = [c_char_p]

def memory_free(buffer) :
    if buffer != None :
        buffer = str.encode(buffer)

    libsrcml.srcml_memory_free(buffer)



# CONVENIENCE FUNCTIONS

# int srcml(const char* input_filename, const char* output_filename);
# -------------------------------------------------------------------------------------------
# Translate to and from the srcML format
# Translates from source code to srcML if the input_filename
# extension is for source code, e.g., .c, .cpp, .java Language
# determined by file extension if language is not set with
# srcml_set_language(). Translates from srcML to source code if the
# input_filename extension is '.xml'
# Parameter: input_filename -> The name of a source-code file or srcML file
# Parameter: output_filename -> The name of the output srcML file or source-code file
# Return: SRCML_STATUS_OK on success
# Return: Status error on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml.restype = c_int
libsrcml.srcml.argtypes = [c_char_p, c_char_p]

def srcml(input_filename, output_filename) :
    check_return(libsrcml.srcml(str.encode(input_filename), str.encode(output_filename)))

# int srcml_set_src_encoding(const char* encoding);
# -------------------------------------------------------------------------------------------
# Set the source encoding for the srcML
# Parameter: encoding -> An output encoding
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_src_encoding.restype = c_char_p
libsrcml.srcml_set_src_encoding.argtypes = [c_char_p]

def set_src_encoding(encoding) :
    check_return(libsrcml.srcml_set_src_encoding(str.encode(encoding)))

# int srcml_set_xml_encoding(const char* encoding);
# -------------------------------------------------------------------------------------------
# Set the xml encoding for the srcML
# Parameter: encoding -> An output encoding
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_xml_encoding.restype = c_int
libsrcml.srcml_set_xml_encoding.argtypes = [c_char_p]

def set_xml_encoding(encoding) :
    check_return(libsrcml.srcml_set_xml_encoding(str.encode(encoding)))

# int srcml_set_language(const char* language);
# -------------------------------------------------------------------------------------------
# Set the language used to parse for the srcML
# Parameter: language -> A supported source-code language
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_language.restype = c_int
libsrcml.srcml_set_language.argtypes = [c_char_p]

def set_language(language) :
    check_return(libsrcml.srcml_set_language(str.encode(language)))

# int srcml_set_filename(const char* filename);
# -------------------------------------------------------------------------------------------
# Set the filename attribute for the srcML
# Parameter: filename -> Name of a file
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_filename.restype = c_int
libsrcml.srcml_set_filename.argtypes = [c_char_p]

def set_filename(filename) :
    check_return(libsrcml.srcml_set_filename(str.encode(filename)))

# int srcml_set_url(const char* url);
# -------------------------------------------------------------------------------------------
# Set the url attribute for the srcML
# Note: The url is not checked for validity
# Parameter: url -> A url path
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_url.restype = c_int
libsrcml.srcml_set_url.argtypes = [c_char_p]

def set_url(url) :
    check_return(libsrcml.srcml_set_url(str.encode(url)))

# int srcml_set_version(const char* version);
# -------------------------------------------------------------------------------------------
# Set the version attribute for the srcML
# Note: The version value is user-defined, and can be any value
# Parameter: version -> A version
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_version.restype = c_int
libsrcml.srcml_set_version.argtypes = [c_char_p]

def set_version(version) :
    check_return(libsrcml.srcml_set_version(str.encode(version)))

# int srcml_set_timestamp(const char* timestamp);
# -------------------------------------------------------------------------------------------
# Set the timestamp attribute for the srcML
# Parameter: timestamp -> A timestamp string in any format
# Return Value: SRCML_STATUS_OK on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_timestamp.restype = c_int
libsrcml.srcml_set_timestamp.argtypes = [c_char_p]

def set_timestamp(timestamp) :
    check_return(libsrcml.srcml_set_timestamp(str.encode(timestamp)))

# int srcml_set_options(size_t option);
# -------------------------------------------------------------------------------------------
# Set options on the srcML, clearing all previously set options
# Parameter: option -> A srcML option
# Return Value: SRCML_STATUS_OK on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_options.restype = c_int
libsrcml.srcml_set_options.argtypes = [c_size_t]

def set_options(option) :
    check_return(libsrcml.srcml_set_options(option))

# int srcml_enable_option(size_t option);
# -------------------------------------------------------------------------------------------
# Enable (set) a specific option on the srcML
# Parameter: option -> The srcML option(s)
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_enable_option.restype = c_int
libsrcml.srcml_enable_option.argtypes = [c_size_t]

def enable_option(option) :
    check_return(libsrcml.srcml_enable_option(option))

# int srcml_disable_option(size_t option);
# -------------------------------------------------------------------------------------------
# Disable (unset) a specific option on the srcML
# Parameter: option -> The srcML option(s)
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_disable_option.restype = c_int
libsrcml.srcml_disable_option.argtypes = [c_size_t]

def disable_option(option) :
    check_return(libsrcml.srcml_disable_option(option))

# int srcml_set_tabstop(size_t tabstop);
# -------------------------------------------------------------------------------------------
# Set the size of the tabstop on the srcML
# Parameter: tabstop -> Tabstop size
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_tabstop.restype = c_int
libsrcml.srcml_set_tabstop.argtypes = [c_size_t]

def set_tabstop(tabstop) :
    check_return(libsrcml.srcml_set_tabstop(tabstop))

# int srcml_register_file_extension(const char* extension, const char* language);
# -------------------------------------------------------------------------------------------
# Associate an extension with a supported source-code language on the srcML
# Parameter: extension -> A source file extension
# Parameter: language -> A supported source code language
# Return: SRCML_STATUS_OK on success
# Return: Status error code on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_register_file_extension.restype = c_int
libsrcml.srcml_register_file_extension.argtypes = [c_char_p, c_char_p]

def register_file_extension(extension, language) :
    check_return(libsrcml.srcml_register_file_extension(str.encode(extension), str.encode(language)))

# int srcml_register_namespace(const char* prefix, const char* ns);
# -------------------------------------------------------------------------------------------
# Add a new namespace or change the prefix of an existing namespace on the srcML
# Parameter: prefix -> An XML namespace prefix
# Parameter: ns -> An XML namespace
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_* -> Status error code on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_register_namespace.restype = c_int
libsrcml.srcml_register_namespace.argtypes = [c_char_p, c_char_p]

def register_namespace(prefix, ns) :
    check_return(libsrcml.srcml_register_namespace(str.encode(prefix), str.encode(ns)))

# int srcml_set_processing_instruction(const char* target, const char* data);
# -------------------------------------------------------------------------------------------
# Set a processing instruction that will be output before the root element of an archive
# Parameter: target -> The processing instruction's target
# Parameter: data -> The processing instruciton's data
# Return: SRCML_STATUS_OK on success
# Return: Status error code on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_processing_instruction.restype = c_int
libsrcml.srcml_set_processing_instruction.argtypes = [c_char_p, c_char_p]

def set_processing_instruction(target, data) :
    check_return(libsrcml.srcml_set_processing_instruction(str.encode(target), str.encode(data)))

# int srcml_set_eol(size_t eol);
# -------------------------------------------------------------------------------------------
# Set the end of line characters to be used for unparse
# Parameter: eol -> The kind of eol to use for unparse
# Return Value: SRCML_STATUS_OK -> on success
# Return Value: SRCML_STATUS_INVALID_ARGUMENT
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_eol.restype = c_int
libsrcml.srcml_set_eol.argtypes = [c_size_t]

def set_eol(eol) :
    check_return(libsrcml.srcml_set_eol(eol))

# int srcml_set_srcdiff_revision(size_t revision_number);
# -------------------------------------------------------------------------------------------
# Set what revision in a srcDiff document to operate with
# Parameter: revision_number -> The revision to operate with
# Return: SRCML_STATUS_OK on success
# Return: Status error code on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_set_srcdiff_revision.restype = c_int
libsrcml.srcml_set_srcdiff_revision.argtypes = [c_size_t]

def set_srcdiff_revision(revision_number) :
    check_return(libsrcml.srcml_set_srcdiff_revision(revision_number))

# const char* srcml_get_src_encoding();
# -------------------------------------------------------------------------------------------
# Return: The source encoding on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_src_encoding.restype = c_char_p
libsrcml.srcml_get_src_encoding.argtypes = []

def get_src_encoding() :
    result = libsrcml.srcml_get_src_encoding()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_xml_encoding();
# -------------------------------------------------------------------------------------------
# Return: The XML encoding on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_xml_encoding.restype = c_char_p
libsrcml.srcml_get_xml_encoding.argtypes = []

def get_xml_encoding() :
    result = libsrcml.srcml_get_xml_encoding()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_revision();
# -------------------------------------------------------------------------------------------
# Return: The srcML revision attribute on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_revision.restype = c_char_p
libsrcml.srcml_get_revision.argtypes = []

def get_revision() :
    result = libsrcml.srcml_get_revision()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_language();
# -------------------------------------------------------------------------------------------
# Return: The language attribute on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_language.restype = c_char_p
libsrcml.srcml_get_language.argtypes = []

def get_language() :
    result = libsrcml.srcml_get_language()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_filename();
# -------------------------------------------------------------------------------------------
# Return: The filename attribute on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_filename.restype = c_char_p
libsrcml.srcml_get_filename.argtypes = []

def get_filename() :
    result = libsrcml.srcml_get_filename()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_url();
# -------------------------------------------------------------------------------------------
# Return: The url attribute for the root unit on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_url.restype = c_char_p
libsrcml.srcml_get_url.argtypes = []

def get_url() :
    result = libsrcml.srcml_get_url()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_version();
# -------------------------------------------------------------------------------------------
# Return: The version attribute on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_version.restype = c_char_p
libsrcml.srcml_get_version.argtypes = []

def get_version() :
    result = libsrcml.srcml_get_version()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_timestamp();
# -------------------------------------------------------------------------------------------
# Return: The timestamp attribute on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_timestamp.restype = c_char_p
libsrcml.srcml_get_timestamp.argtypes = []

def get_timestamp() :
    result = libsrcml.srcml_get_timestamp()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_hash();
# -------------------------------------------------------------------------------------------
# Return: The loc of the source code on success
# Return: -1 on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_hash.restype = c_char_p
libsrcml.srcml_get_hash.argtypes = []

def get_hash() :
    result = libsrcml.srcml_get_hash()
    if result != None :
        result = bytes.decode(result)

    return result

# int srcml_get_loc();
# -------------------------------------------------------------------------------------------
# Return: The eol for to-src output (unparse)
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_loc.restype = c_int
libsrcml.srcml_get_loc.argtypes = []

def get_loc() :
    return libsrcml.srcml_get_loc()

# size_t srcml_get_eol();
# -------------------------------------------------------------------------------------------
# Return: The currently set options on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_eol.restypes = c_size_t
libsrcml.srcml_get_eol.argtypes = []

def get_eol() :
    return libsrcml.srcml_get_eol()

# int srcml_get_options();
# -------------------------------------------------------------------------------------------
# Return: The currently set options on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_options.restype = c_int
libsrcml.srcml_get_options.argtypes = []

def get_options() :
    return libsrcml.srcml_get_options()

# size_t srcml_get_tabstop();
# -------------------------------------------------------------------------------------------
# Return: The tabstop size on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_tabstop.restype = c_size_t
libsrcml.srcml_get_tabstop.argtypes = []

def get_tabstop() :
    return libsrcml.srcml_get_tabstop()

# const char* srcml_get_processing_instruction_target();
# -------------------------------------------------------------------------------------------
# Return: The processing instruction target
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_processing_instruction_target.restype = c_char_p
libsrcml.srcml_get_processing_instruction_target.argtypes = []

def get_processing_instruction_target() :
    result = libsrcml.srcml_get_processing_instruction_target()
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_processing_instruction_data();
# -------------------------------------------------------------------------------------------
# Return: The processing instruction data
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_processing_instruction_data.restype = c_char_p
libsrcml.srcml_get_processing_instruction_data.argtypes = []

def get_processing_instruction_data() :
    result = libsrcml.srcml_get_processing_instruction_data()
    if result != None :
        result = bytes.decode(result)

    return result

# size_t srcml_get_namespace_size();
# -------------------------------------------------------------------------------------------
# Return: Number of declared XML namespaces
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_namespace_size.restype = c_size_t
libsrcml.srcml_get_namespace_size.argtypes = []

def get_namespace_size() :
    return libsrcml.srcml_get_namespace_size()

# const char* srcml_get_namespace_prefix(size_t pos);
# -------------------------------------------------------------------------------------------
# Get the prefix of the namespace at that position
# Parameter: pos -> The position to get the namespace prefix at
# Return: The prefix, where empty namespace is an empty string
# Return: 0 if given an invalid position
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_namespace_prefix.restype = c_char_p
libsrcml.srcml_get_namespace_prefix.argtypes = [c_size_t]

def get_namespace_prefix(pos) :
    result = libsrcml.srcml_get_namespace_prefix(pos)
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_prefix_from_uri(const char* namespace_uri);
# -------------------------------------------------------------------------------------------
# Get the registered prefix for the given namespace
# Parameter: namespace_uri -> An XML namespace
# Return: The registered prefix for the given namespace
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_prefix_from_uri.restype = c_char_p
libsrcml.srcml_get_prefix_from_uri.argtypes = [c_char_p]

def get_prefix_from_uri(namespace_uri) :
    if(namespace_uri != None) :
        namespace_uri = str.encode(namespace_uri)

    result = libsrcml.srcml_get_prefix_from_uri(namespace_uri)
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_namespace_uri(size_t pos);
# -------------------------------------------------------------------------------------------
# Parameter: pos -> position in namespaces
# Return: The namespace URI at that position on succcess
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_namespace_uri.restype = c_char_p
libsrcml.srcml_get_namespace_uri.argtypes = [c_size_t]

def get_namespace_uri(pos) :
    result = libsrcml.srcml_get_namespace_uri(pos)
    if result != None :
        result = bytes.decode(result)

    return result

# const char* srcml_get_uri_from_prefix(const char* prefix);
# -------------------------------------------------------------------------------------------
# Parameter: prefix -> An XML prefix
# Return: The first namespace URI for the given prefix on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
libsrcml.srcml_get_uri_from_prefix.restype = c_char_p
libsrcml.srcml_get_uri_from_prefix.argtypes = [c_char_p]

def get_uri_from_prefix(prefix) :
    if(prefix != None) :
        prefix = str.encode(prefix)

    result = libsrcml.srcml_get_uri_from_prefix(prefix)
    if result != None :
        result = bytes.decode(result)

    return result

# void srcml_cleanup_globals();
# -------------------------------------------------------------------------------------------
# Cleanup and free globally allocated items (usually by libxml2)
# -------------------------------------------------------------------------------------------
libsrcml.srcml_cleanup_globals.restype = None
libsrcml.srcml_cleanup_globals.argtypes = []

def cleanup_globals() :
    libsrcml.srcml_cleanup_globals()