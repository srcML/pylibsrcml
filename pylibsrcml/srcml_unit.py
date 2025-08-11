# SPDX-License-Identifier: GPL-3.0-only
"""
@file srcml_unit.py

@copyright Copyright (C) 2014-2025 srcML, LLC. (www.srcML.org)

This file is part of pylibsrcml, a Python binding of libsrcml
"""

from .globals import libsrcml
from .exceptions import srcMLTypeError, srcMLInvalidConstruction, check_srcml_status

from ctypes import pointer, c_char_p, c_size_t

from io import TextIOWrapper as File

class srcMLUnit:
    def __init__(self, unit_ptr: int, freeable: bool = True):
        self.c_unit = unit_ptr
        self.is_freeable = freeable

    def __str__(self):
        """
        Get a complete, valid XML of the srcML from this unit
        The XML returned is a complete solo srcML unit
        Note: Do not free
        Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
        Return: The standalone unit srcML on success and NULL on failure.
        """
        rtn = self.get_srcml()
        return rtn if rtn else ""

    def clone(self):
        """
        Clone the setup of an existing unit
        Return: The cloned unit
        """
        copy_ptr = libsrcml.srcml_unit_clone(self.c_unit)
        copy = srcMLUnit(copy_ptr)
        return copy

    def error_number(self) -> int:
        """
        Provides a code of the last error to occur for a unit
        Parameter: unit -> A srcml_unit
        Return: A code for the last recorded error
        """
        return libsrcml.srcml_unit_error_number(self.c_unit)

    def error_string(self) -> str | None:
        """
        Provides a description of the last error to occur for a unit
        Parameter: unit -> A srcml unit
        Return: A string describing last recorded error
        """
        result = libsrcml.srcml_unit_error_string(self.c_unit)
        return result.decode() if result else None

    def __del__(self) -> None:
        """
        Free an allocated unit (void srcml_unit_free(struct srcml_unit*))
        """
        #print("IN UDEL",self.c_unit)
        if self.c_unit != 0 and self.c_unit != None and self.is_freeable:
            libsrcml.srcml_unit_free(self.c_unit)
        #print("OUT UDEL")

    def set_src_encoding(self, encoding: str) -> None :
        """
        Set the source-code encoding for the srcml unit
        Parameter: encoding -> A source-code encoding
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(encoding) != str:
            raise srcMLTypeError(self.set_src_encoding,"encoding",encoding)
        status = libsrcml.srcml_unit_set_src_encoding(self.c_unit, encoding.encode())
        check_srcml_status(status)

    def set_language(self, language: str) -> None:
        """
        Set the source-code language for the srcml unit
        Parameter: language -> A supported source-code language
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(language) != str:
            raise srcMLTypeError(self.set_language,"language",language)
        status = libsrcml.srcml_unit_set_language(self.c_unit, language.encode())
        check_srcml_status(status)

    def set_filename(self, filename: str) -> None:
        """
        Set the filename attribute for the srcml unit
        Parameter: filename -> The name of a file
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(filename) != str:
            raise srcMLTypeError(self.set_filename,"filename",filename)
        status = libsrcml.srcml_unit_set_filename(self.c_unit, filename.encode())
        check_srcml_status(status)

    def set_version(self, version: str) -> None:
        """
        Set the version attribute for the srcml unit
        Parameter: version -> A version string
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(version) != str:
            raise srcMLTypeError(self.set_version,"version",version)
        status = libsrcml.srcml_unit_set_version(self.c_unit, version.encode())
        check_srcml_status(status)

    def set_timestamp(self, timestamp: str) -> None:
        """
        Set the timestamp attribute for the srcml unit
        Parameter: timestamp -> A timestamp string
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(timestamp) != str:
            raise srcMLTypeError(self.set_timestamp,"timestamp",timestamp)
        status = libsrcml.srcml_unit_set_timestamp(self.c_unit, timestamp.encode())
        check_srcml_status(status)

    def set_eol(self, eol: int) -> None:
        """
        Set the type of end of line to be used for unparse
        Parameter: eol -> The kind of eol to use for unparse
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(eol) != int:
            raise srcMLTypeError(self.set_eol,"eol",eol)
        status = libsrcml.srcml_unit_set_eol(self.c_unit, eol)
        check_srcml_status(status)

    def register_namespace(self, prefix: str, uri: str) -> None:
        """
        Create a new namespace or change the prefix of an existing namespace
        Parameter: prefix -> An XML namespace prefix
        Parameter: uri -> An XML namespace uri
        Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(prefix) != str:
            raise srcMLTypeError(self.register_namespace,"prefix",prefix)
        if type(uri) != str:
            raise srcMLTypeError(self.register_namespace,"uri",uri)
        status = libsrcml.srcml_unit_register_namespace(self.c_unit, prefix.encode(), uri.encode())
        check_srcml_status(status)

    def add_attribute(self, uri: str, name: str, value: str) -> None:
        """
        Add the attribute to the unit
        Parameter: uri -> An XML namespace uri of the attribute
        Parameter: name -> The attribute name
        Parameter: value -> the attribute value
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(uri) != str:
            raise srcMLTypeError(self.add_attribute,"uri",uri)
        if type(name) != str:
            raise srcMLTypeError(self.add_attribute,"name",name)
        if type(value) != str:
            raise srcMLTypeError(self.add_attribute,"value",value)
        status = libsrcml.srcml_unit_add_attribute(self.c_unit, uri.encode(), name.encode(), value.encode())
        check_srcml_status(status)

    def get_attribute_size() -> int:
        """
        Number of custom attributes
        Return: The number of attributes or 0 if unit is NULL
        """
        return libsrcml.srcml_archive_get_attribute_size(self.c_unit)

    def get_attribute_prefix(pos: int) -> str | None:
        """
        Prefix of the custom attribute at position pos
        Parameter: pos -> The attribute position
        Return: The prefix for the given position, or NULL
        """
        if type(pos) != int:
            raise srcMLTypeError(self.get_attribute_prefix,"pos",pos)
        result = libsrcml.srcml_unit_get_attribute_prefix(self.c_unit, pos)
        return result.decode() if result else None

    def get_attribute_name(pos: int) -> str | None:
        """
        Name of the custom attribute at position pos
        Parameter: pos -> The attribute position
        Return: The name for the given position, or NULL
        """
        if type(pos) != int:
            raise srcMLTypeError(self.get_attribute_name,"pos",pos)
        result = libsrcml.srcml_unit_get_attribute_name(self.c_unit, pos)
        return result.decode() if result else None

    def get_attribute_value(pos: int) -> str | None:
        """
        Value of the custom attribute at position pos
        Parameter: pos -> The attribute position
        Return: The value for the given position, or NULL
        """
        if type(pos) != int:
            raise srcMLTypeError(self.get_attribute_value,"pos",pos)
        result = libsrcml.srcml_unit_get_attribute_value(self.c_archive, pos)
        return result.decode() if result else None

    def get_src_encoding(self) -> str | None:
        """Return: The source-code encoding for the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_src_encoding(self.c_unit)
        return result.decode() if result else None

    def get_revision(self) -> str | None:
        """Return: The revision for the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_revision(self.c_unit)
        return result.decode() if result else None

    def get_language(self) -> str | None:
        """Return: The source-code language for the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_language(self.c_unit)
        return result.decode() if result else None

    def get_filename(self) -> str | None:
        """Return: The filename attribute on the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_filename(self.c_unit)
        return result.decode() if result else None

    def get_version(self) -> str | None:
        """The version for the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_version(self.c_unit)
        return result.decode() if result else None

    def get_timestamp(self) -> str | None:
        """Return: The timestamp attribute on the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_timestamp(self.c_unit)
        return result.decode() if result else None

    def get_hash(self) -> str | None:
        """Return: The hash attribute on the unit on success, or NULL"""
        result = libsrcml.srcml_unit_get_hash(self.c_unit)
        return result.decode() if result else None

    def get_loc(self) -> int:
        """Return: The loc of the source code in the unit, or -1 on failure"""
        return libsrcml.srcml_unit_get_loc(self.c_unit)

    def get_eol(self) -> int:
        """Return: The eol for to-src output (unparse), or NULL"""
        return libsrcml.srcml_unit_get_eol(self.c_unit)

    def get_srcml(self) -> str | None:
        """
        Get a complete, valid XML of the srcML from this unit
        The XML returned is a complete solo srcML unit
        Note: Do not free
        Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
        Return: The standalone unit srcML on success and NULL on failure.
        """
        result = libsrcml.srcml_unit_get_srcml(self.c_unit)
        return result.decode() if result else None

    def get_srcml_outer(self) -> str | None:
        """
        Get a fragment of the srcML from this unit
        The XML returned is UTF-8 encoded XML. It is not well-formed XML, e.g., it is missing
        the archive namespace declarations
        Note: Do not free
        Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
        Return: The fragment unit srcML on success and NULL on failure.
        """
        result = libsrcml.srcml_unit_get_srcml_outer(self.c_unit)
        return result.decode() if result else None

    def get_srcml_inner(self) -> str | None:
        """
        Get the srcML without the enclosing unit tags
        The XML fragment returned is UTF-8 encoded XML. It is not well-formed XML, e.g., it is missing
        the archive namespace declarations and may not have a single root.
        Note: Do not free
        Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
        Return: The fragment unit srcML on success and NULL on failure.
        """
        result = libsrcml.srcml_unit_get_srcml_inner(self.c_unit)
        return result.decode() if result else None

    def get_namespace_size(self) -> int:
        """
        Return: The number of currently defined namespaces or 0 if unit is NULL
        """
        return libsrcml.srcml_unit_get_namespace_size(self.c_unit)

    def get_namespace_prefix(self, pos: int) -> str | None:
        """
        Parameter: pos -> The namespace position
        Return: The prefix for the given position, or NULL
        """
        if type(pos) != int:
            raise srcMLTypeError(self.get_namespace_prefix,"pos",pos)
        result = libsrcml.srcml_unit_get_namespace_prefix(self.c_unit, pos)
        return result.decode() if result else None

    def get_prefix_from_uri(self, namespace_uri: str) -> str | None:
        """
        Parameter: namespace_uri -> An XML namespace URI
        Return: The registered prefix for the given namespace, or NULL
        """
        if type(namespace_uri) != str:
            raise srcMLTypeError(self.get_prefix_from_uri,"namespace_uri",namespace_uri)
        result = libsrcml.srcml_unit_get_prefix_from_uri(self.c_unit, namespace_uri.encode())
        return result.decode() if result else None

    def get_namespace_uri(self, pos: int) -> str | None:
        """
        Parameter: pos -> The namespace position
        Return: The namespace for the given position, or NULL
        """
        if type(pos) != int:
            raise srcMLTypeError(self.get_namespace_uri,"pos",pos)
        result = libsrcml.srcml_unit_get_namespace_uri(self.c_unit, pos)
        return result.decode() if result else None

    def get_uri_from_prefix(self, prefix: str) -> str | None:
        """
        Parameter: prefix -> An XML prefix
        Return: The first namespace for the given prefix on success, or NULL
        """
        if type(prefix) != str:
            raise srcMLTypeError(self.get_uri_from_prefix,"prefix",prefix)
        result = libsrcml.srcml_unit_get_uri_from_prefix(self.c_unit, prefix.encode())
        return result.decode() if result else None

    def parse_filename(self, src_filename: str) -> None :
        """
        Convert the contents of the file with the name src_filename to srcML and store in the unit
        Parameter: src_filename -> Name of a file to parse into srcML
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(src_filename) != str:
            raise srcMLTypeError(self.parse_filename,"src_filename",src_filename)

        status = libsrcml.srcml_unit_parse_filename(self.c_unit, src_filename.encode())
        check_srcml_status(status)

    def parse_memory(self, src_buffer: bytes | str) -> None :
        """
        Convert the contents of the src_buffer to srcML and store in the unit
        Parameter: src_buffer -> Buffer containing source code to parse into srcML
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(src_buffer) != bytes and type(src_buffer) != str:
            raise srcMLTypeError(self.parse_memory,"src_buffer",src_buffer)
        if type(src_buffer) == str:
            src_buffer = src_buffer.encode() if self.get_src_encoding() == None else src_buffer.encode(self.get_src_encoding())

        status = libsrcml.srcml_unit_parse_memory(self.c_unit, src_buffer, len(src_buffer))
        check_srcml_status(status)

    def parse_file(self, src_file: File) -> None:
        """
        Convert the contents of the source-code file to srcML and store in the unit
        Parameter: src_file -> A Python file opened for reading
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(src_file) != File:
            raise srcMLTypeError(self.parse_file,"src_file",src_file)
        status = libsrcml.srcml_unit_parse_fd(self.c_unit,src_file.fileno())
        check_srcml_status(status)

    def get_src(self) -> str | None:
        """
        Get the source from this unit
        None: The source is in UTF-8 encoding and does not follow the source encoding
        Note: If other encodings are needed, use srcml_unit_unparse_memory()
        Return: The source
        Return: Null on failure
        """
        result = libsrcml.srcml_unit_get_src(self.c_unit)
        return result.decode() if result else None

    def get_src_size(self) -> int:
        """
        Get the source size from this unit
        None: The size of the source is for UTF-8 encoding and does not follow the source encoding
        Note: If the size of other encodings are needed, use srcml_unit_unparse_memory()
        Return: The source size
        Return: -1 on failure
        """
        return libsrcml.srcml_unit_get_src_size(self.c_unit)

    def unparse_filename(self, src_filename: str) -> None :
        """
        Convert the srcML in a unit into source code and place it into a filename
        If the srcML was not read in, but the attributes were, the XML is read in and that value is unparsed
        Parameter: src_filename -> Name of a file to output contents of unit as source
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(src_filename) != str:
            raise srcMLTypeError(self.unparse_filename,"src_filename",src_filename)

        status = libsrcml.srcml_unit_unparse_filename(self.c_unit, src_filename.encode())
        check_srcml_status(status)

    def unparse_memory(self) -> bytes :
        """
        Convert the srcML in a unit into source code and place it into a buffer
        The buffer is allocated in the function and needs to be freed after using.
        Return: a bytes buffer containing the unit srcML data
        """
        buffer = c_char_p()
        size = c_size_t()
        status = libsrcml.srcml_unit_unparse_memory(self.c_unit, pointer(buffer), pointer(size))
        check_srcml_status(status)
        return buffer.value

    def unparse_string(self) -> str :
        """
        Convert the srcML in a unit into source code and place it into a buffer
        The buffer is allocated in the function and needs to be freed after using.
        Return: a string containing the unit srcML data
        """
        buffer = self.unparse_memory()
        return buffer.decode() if self.get_src_encoding() == None else buffer.decode(self.get_src_encoding())

    def unparse_file(self, ofile: File) -> None:
        """
        Convert the srcML in a unit into source code and output to the FILE*
        Parameter: ofile -> Python file
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(ofile) != File:
            raise srcMLTypeError(self.unparse_file,"ofile",ofile)
        status = libsrcml.srcml_unit_unparse_fd(self.c_unit, ofile.fileno())
        check_srcml_status(status)

    def write_start_unit(self) -> None:
        """
        Write a start tag for a unit
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        status = libsrcml.srcml_write_start_unit(self.c_unit)
        check_srcml_status(status)

    def write_end_unit(self) -> None:
        """
        Write an end tag for a unit
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        status = libsrcml.srcml_write_end_unit(self.c_unit)
        check_srcml_status(status)

    def write_start_element(self, prefix: str | None, name: str, uri: str | None) -> None:
        """
        Write a start tag for a general element
        Parameter: prefix -> Element prefix
        Parameter: name -> Element name
        Parameter: uri -> URI of the prefix
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(prefix) != str and prefix != None:
            raise srcMLTypeError(self.write_start_element,"prefix",prefix)
        if type(name) != str:
            raise srcMLTypeError(self.write_start_element,"name",name)
        if type(uri) != str and uri != None:
            raise srcMLTypeError(self.write_start_element,"uri",uri)

        status = libsrcml.srcml_write_start_element(self.c_unit, prefix.encode() if prefix != None else None, name.encode(), uri.encode() if uri != None else None)
        check_srcml_status(status)

    def write_end_element(self) :
        """
        Write an end tag for a general element
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        status = libsrcml.srcml_write_end_element(self.c_unit)
        check_srcml_status(status)

    def write_namespace(self, prefix: str | None, uri: str) -> None:
        """
        Write a namespace
        Parameter: prefix -> Namespace prefix
        Parameter: uri -> Namespace URI
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(prefix) != str and prefix != None:
            raise srcMLTypeError(self.write_namespace,"prefix",prefix)
        if type(uri) != str:
            raise srcMLTypeError(self.write_namespace,"uri",uri)

        status = libsrcml.srcml_write_namespace(self.c_unit, prefix.encode() if prefix != None else None, uri.encode())
        check_srcml_status(status)

    def write_attribute(self, prefix: str | None, name: str, uri: str | None, content: str) -> None :
        """
        Write an attribute
        Parameter: prefix -> Element prefix
        Parameter: name -> Element name
        Parameter: uri -> URI of the prefix
        Parameter: content -> Value of the attribute
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(prefix) != str and prefix != None:
            raise srcMLTypeError(self.write_attribute,"prefix",prefix)
        if type(name) != str:
            raise srcMLTypeError(self.write_attribute,"name",name)
        if type(uri) != str and uri != None:
            raise srcMLTypeError(self.write_attribute,"uri",uri)
        if type(content) != str:
            raise srcMLTypeError(self.write_attribute,"content",content)

        status = libsrcml.srcml_write_attribute(self.c_unit, prefix.encode() if prefix else None, name.encode(), uri.encode() if uri else None, content.encode())
        check_srcml_status(status)

    def write_string(self, content: str) -> None :
        """
        Write a general string
        Parameter: content -> Null-terminated string to write
        Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
        """
        if type(content) != str:
            raise srcMLTypeError(self.write_string,"content",content)

        status = libsrcml.srcml_write_string(self.c_unit, content.encode())
        check_srcml_status(status)
