from .globals import libsrcml
from .exceptions import srcMLTypeError, srcDiffRevisionInvalid, check_srcml_status
from .values import srcDiffRevision, srcMLStatus
from .srcml_unit import srcMLUnit
from .srcml_transform_result import srcMLTransformResult

from io import TextIOWrapper as File
#from pathlib import Path

import os

from ctypes import pointer, c_char_p, c_size_t

class srcMLArchive:
    # -------------------------------------------------------------------------------------------
    # Create a new srcml archive (constructor)
    # ------------------------------------------------------------------------------------------- 
    def __init__(self, arch_ptr: None | int = None):
        if type(arch_ptr) != int and arch_ptr != None:
            raise srcMLTypeError(self.__init__,"arch_ptr",arch_ptr)
        self.c_archive = libsrcml.srcml_archive_create() if type(arch_ptr) != int else arch_ptr
        self.closed = False

    # -------------------------------------------------------------------------------------------
    # Free a srcml archive that was previously allocated (destructor)
    # Note: The archive must be reallocated/re-created to use again
    # -------------------------------------------------------------------------------------------
    def __del__(self) :
        #print("In",type(self), "Del",self.c_archive)
        if not self.closed:
            self.close()
        if self.c_archive != 0 and self.c_archive != None:
            libsrcml.srcml_archive_free(self.c_archive)
        #print("Done",type(self), "Del",self.c_archive)

    # -------------------------------------------------------------------------------------------
    # The enter statement for a context manager
    # Return: The archive itself, the constructor does the opening
    # -------------------------------------------------------------------------------------------
    def __enter__(self) :
        return self

    # -------------------------------------------------------------------------------------------
    # The exit statement for a context manager
    # Closes the Archive automatically.
    # -------------------------------------------------------------------------------------------
    def __exit__(self, exc_type, exc_val, exc_tb) :
        self.close()

    # -------------------------------------------------------------------------------------------
    # Provides the code of the last error to occur for the archive
    # Return: Error code for the last recorded error
    # -------------------------------------------------------------------------------------------
    def error_number(self) -> int:
        return libsrcml.srcml_archive_error_number(self.c_archive)

    # -------------------------------------------------------------------------------------------
    # Provides a description of the last error to occur for an archive
    # Return: A string describing last recorded error
    # -------------------------------------------------------------------------------------------
    def error_string(self) -> str | None:
        result = libsrcml.srcml_archive_error_string(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Close a srcml archive opened using archive.read_open_*() or archive.write_open_*()
    # -------------------------------------------------------------------------------------------
    def close(self) :
        if not self.closed:
            libsrcml.srcml_archive_close(self.c_archive)
            self.closed = True

    # -------------------------------------------------------------------------------------------
    # Whether the archive is a single, non-nested unit, or an archive
    # Return: True if is a solitary unit
    # Return: False if an archive that contains other units
    # -------------------------------------------------------------------------------------------
    def is_solitary_unit(self) -> bool:
        return bool(libsrcml.srcml_archive_is_solitary_unit(self.c_archive))

    # -------------------------------------------------------------------------------------------
    # Enable a single, solitary unit. This is only needed when each source-code file is to be
    # represented by an individual srcML file. Note that writing multiple units to this archive is an error.
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def enable_solitary_unit(self) -> None :
        status = libsrcml.srcml_archive_enable_solitary_unit(self.c_archive)
        check_srcml_status(status)
    
    # -------------------------------------------------------------------------------------------
    # Disable the solitary unit. The full archive format allows for multiple units, and
    # is the default.
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def disable_solitary_unit(self) -> None:
        status = libsrcml.srcml_archive_disable_solitary_unit(self.c_archive)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Whether the hash attribute exists (in the case of a read), or would be added (in case of a write)
    # Return: True will include hash attribute
    # Return: False does not include the hash attribute
    # -------------------------------------------------------------------------------------------
    def has_hash(self) -> bool:
        return bool(libsrcml.srcml_archive_has_hash(self.c_archive))

    # -------------------------------------------------------------------------------------------
    # Enable the hash attribute. This is the default
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def enable_hash(self) -> None :
        status = libsrcml.srcml_archive_enable_hash(self.c_archive)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Disable the hash attribute
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def disable_hash(self) -> None:
        status = libsrcml.srcml_archive_disable_hash(self.c_archive)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the XML encoding of the srcML archive
    # Parameter: encoding -> The encoding of the archive
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_xml_encoding(self, encoding: str) -> None :
        if type(encoding) != str:
            raise srcMLTypeError(self.set_xml_encoding,"encoding",encoding)
        
        status = libsrcml.srcml_archive_set_xml_encoding(self.c_archive, encoding.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the default source encoding for the srcML archive
    # Parameter: encoding -> A source-code encoding
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_src_encoding(self, encoding: str) -> None :
        if type(encoding) != str:
            raise srcMLTypeError(self.set_src_encoding,"encoding",encoding)
        
        status = libsrcml.srcml_archive_set_src_encoding(self.c_archive, encoding.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the language of the srcML archive
    # Parameter: language -> A source-code language
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_language(self, language: str) -> None :
        if type(language) != str:
            raise srcMLTypeError(self.set_language,"language",language)
        
        status = libsrcml.srcml_archive_set_language(self.c_archive, language.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set all options for processing an archive, erasing all previously set options
    # Note: Erases all previously set options
    # Parameter: option -> A set of srcml options
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_options(self, option: int) -> None :
        if type(option) != int:
            raise srcMLTypeError(self.set_options,"option",option)
        
        status = libsrcml.srcml_archive_set_options(self.c_archive, option)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Enable/set an option or options on an archive
    # Parameter: option -> An option, or multiple options by |ing each, to set on the archive
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def enable_option(self, option: int) -> None :
        if type(option) != int:
            raise srcMLTypeError(self.enable_option,"option",option)
        
        status = libsrcml.srcml_archive_enable_option(self.c_archive, option)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Remove an option or options from an archive
    # Parameter: option -> The option, or multiple options by |ing each, to clear from the archive
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def disable_option(self, option: int) -> None :
        if type(option) != int:
            raise srcMLTypeError(self.disable_option,"option",option)
        
        status = libsrcml.srcml_archive_disable_option(self.c_archive, option)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the tabstop size for position and column calculation
    # Parameter: tabstop -> Size of a tabstop
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_tabstop(self, tabstop: int) -> None :
        if type(tabstop) != int:
            raise srcMLTypeError(self.set_tabstop,"tabstop",tabstop)
        
        status = libsrcml.srcml_archive_set_tabstop(self.c_archive, tabstop)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set an extension to be associated with a given source-code language
    # Parameter: extension -> A file extension
    # Parameter: language -> A supported source-code language
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def register_file_extension(self, extension: str, language:str) -> None :
        if type(extension) != str:
            raise srcMLTypeError(self.register_file_extension,"extension",extension)
        if type(language) != str:
            raise srcMLTypeError(self.register_file_extension,"language",language)

        status = libsrcml.srcml_archive_register_file_extension(self.c_archive, extension.encode(), language.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Create a new namespace or change the prefix of an existing namespace
    # Parameter: prefix -> An XML namespace prefix
    # Parameter: uri -> An XML namespace uri
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def register_namespace(self, prefix: str, uri: str) -> None :
        if type(prefix) != str:
            raise srcMLTypeError(self.register_namespace,"prefix",prefix)
        if type(uri) != str:
            raise srcMLTypeError(self.register_namespace,"uri",uri)
        
        status = libsrcml.srcml_archive_register_namespace(self.c_archive, prefix.encode(), uri.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set a processing instruction that will be output before the root element of the archive
    # Parameter: target -> The processing instruction's target
    # Parameter: data -> The processing instruction's data
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_processing_instruction(self, target: str, data: str) -> None :
        if type(target) != str:
            raise srcMLTypeError(self.set_processing_instruction,"target",target)
        if type(data) != str:
            raise srcMLTypeError(self.set_processing_instruction,"data",data)
        
        status = libsrcml.srcml_archive_set_processing_instruction(self.c_archive, target.encode(), data.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the root URL attribute of the srcML archive
    # Parameter: url -> A url path
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_url(self, url: str) -> None :
        if type(url) != str:
            raise srcMLTypeError(self.set_url,"url",url)

        status = libsrcml.srcml_archive_set_url(self.c_archive, url.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the root version attribute of the srcML archive
    # Parameter: version -> A version string
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_version(self, version: str) -> None :
        if type(version) != str:
            raise srcMLTypeError(self.set_version,"version",version)

        status = libsrcml.srcml_archive_set_version(self.c_archive, version.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Return: The currently default XML encoding, or NULL
    # -------------------------------------------------------------------------------------------
    def get_xml_encoding(self) -> str | None:
        result = libsrcml.srcml_archive_get_xml_encoding(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The currently default source encoding, or NULL
    # -------------------------------------------------------------------------------------------
    def get_src_encoding(self) -> str | None:
        result = libsrcml.srcml_archive_get_src_encoding(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The currently set revision, or NULL
    # -------------------------------------------------------------------------------------------
    def get_revision(self) -> str | None:
        result = libsrcml.srcml_archive_get_revision(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The currently set language, or NULL
    # -------------------------------------------------------------------------------------------
    def get_language(self) -> str | None :
        result = libsrcml.srcml_archive_get_language(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The currently set root url attribute, or NULL
    # -------------------------------------------------------------------------------------------
    def get_url(self) -> str | None:
        result = libsrcml.srcml_archive_get_url(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The currently set root version attribute, or NULL
    # -------------------------------------------------------------------------------------------
    def get_version(self) -> str | None:
        result = libsrcml.srcml_archive_get_version(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The currently set options
    # -------------------------------------------------------------------------------------------
    def get_options(self) -> int:
        return libsrcml.srcml_archive_get_options(self.c_archive)

    # -------------------------------------------------------------------------------------------
    # Return: The currently set tabstop size
    # -------------------------------------------------------------------------------------------
    def get_tabstop(self) -> int:
        return libsrcml.srcml_archive_get_tabstop(self.c_archive)

    # -------------------------------------------------------------------------------------------
    # Return: The number of currently defined namespaces or 0 if archive is NULL
    # -------------------------------------------------------------------------------------------
    def get_namespace_size(self) -> int:
        return libsrcml.srcml_archive_get_namespace_size(self.c_archive)

    # -------------------------------------------------------------------------------------------
    # Parameter: pos -> The namespace position
    # Return: The prefix for the given position, or NULL
    # -------------------------------------------------------------------------------------------
    def get_namespace_prefix(self, pos: int) -> str | None:
        if type(pos) != int:
            raise srcMLTypeError(self.get_namespace_prefix,"pos",pos)
        result = libsrcml.srcml_archive_get_namespace_prefix(self.c_archive, pos)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Parameter: namespace_uri -> An XML namespace URI
    # Return: The registered prefix for the given namespace, or NULL
    # -------------------------------------------------------------------------------------------
    def get_prefix_from_uri(self, namespace_uri: str) -> str | None:
        if type(namespace_uri) != str:
            raise srcMLTypeError(self.get_prefix_from_uri,"namespace_uri",namespace_uri)
        
        result = libsrcml.srcml_archive_get_prefix_from_uri(self.c_archive, namespace_uri.encode())
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Parameter: pos -> The namespace position
    # Return: The namespace at the given position, or NULL
    # -------------------------------------------------------------------------------------------
    def get_namespace_uri(self, pos: int) -> str | None:
        if type(pos) != int:
            raise srcMLTypeError(self.get_namespace_uri,"pos",pos)
        result = libsrcml.srcml_archive_get_namespace_uri(self.c_archive, pos)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Parameter: prefix -> An XML prefix
    # Return: The first namespace for the given prefix on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_uri_from_prefix(self, prefix: str) -> str | None:
        if type(prefix) != str:
            raise srcMLTypeError(self.get_uri_from_prefix,"prefix",prefix)
        
        result = libsrcml.srcml_archive_get_uri_from_prefix(self.c_archive, prefix.encode())
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The processing instruction target
    # -------------------------------------------------------------------------------------------
    def get_processing_instruction_target(self) -> str | None:
        result = libsrcml.srcml_archive_get_processing_instruction_target(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The processing instruction data
    # -------------------------------------------------------------------------------------------
    def get_processing_instruction_data(self) -> str | None:
        result = libsrcml.srcml_archive_get_processing_instruction_data(self.c_archive)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Retrieve the currently registered language for a file extension
    # Parameter: filename -> Name of a file. Given the full filename, the extension is extracted
    # Return: The language for extension, or None if no language.
    # -------------------------------------------------------------------------------------------
    def check_extension(self, filename: str) -> str | None:
        if type(filename) != str:
            raise srcMLTypeError(self.check_extension,"filename",filename)
        
        result = libsrcml.srcml_archive_check_extension(self.c_archive, filename.encode())
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Gets the srcdiff revision number that the archive is using for processing.
    # Return: The srcdiff revision number that the archive is using for processing
    # -------------------------------------------------------------------------------------------
    def get_srcdiff_revision(self) -> int:
        rev = libsrcml.srcml_archive_get_srcdiff_revision(self.c_archive)
        #if rev == srcDiffRevision.INVALID:
        #    raise srcDiffRevisionInvalid()
        return rev

    # -------------------------------------------------------------------------------------------
    # Set what revision in a srcDiff archive to operate with
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_srcdiff_revision(self,revision_number: int) -> None:
        if type(revision_number) != int:
            raise srcMLTypeError(self.set_srcdiff_revision,"revision_number",revision_number)

        check_srcml_status(libsrcml.srcml_archive_set_srcdiff_revision(self.c_archive, revision_number))

    # -------------------------------------------------------------------------------------------
    # Create a new srcml_unit tied to the srcml archive
    # Parameter: archive -> A srcml archive
    # -------------------------------------------------------------------------------------------
    def unit_create(self):
        c_unit = libsrcml.srcml_unit_create(self.c_archive)
        return srcMLUnit(c_unit)



class srcMLArchiveRead(srcMLArchive):
    # -------------------------------------------------------------------------------------------
    # Create a new srcml archive (constructor)
    # ------------------------------------------------------------------------------------------- 
    def __init__(self, source: str, string_read_mode: ["source","filename",None] = None, *, clone_from: srcMLArchive | None = None):
        if not isinstance(clone_from,srcMLArchive) and clone_from != None:
            raise srcMLTypeError(self.__init__, "clone_from", clone_from, inheritance_flag=True)

        #self._internal_source = source # save source to try to prevent C issues

        super().__init__(None if clone_from == None else libsrcml.srcml_archive_clone(clone_from.c_archive))

        if string_read_mode != None and string_read_mode != "source" and string_read_mode != "filename":
            raise srcMLTypeError(self.__init__,"string_read_mode",string_read_mode)
        
        if type(source) != str:
            raise srcMLTypeError(self.__init__,"source",source)
        elif type(source) == str and (string_read_mode == "source" or "<" in source): # Raw XML String
            status = libsrcml.srcml_archive_read_open_memory(self.c_archive, source.encode(), len(source.encode()))
        elif type(source) == str: # Other string - check that it is a file path
            status = libsrcml.srcml_archive_read_open_filename(self.c_archive, source.encode())
        # NOTE - Disabled due to it automatically closing the file.
        # elif type(source) == File: # File
        #     status = libsrcml.srcml_archive_read_open_fd(self.c_archive,source.fileno())
        #     #source.close()
        else:
            raise ValueError("The provided source value is an incorrect format.")
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Free a srcml archive that was previously allocated (destructor)
    # Note: The archive must be reallocated/re-created to use again
    # Note: Special case for Read Archives, clearing the transforms before destruction
    # -------------------------------------------------------------------------------------------
    def __del__(self) :
        if self.c_archive != 0 and self.c_archive != None:
            self.clear_transforms()
        super().__del__()

    # -------------------------------------------------------------------------------------------
    # iter function for working with for loops
    # -------------------------------------------------------------------------------------------
    def __iter__(self):
        unit = self.read_unit()
        while unit != None:
            yield unit
            unit = self.read_unit()

    # -------------------------------------------------------------------------------------------
    # Read the next unit from the archive
    # Return: The read srcMLUnit on success
    # Return: NULL on failure
    # -------------------------------------------------------------------------------------------
    def read_unit(self) -> srcMLUnit | None:
        c_unit = libsrcml.srcml_archive_read_unit(self.c_archive)
        return srcMLUnit(c_unit) if c_unit else None

    # -------------------------------------------------------------------------------------------
    # Read the remaining units in the archive
    # Return: A list of read srcMLUnits on success
    # -------------------------------------------------------------------------------------------
    def read_all_units(self) -> list[srcMLUnit]:
        units = []
        c_unit = libsrcml.srcml_archive_read_unit(self.c_archive)
        while c_unit:
            units.append(srcMLUnit(c_unit))
            c_unit = libsrcml.srcml_archive_read_unit(self.c_archive)
        return units

    # -------------------------------------------------------------------------------------------
    # Skip the next unit from the archive
    # Return: 1 if successfully skipped
    # Return: 0 on failure
    # -------------------------------------------------------------------------------------------
    def skip_unit(self) :
        return libsrcml.srcml_archive_skip_unit(self.c_archive)

    # -------------------------------------------------------------------------------------------
    # Append the XPath expression to the list of transformations/queries
    # Note: Currently, there is no way to specify context to the expression.
    # Parameter: xpath_string -> An XPath expression
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_xpath(self, xpath_string: str) -> None:
        if type(xpath_string) != str:
            raise srcMLTypeError(self.append_transform_xpath,"xpath_string",xpath_string)

        status = libsrcml.srcml_append_transform_xpath(self.c_archive, xpath_string.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the XPath expression to the list of transformations/queries.
    # Instead of outputting the results in a separate unit tag, output the complete
    # archive marking the XPath results with a user provided attribute
    # Parameter: xpath_string -> An XPath expression
    # Parameter: prefix -> Attribute prefix
    # Parameter: namespace_uri -> Attribute namespace
    # Parameter: attr_name -> Attribute name
    # Parameter: attr_value -> Attribute value
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_xpath_attribute(self, xpath_string: str, prefix: str, namespace_uri: str, attr_name: str, attr_value: str) -> None:
        if type(xpath_string) != str:
            raise srcMLTypeError(self.append_transform_xpath_attribute,"xpath_string",xpath_string)
        if type(prefix) != str:
            raise srcMLTypeError(self.append_transform_xpath_attribute,"prefix",prefix)
        if type(namespace_uri) != str:
            raise srcMLTypeError(self.append_transform_xpath_attribute,"namespace_uri",namespace_uri)
        if type(attr_name) != str:
            raise srcMLTypeError(self.append_transform_xpath_attribute,"attr_name",attr_name)
        if type(attr_value) != str:
            raise srcMLTypeError(self.append_transform_xpath_attribute,"attr_value",attr_value)

        status = libsrcml.srcml_append_transform_xpath_attribute(self.c_archive, xpath_string.encode(), prefix.encode(), namespace_uri.encode(), attr_name.encode(), attr_value.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the XPath expression to the list of transformations/queries.
    # Instead of outputting the results in a separate unit tag, output the complete
    # archive marking the XPath results with a user provided element
    # Parameter: xpath_string -> An XPath expression
    # Parameter: prefix -> Element prefix
    # Parameter: namespace_uri -> Element namespace
    # Parameter: element -> Element name
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_xpath_element(self, xpath_string: str, prefix: str, namespace_uri: str, element: str) -> None:
        if type(xpath_string) != str:
            raise srcMLTypeError(self.append_transform_xpath_element,"xpath_string",xpath_string)
        if type(prefix) != str:
            raise srcMLTypeError(self.append_transform_xpath_element,"prefix",prefix)
        if type(namespace_uri) != str:
            raise srcMLTypeError(self.append_transform_xpath_element,"namespace_uri",namespace_uri)
        if type(element) != str:
            raise srcMLTypeError(self.append_transform_xpath_element,"element",element)
        
        status = libsrcml.srcml_append_transform_xpath_element(self.c_archive, xpath_string.encode(), prefix.encode(), namespace_uri.encode(), element.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program at the designated filename path to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_filename -> An XSLT program filename path
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_filename(self, xslt_filename: str) -> None:
        if type(xslt_filename) != str:
            raise srcMLTypeError(self.append_transform_xslt_filename,"xslt_filename",xslt_filename)
        
        status = libsrcml.srcml_append_transform_xslt_filename(self.c_archive, xslt_filename.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program from a buffer to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_buffer -> A buffer holding an XSLT
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_memory(self, xslt_buffer: bytes | str) -> None:
        if type(xslt_buffer) != bytes and type(xslt_buffer) != str:
            raise srcMLTypeError(self.append_transform_xslt_memory,"xslt_buffer",xslt_buffer)
        if type(xslt_buffer) == str:
            xslt_buffer = xslt_buffer.encode()

        status = libsrcml.srcml_append_transform_xslt_memory(self.c_archive, xslt_buffer, len(xslt_buffer))
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append an XSLT program from a file to the list of transformations/queries
    # Note: Currently no way to specify parameters or context
    # Parameter: xslt_file -> A file containing an XSLT program
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_xslt_file(self, xslt_file: File) :
        if type(xslt_file) != File:
            raise srcMLTypeError(self.append_transform_xslt_file,"xslt_file",xslt_file)
        check_srcml_status(libsrcml.srcml_append_transform_xslt_fd(self.c_archive, xslt_file.fileno()))

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema from a filename path to the list of transformations/queries
    # Parameter: relaxng_filename -> A RelaxNG schema filename path
    # Return: SRCML_STATUS_OK on success
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_filename(self, relaxng_filename: str) -> None:
        if type(relaxng_filename) != str:
            raise srcMLTypeError(self.append_transform_relaxng_filename,"relaxng_filename",relaxng_filename)
        
        status = libsrcml.srcml_append_transform_relaxng_filename(self.c_archive, relaxng_filename.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema in the buffer to the list of transformations/queries
    # Parameter: relaxng_buffer -> A buffer holding a RelaxNG schema
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_memory(self, relaxng_buffer: bytes | str) -> None :
        if type(relaxng_buffer) != bytes and type(relaxng_buffer) != str:
            raise srcMLTypeError(self.append_transform_relaxng_memory,"relaxng_buffer",relaxng_buffer)
        if type(relaxng_buffer) == str:
            relaxng_buffer = relaxng_buffer.encode()

        status = libsrcml.srcml_append_transform_relaxng_memory(self.c_archive, relaxng_buffer, len(relaxng_buffer))
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the RelaxNG schema in a file descriptor to the list of transformations/queries
    # Parameter: relaxng_file -> A file containing a RelaxNG schema
    # Return: Status error code on failure
    # -------------------------------------------------------------------------------------------
    def append_transform_relaxng_file(self, relaxng_file: File) :
        if type(relaxng_file) != File:
            raise srcMLTypeError(self.append_transform_relaxng_file,"relaxng_file",relaxng_file)
        check_srcml_status(libsrcml.srcml_append_transform_relaxng_fd(self.c_archive, relaxng_file.fileno()))

    # -------------------------------------------------------------------------------------------
    # Append the srcQL query to the list of transformations/queries
    # -------------------------------------------------------------------------------------------
    def append_transform_srcql(self, srcql_string: str) -> None:
        if type(srcql_string) != str:
            raise srcMLTypeError(self.append_transform_srcql,"srcql_string",srcql_string)

        status = libsrcml.srcml_append_transform_srcql(self.c_archive, srcql_string.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the srcQL query to the list of transformations/queries.
    # Instead of outputting the results in a separate unit tag, output the complete
    # archive marking the XPath results with a user provided element.
    # -------------------------------------------------------------------------------------------
    def append_transform_srcql_attribute(self, srcql_string: str, prefix: str, namespace_uri: str, attr_name: str, attr_value: str) -> None:
        if type(srcql_string) != str:
            raise srcMLTypeError(self.append_transform_srcql_attribute,"srcql_string",srcql_string)
        if type(prefix) != str:
            raise srcMLTypeError(self.append_transform_srcql_attribute,"prefix",prefix)
        if type(namespace_uri) != str:
            raise srcMLTypeError(self.append_transform_srcql_attribute,"namespace_uri",namespace_uri)
        if type(attr_name) != str:
            raise srcMLTypeError(self.append_transform_srcql_attribute,"attr_name",attr_name)
        if type(attr_value) != str:
            raise srcMLTypeError(self.append_transform_srcql_attribute,"attr_value",attr_value)

        status = libsrcml.srcml_append_transform_srcql_attribute(self.c_archive, srcql_string.encode(), prefix.encode(), namespace_uri.encode(), attr_name.encode(), attr_value.encode())
        check_srcml_status(status)


    # -------------------------------------------------------------------------------------------
    # Append the srcQL query to the list of transformations/queries.
    # Instead of outputting the results in a separate unit tag, output the complete
    # archive marking the XPath results with a user provided element.
    # -------------------------------------------------------------------------------------------
    def append_transform_srcql_element(self, srcql_string: str, prefix: str, namespace_uri: str, element: str) -> None:
        if type(srcql_string) != str:
            raise srcMLTypeError(self.append_transform_srcql_element,"srcql_string",srcql_string)
        if type(prefix) != str:
            raise srcMLTypeError(self.append_transform_srcql_element,"prefix",prefix)
        if type(namespace_uri) != str:
            raise srcMLTypeError(self.append_transform_srcql_element,"namespace_uri",namespace_uri)
        if type(element) != str:
            raise srcMLTypeError(self.append_transform_srcql_element,"element",element)
        
        status = libsrcml.srcml_append_transform_srcql_element(self.c_archive, srcql_string.encode(), prefix.encode(), namespace_uri.encode(), element.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append an XSLT parameter to the last transformation
    # Parameter: param_name -> Name of a parameter
    # Parameter: param_value -> Value of the parameter
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_param(self, param_name: str, param_value: str) -> None:
        if type(param_name) != str:
            raise srcMLTypeError(self.append_transform_param,"param_name",param_name)
        if type(param_value) != str:
            raise srcMLTypeError(self.append_transform_param,"param_value",param_value)

        check_srcml_status(libsrcml.srcml_append_transform_param(self.c_archive, param_name.encode(), param_value.encode()))

    # -------------------------------------------------------------------------------------------
    # Append a string XSLT parameter to the last transformation, with the value wrapped in quotes
    # Parameter: param_name -> Name of a parameter
    # Parameter: param_value -> Value of the named parameter wrapped in quotes (")
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def append_transform_stringparam(self, param_name: str, param_value: str) -> None:
        if type(param_name) != str:
            raise srcMLTypeError(self.append_transform_stringparam,"param_name",param_name)
        if type(param_value) != str:
            raise srcMLTypeError(self.append_transform_stringparam,"param_value",param_value)

        check_srcml_status(libsrcml.srcml_append_transform_stringparam(self.c_archive, param_name.encode(), param_value.encode()))

    # -------------------------------------------------------------------------------------------
    # Apply appended transformations inorder added and consecutively.
    # Intermediate results are stored in a temporary file.
    # Transformations are cleared.
    # Return: The srcMLTransformResult containing the changed units
    # -------------------------------------------------------------------------------------------
    def unit_apply_transforms(self, unit: srcMLUnit) -> srcMLTransformResult:
        if type(unit) != srcMLUnit:
            raise srcMLTypeError(self.unit_apply_transforms,"unit",unit)
        res = srcMLTransformResult()
        check_srcml_status(libsrcml.srcml_unit_apply_transforms(self.c_archive,unit.c_unit, pointer(res.c_res)))
        return res

    # -------------------------------------------------------------------------------------------
    # Remove all transformations from archive.
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def clear_transforms(self) -> None:
        check_srcml_status(libsrcml.srcml_clear_transforms(self.c_archive))



class srcMLArchiveWrite(srcMLArchive):
    def __init__(self, out: str | File, clone_from: srcMLArchive | None = None):
        if not isinstance(clone_from,srcMLArchive) and clone_from != None:
            raise srcMLTypeError(self.__init__, "clone_from", clone_from, inheritance_flag=True)

        super().__init__(None if clone_from == None else libsrcml.srcml_archive_clone(clone_from.c_archive))
        
        if type(out) != str and type(out) != File:
            raise srcMLTypeError(self.__init__,"out",out)
        elif type(out) == str:
            status = libsrcml.srcml_archive_write_open_filename(self.c_archive, out.encode())
        elif type(out) == File:
            status = libsrcml.srcml_archive_write_open_fd(self.c_archive,out.fileno())
        #elif out == None: # None, for cloning
        #    status = srcMLStatus.OK
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the srcml unit to the srcml archive
    # Parameter: unit -> A srcml unit to output
    # Note: Can not mix with by element mode
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_unit(self, unit: srcMLUnit) -> None:
        if type(unit) != srcMLUnit:
            raise srcMLTypeError(self.write_unit,"unit",unit)
        status = libsrcml.srcml_archive_write_unit(self.c_archive, unit.c_unit)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Append the string to the srcml archive
    # Parameter: s -> String to write
    # Parameter: len -> Length of the string to write
    # Note: Can not mix with by element mode
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_string(self, s: str) -> None:
        if type(s) != str:
            raise srcMLTypeError(self.write_string,"s",s)
        
        status = libsrcml.srcml_archive_write_string(self.c_archive, s.encode(), len(s))
        check_srcml_status(status)



class srcMLArchiveWriteString(srcMLArchiveWrite):
    def __init__(self, clone_from: srcMLArchive | None = None):
        if not isinstance(clone_from,srcMLArchive) and clone_from != None:
            raise srcMLTypeError(self.__init__, "clone_from", clone_from, inheritance_flag=True)

        super(srcMLArchiveWrite, self).__init__(None if clone_from == None else libsrcml.srcml_archive_clone(clone_from.c_archive))

        self.buffer = c_char_p()
        self.size = c_size_t()
        status = libsrcml.srcml_archive_write_open_memory(self.c_archive, pointer(self.buffer), pointer(self.size))
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Close a srcml archive opened using archive.read_open_*() or archive.write_open_*()
    # Note: Special close for srcMLArchiveWriteString
    #       Sets a closed flag and allows for the return of the buffer content
    # Return: str containing output
    # -------------------------------------------------------------------------------------------
    def close(self) -> str:
        super().close()
        return self.get_output_string()

    # -------------------------------------------------------------------------------------------
    # Get the output string of a closed srcMLArchiveWriteString
    # Return: str containing output
    # -------------------------------------------------------------------------------------------
    def get_output_string(self) -> str:
        if not self.closed:
            raise IOError("srcMLArchiveWriteString needs to be closed before accessing output string")
        return self.buffer.value.decode()
