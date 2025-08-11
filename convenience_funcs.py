# SPDX-License-Identifier: GPL-3.0-only
"""
@file convenience_funcs.py

@copyright Copyright (C) 2014-2025 srcML, LLC. (www.srcML.org)

This file is part of pylibsrcml, a Python binding of libsrcml
"""

from .globals import libsrcml
from .exceptions import srcMLTypeError, check_srcml_status

def srcml(input_filename: str, output_filename: str) -> None:
    """
    Translate to and from the srcML format
    Translates from source code to srcML if the input_filename
    extension is for source code, e.g., .c, .cpp, .java Language
    determined by file extension if language is not set with
    srcml_set_language(). Translates from srcML to source code if the
    input_filename extension is '.xml'
    Parameter: input_filename -> The name of a source-code file or srcML file
    Parameter: output_filename -> The name of the output srcML file or source-code file
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(input_filename) != str:
        raise srcMLTypeError(srcml,"input_filename",input_filename)
    if type(output_filename) != str:
        raise srcMLTypeError(srcml,"output_filename",output_filename)

    archive_language = libsrcml.srcml_get_language()
    check_language = libsrcml.srcml_check_extension(input_filename.encode())

    if check_language:
        libsrcml.srcml_set_language(archive_language if archive_language else check_language)

    status = libsrcml.srcml(input_filename.encode(), output_filename.encode())
    check_srcml_status(status)

def set_src_encoding(encoding: str) -> None:
    """
    Set the source encoding for the srcML
    Parameter: encoding -> An output encoding
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(encoding) != str:
        raise srcMLTypeError(set_src_encoding,"encoding",encoding)
    status = libsrcml.srcml_set_src_encoding(encoding.encode())
    check_srcml_status(status)

def set_xml_encoding(encoding: str) -> None:
    """
    Set the xml encoding for the srcML
    Parameter: encoding -> An output encoding
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(encoding) != str:
        raise srcMLTypeError(set_xml_encoding,"encoding",encoding)
    status = libsrcml.srcml_set_xml_encoding(encoding.encode())
    check_srcml_status(status)

def set_language(language: str | None) -> None:
    """
    Set the language used to parse for the srcML
    Parameter: language -> A supported source-code language
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(language) != str and language != None:
        raise srcMLTypeError(set_language,"language",language)
    status = libsrcml.srcml_set_language(language.encode() if language != None else language)
    check_srcml_status(status)

def set_filename(filename: str) -> None:
    """
    Set the filename attribute for the srcML
    Parameter: filename -> Name of a file
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(filename) != str:
        raise srcMLTypeError(set_filename,"filename",filename)
    status = libsrcml.srcml_set_filename(filename.encode())
    check_srcml_status(status)

def set_url(url: str) -> None:
    """
    Set the url attribute for the srcML
    Note: The url is not checked for validity
    Parameter: url -> A url path
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(url) != str:
        raise srcMLTypeError(set_url,"url",url)
    status = libsrcml.srcml_set_url(url.encode())
    check_srcml_status(status)

def set_version(version: str) -> None:
    """
    Set the version attribute for the srcML
    Note: The version value is user-defined, and can be any value
    Parameter: version -> A version
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(version) != str:
        raise srcMLTypeError(set_version,"version",version)
    status = libsrcml.srcml_set_version(version.encode())
    check_srcml_status(status)

def set_timestamp(timestamp: str) -> None:
    """
    Set the timestamp attribute for the srcML
    Parameter: timestamp -> A timestamp string in any format
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(timestamp) != str:
        raise srcMLTypeError(set_timestamp,"timestamp",timestamp)
    status = libsrcml.srcml_set_timestamp(timestamp.encode())
    check_srcml_status(status)

def set_options(option: int) -> None:
    """
    Set options on the srcML, clearing all previously set options
    Parameter: option -> A srcML option
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(option) != int:
        raise srcMLTypeError(set_options,"option",option)
    status = libsrcml.srcml_set_options(option)
    check_srcml_status(status)

def enable_option(option: int) -> None:
    """
    Enable (set) a specific option on the srcML
    Parameter: option -> The srcML option(s)
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(option) != int:
        raise srcMLTypeError(enable_option,"option",option)
    status = libsrcml.srcml_enable_option(option)
    check_srcml_status(status)

def disable_option(option: int) -> None:
    """
    Disable (unset) a specific option on the srcML
    Parameter: option -> The srcML option(s)
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(option) != int:
        raise srcMLTypeError(disable_option,"option",option)
    status = libsrcml.srcml_disable_option(option)
    check_srcml_status(status)

def set_tabstop(tabstop: int) -> None:
    """
    Set the size of the tabstop on the srcML
    Parameter: tabstop -> Tabstop size
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(tabstop) != int:
        raise srcMLTypeError(set_tabstop,"tabstop",tabstop)
    status = libsrcml.srcml_set_tabstop(tabstop)
    check_srcml_status(status)

def register_file_extension(extension: str, language: str) -> None:
    """
    Associate an extension with a supported source-code language on the srcML
    Parameter: extension -> A source file extension
    Parameter: language -> A supported source code language
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(extension) != str:
        raise srcMLTypeError(register_file_extension,"extension",extension)
    if type(language) != str:
        raise srcMLTypeError(register_file_extension,"language",language)
    status = libsrcml.srcml_register_file_extension(extension.encode(),language.encode())
    check_srcml_status(status)

def register_namespace(prefix: str, ns: str) -> None:
    """
    Add a new namespace or change the prefix of an existing namespace on the srcML
    Parameter: prefix -> An XML namespace prefix
    Parameter: ns -> An XML namespace
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(prefix) != str:
        raise srcMLTypeError(register_namespace,"prefix",prefix)
    if type(ns) != str:
        raise srcMLTypeError(register_namespace,"ns",ns)
    status = libsrcml.srcml_register_namespace(prefix.encode(),ns.encode())
    check_srcml_status(status)

def set_processing_instruction(target: str, data: str) -> None:
    """
    Set a processing instruction that will be output before the root element of an archive
    Parameter: target -> The processing instruction's target
    Parameter: data -> The processing instruciton's data
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(extension) != str:
        raise srcMLTypeError(set_processing_instruction,"target",target)
    if type(language) != str:
        raise srcMLTypeError(set_processing_instruction,"data",data)
    status = libsrcml.srcml_set_processing_instruction(target.encode(),data.encode())
    check_srcml_status(status)

def set_eol(eol: int) -> None:
    """
    Set the end of line characters to be used for unparse
    Parameter: eol -> The kind of eol to use for unparse
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(eol) != int:
        raise srcMLTypeError(set_eol,"eol",eol)
    status = libsrcml.srcml_set_eol(eol)
    check_srcml_status(status)

def set_srcdiff_revision(revision_number: int) -> None:
    """
    Set what revision in a srcDiff document to operate with
    Parameter: revision_number -> The revision to operate with
    Return: SRCML_STATUS_OK on success
    Return: Status error code on failure
    """
    if type(revision_number) != int:
        raise srcMLTypeError(set_srcdiff_revision,"revision_number",revision_number)
    status = libsrcml.srcml_set_srcdiff_revision(revision_number)
    check_srcml_status(status)

def get_src_encoding() -> str | None:
    """
    Return: The source encoding on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_src_encoding()
    return result.decode() if result else None

def get_xml_encoding() -> str:
    """
    Return: The XML encoding on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_xml_encoding()
    return result.decode() if result else None

def get_revision() -> str:
    """
    Return: The srcML revision attribute on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_revision()
    return result.decode() if result else None

def get_language() -> str:
    """
    Return: The language attribute on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_language()
    return result.decode() if result else None

def get_filename() -> str:
    """
    Return: The filename attribute on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_filename()
    return result.decode() if result else None

def get_url() -> str:
    """
    Return: The url attribute for the root unit on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_url()
    return result.decode() if result else None

def get_version() -> str:
    """
    Return: The version attribute on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_version()
    return result.decode() if result else None

def get_timestamp() -> str:
    """
    Return: The timestamp attribute on success
    Return: NULL on failure
    """
    result = libsrcml.srcml_get_timestamp()
    return result.decode() if result else None

def get_hash() -> str:
    """
    Return: The loc of the source code on success
    Return: -1 on failure
    """
    result = libsrcml.srcml_get_hash()
    return result.decode() if result else None

def get_loc() -> int:
    """
    Return: The eol for to-src output (unparse)
    Return: NULL on failure
    """
    return libsrcml.srcml_get_loc()

def get_eol() -> int:
    """
    Return: The currently set options on success
    Return: NULL on failure
    """
    return libsrcml.srcml_get_eol()

def get_srcdiff_revision() -> int:
    """
    Return: The srcdiff revision number that is being used for processing
    Return: NULL on failure
    """
    return libsrcml.srcml_get_srcdiff_revision()

def get_options() -> int:
    """
    Return: The currently set options on success
    Return: NULL on failure
    """
    return libsrcml.srcml_get_options()

def get_tabstop() -> int:
    """
    Return: The tabstop size on success
    Return: NULL on failure
    """
    return libsrcml.srcml_get_tabstop()

def get_processing_instruction_target() -> str:
    """Return: The processing instruction target"""
    result = libsrcml.srcml_get_processing_instruction_target()
    return result.decode() if result else None




def get_processing_instruction_data() -> str:
    """Return: The processing instruction data"""
    result = libsrcml.srcml_get_processing_instruction_data()
    return result.decode() if result else None

def get_namespace_size() -> int:
    """Return: Number of declared XML namespaces"""
    return libsrcml.srcml_get_namespace_size()

def get_namespace_prefix(pos: int) -> str:
    """
    Get the prefix of the namespace at that position
    Parameter: pos -> The position to get the namespace prefix at
    Return: The prefix, where empty namespace is an empty string
    Return: 0 if given an invalid position
    """
    result = libsrcml.srcml_get_namespace_prefix(pos)
    return result.decode() if result else None

def get_prefix_from_uri(namespace_uri: str) -> str:
    """
    Get the registered prefix for the given namespace
    Parameter: namespace_uri -> An XML namespace
    Return: The registered prefix for the given namespace
    Return: NULL on failure
    """
    if type(namespace_uri) != str:
        raise srcMLTypeError(get_prefix_from_uri,"namespace_uri",namespace_uri)
    result = libsrcml.srcml_get_prefix_from_uri(namespace_uri.encode())
    return result.decode() if result else None

def get_namespace_uri(pos: int) -> str:
    """
    Parameter: pos -> position in namespaces
    Return: The namespace URI at that position on succcess
    Return: NULL on failure
    """
    if type(pos) != int:
        raise srcMLTypeError(get_namespace_uri,"pos",pos)
    result = libsrcml.srcml_get_namespace_uri(pos)
    return result.decode() if result else None

def get_uri_from_prefix(prefix: str) -> str | None:
    """
    Parameter: prefix -> An XML prefix
    Return: The first namespace URI for the given prefix on success
    Return: NULL on failure
    """
    if type(prefix) != str:
        raise srcMLTypeError(get_uri_from_prefix,"prefix",prefix)
    result = libsrcml.srcml_get_uri_from_prefix(prefix.encode())
    return result.decode() if result else None

def add_attribute(uri: str, name: str, value: str) -> None:
    """
    Add the attribute to the archive
    Parameter: uri -> An XML prefix
    Parameter: name -> The attribute name
    Parameter: value -> the attribute value
    Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    """
    if type(uri) != str:
        raise srcMLTypeError(add_attribute,"uri",uri)
    if type(name) != str:
        raise srcMLTypeError(add_attribute,"name",name)
    if type(value) != str:
        raise srcMLTypeError(add_attribute,"value",value)
    status = libsrcml.srcml_add_attribute(uri.encode(), name.encode(), value.encode())
    check_srcml_status(status)

def get_attribute_size() -> int:
    """
    Number of custom attributes
    Return: The number of attributes or 0 if archive is NULL
    """
    return libsrcml.srcml_get_attribute_size()

def get_attribute_prefix(pos: int) -> str | None:
    """
    Prefix of the custom attribute at position pos
    Parameter: pos -> The attribute position
    Return: The prefix for the given position, or NULL
    """
    if type(pos) != int:
        raise srcMLTypeError(get_attribute_prefix,"pos",pos)
    result = libsrcml.srcml_get_attribute_prefix(pos)
    return result.decode() if result else None

def get_attribute_name(pos: int) -> str | None:
    """
    Name of the custom attribute at position pos
    Parameter: pos -> The attribute position
    Return: The name for the given position, or NULL
    """
    if type(pos) != int:
        raise srcMLTypeError(get_attribute_name,"pos",pos)
    result = libsrcml.srcml_get_attribute_name(pos)
    return result.decode() if result else None

def get_attribute_value(pos: int) -> str | None:
    """
    Value of the custom attribute at position pos
    Parameter: pos -> The attribute position
    Return: The value for the given position, or NULL
    """
    if type(pos) != int:
        raise srcMLTypeError(get_attribute_value,"pos",pos)
    result = libsrcml.srcml_get_attribute_value(pos)
    return result.decode() if result else None

def cleanup_globals() -> None:
    """Cleanup and free globally allocated items (usually by libxml2)"""
    libsrcml.srcml_cleanup_globals()
