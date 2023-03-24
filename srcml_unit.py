from .globals import libsrcml
from .exceptions import srcMLTypeError, srcMLInvalidConstruction, check_srcml_status

from ctypes import pointer, c_char_p, c_size_t

from io import TextIOWrapper as File

class srcMLUnit:
    def __init__(self, unit_ptr: int, freeable: bool = True):
        self.c_unit = unit_ptr
        self.is_freeable = freeable

    # -------------------------------------------------------------------------------------------
    # Clone the setup of an existing unit
    # Parameter: unit -> A srcml unit
    # Return: The cloned unit
    # TODO: This may cause a memory leak
    # -------------------------------------------------------------------------------------------
    def clone(self):
        copy_ptr = libsrcml.srcml_unit_clone(self.c_unit)
        copy = srcMLUnit(copy_ptr)
        return copy

    # -------------------------------------------------------------------------------------------
    # Provides a code of the last error to occur for a unit
    # Parameter: unit -> A srcml_unit
    # Return: A code for the last recorded error
    # -------------------------------------------------------------------------------------------
    def error_number(self) -> int:
        return libsrcml.srcml_unit_error_number(self.c_unit)

    # -------------------------------------------------------------------------------------------
    # Provides a description of the last error to occur for a unit
    # Parameter: unit -> A srcml unit
    # Return: A string describing last recorded error
    # -------------------------------------------------------------------------------------------
    def error_string(self) -> str | None:
       result = libsrcml.srcml_unit_error_string(self.c_unit)
       return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Free an allocated unit (void srcml_unit_free(struct srcml_unit*))
    # -------------------------------------------------------------------------------------------
    def __del__(self) -> None:
        print("TOP_UNIT")
        if self.c_unit != 0 and self.c_unit != None and self.is_freeable:
            libsrcml.srcml_unit_free(self.c_unit)
        print("BOT_UNIT")

    # -------------------------------------------------------------------------------------------
    # Set the source-code encoding for the srcml unit
    # Parameter: encoding -> A source-code encoding
    # Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_src_encoding(self, encoding: str) -> None :
        if type(encoding) != str:
            raise srcMLTypeError(self.set_src_encoding,"encoding",encoding)
        status = libsrcml.srcml_unit_set_src_encoding(self.c_unit, encoding.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the source-code language for the srcml unit
    # Parameter: language -> A supported source-code language
    # Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_language(self, language: str) -> None:
        if type(language) != str:
            raise srcMLTypeError(self.set_language,"language",language)
        status = libsrcml.srcml_unit_set_language(self.c_unit, language.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the filename attribute for the srcml unit
    # Parameter: filename -> The name of a file
    # Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_filename(self, filename: str) -> None:
        if type(filename) != str:
            raise srcMLTypeError(self.set_filename,"filename",filename)
        status = libsrcml.srcml_unit_set_filename(self.c_unit, filename.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the version attribute for the srcml unit
    # Parameter: version -> A version string
    # Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_version(self, version: str) -> None :
        if type(version) != str:
            raise srcMLTypeError(self.set_version,"version",version)
        status = libsrcml.srcml_unit_set_version(self.c_unit, version.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the timestamp attribute for the srcml unit
    # Parameter: timestamp -> A timestamp string
    # Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_timestamp(self, timestamp: str) -> None :
        if type(timestamp) != str:
            raise srcMLTypeError(self.set_timestamp,"timestamp",timestamp)
        status = libsrcml.srcml_unit_set_timestamp(self.c_unit, timestamp.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Set the type of end of line to be used for unparse
    # Parameter: eol -> The kind of eol to use for unparse
    # Return: Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def set_eol(self, eol: int) -> None:
        if type(eol) != int:
            raise srcMLTypeError(self.set_eol,"eol",eol)
        status = libsrcml.srcml_unit_set_eol(self.c_unit, eol)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Return: The source-code encoding for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_src_encoding(self) -> str | None:
        result = libsrcml.srcml_unit_get_src_encoding(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The revision for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_revision(self) -> str | None:
        result = libsrcml.srcml_unit_get_revision(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The source-code language for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_language(self) -> str | None:
        result = libsrcml.srcml_unit_get_language(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The filename attribute on the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_filename(self) -> str | None:
        result = libsrcml.srcml_unit_get_filename(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # The version for the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_version(self) -> str | None:
        result = libsrcml.srcml_unit_get_version(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The timestamp attribute on the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_timestamp(self) -> str | None:
        result = libsrcml.srcml_unit_get_timestamp(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The hash attribute on the unit on success, or NULL
    # -------------------------------------------------------------------------------------------
    def get_hash(self) -> str | None:
        result = libsrcml.srcml_unit_get_hash(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Return: The loc of the source code in the unit, or -1 on failure
    # -------------------------------------------------------------------------------------------
    def get_loc(self) -> int:
        return libsrcml.srcml_unit_get_loc(self.c_unit)

    # -------------------------------------------------------------------------------------------
    # Return: The eol for to-src output (unparse), or NULL
    # -------------------------------------------------------------------------------------------
    def get_eol(self) -> int:
        return libsrcml.srcml_unit_get_eol(self.c_unit)

    # -------------------------------------------------------------------------------------------
    # Get a complete, valid XML of the srcML from this unit
    # The XML returned is a complete solo srcML unit
    # Note: Do not free
    # Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
    # Return: The standalone unit srcML on success and NULL on failure.
    # -------------------------------------------------------------------------------------------
    def get_srcml(self) -> str | None:
        result = libsrcml.srcml_unit_get_srcml(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Get a fragment of the srcML from this unit
    # The XML returned is UTF-8 encoded XML. It is not well-formed XML, e.g., it is missing
    # the archive namespace declarations
    # Note: Do not free
    # Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
    # Return: The fragment unit srcML on success and NULL on failure.
    # -------------------------------------------------------------------------------------------
    def get_srcml_outer(self) -> str | None :
        result = libsrcml.srcml_unit_get_srcml_outer(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Get the srcML without the enclosing unit tags
    # The XML fragment returned is UTF-8 encoded XML. It is not well-formed XML, e.g., it is missing
    # the archive namespace declarations and may not have a single root.
    # Note: Do not free
    # Note: String is valid until the unit is freed, or another unit.get_srcml*() is called
    # Return: The fragment unit srcML on success and NULL on failure.
    # -------------------------------------------------------------------------------------------
    def get_srcml_inner(self) :
        result = libsrcml.srcml_unit_get_srcml_inner(self.c_unit)
        return result.decode() if result else None

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the file with the name src_filename to srcML and store in the unit
    # Parameter: src_filename -> Name of a file to parse into srcML
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def parse_filename(self, src_filename: str) -> None :
        if type(src_filename) != str:
            raise srcMLTypeError(self.parse_filename,"src_filename",src_filename)

        status = libsrcml.srcml_unit_parse_filename(self.c_unit, src_filename.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the src_buffer to srcML and store in the unit
    # Parameter: src_buffer -> Buffer containing source code to parse into srcML
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def parse_memory(self, src_buffer: bytes | str) -> None :
        if type(src_buffer) != bytes and type(src_buffer) != str:
            raise srcMLTypeError(self.parse_memory,"src_buffer",src_buffer)
        if type(src_buffer) == str:
            src_buffer = src_buffer.encode() if self.get_src_encoding() == None else src_buffer.encode(self.get_src_encoding())



        status = libsrcml.srcml_unit_parse_memory(self.c_unit, src_buffer, len(src_buffer))
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the source-code file to srcML and store in the unit
    # Parameter: src_file -> A Python file opened for reading
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def parse_file(self, src_file: File) -> None:
        if type(src_file) != File:
            raise srcMLTypeError(self.parse_file,"src_file",src_file)
        status = libsrcml.srcml_unit_parse_fd(self.c_unit,src_file.fileno())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Convert the contents of the source-code FILE* to srcML and store in the unit
    # Parameter: src_file -> A FILE* opened for reading
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    # NOTE: Disabled - there is no FILE* in Python
    #def parse_FILE(self, src_file) :
    #    check_return(libsrcml.srcml_unit_parse_FILE(self.unit, src_file))

    # -------------------------------------------------------------------------------------------
    # Convert the contents of a file descriptor and stored in the unit
    # Parameter: unit -> A srcml_unit to parse the results to
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    # NOTE: Disabled - there is no file descriptor in Python
    #def parse_fd(self, src_fd) :
    #    check_return(libsrcml.srcml_unit_parse_fd(self.unit, src_fd))

    # -------------------------------------------------------------------------------------------
    # Convert to srcML the contents from the opened context accessed via read and close callbacks and place it into a unit
    # Parameter: context -> an io context
    # Parameter: read_callback -> a read callback function
    # Parameter: close_callback -> a close callback function
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    # NOTE: Disabled - Not sure this is needed for Python
    #def parse_io(self, context, read_callback, close_callback) :
    #    check_return(libsrcml.srcml_unit_parse_io(self.unit, context, read_callback, close_callback))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and place it into a filename
    # If the srcML was not read in, but the attributes were, the XML is read in and that value is unparsed
    # Parameter: src_filename -> Name of a file to output contents of unit as source
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def unparse_filename(self, src_filename: str) -> None :
        if type(src_filename) != str:
            raise srcMLTypeError(self.unparse_filename,"src_filename",src_filename)

        status = libsrcml.srcml_unit_unparse_filename(self.c_unit, src_filename.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and place it into a buffer
    # The buffer is allocated in the function and needs to be freed after using.
    # Return: a bytes buffer containing the unit srcML data
    # -------------------------------------------------------------------------------------------
    def unparse_memory(self) -> bytes :
        buffer = c_char_p()
        size = c_size_t()
        status = libsrcml.srcml_unit_unparse_memory(self.c_unit, pointer(buffer), pointer(size))
        check_srcml_status(status)
        return buffer.value

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and place it into a buffer
    # The buffer is allocated in the function and needs to be freed after using.
    # Return: a string containing the unit srcML data
    # -------------------------------------------------------------------------------------------
    def unparse_string(self) -> str :
        buffer = c_char_p()
        size = c_size_t()
        status = libsrcml.srcml_unit_unparse_memory(self.c_unit, pointer(buffer), pointer(size))
        check_srcml_status(status)
        return buffer.value.decode() if self.get_src_encoding() == None else buffer.value.decode(self.get_src_encoding())

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and output to the FILE*
    # Parameter: file -> FILE* opened for writing to output the source file
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    # NOTE: Disabled, Python doesn't have FILE*
    #def unparse_FILE(self, file) :
    #    check_return(libsrcml.srcml_unit_unparse_FILE(self.unit, file))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and output to the file descriptor
    # Parameter: fd File descriptor opened for writing to output the source file
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    # NOTE: Python doesn't have file descriptor
    #def unparse_fd(self, fd) :
    #    check_return(libsrcml.srcml_unit_unparse_fd(self.unit, fd))

    # -------------------------------------------------------------------------------------------
    # Convert the srcML in a unit into source code and output using write callbacks
    # Parameter: context -> an io context
    # Parameter: write_callback -> a write callback function
    # Parameter: close_callback -> a close callback function
    # Return: SRCML_STATUS_OK on success
    # Return: Status error code on failure.
    # -------------------------------------------------------------------------------------------
    # NOTE: Disabled, not sure if this is needed for Python
    #def unparse_io(self, context, write_callback, close_callback) :
    #    check_return(libsrcml.srcml_unit_unparse_io(self.unit, context, write_callback, close_callback))

    # -------------------------------------------------------------------------------------------
    # Write a start tag for a unit
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_start_unit(self) -> None:
        status = libsrcml.srcml_write_start_unit(self.c_unit)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Write an end tag for a unit
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_end_unit(self) -> None:
        status = libsrcml.srcml_write_end_unit(self.c_unit)

    # -------------------------------------------------------------------------------------------
    # Write a start tag for a general element
    # Parameter: prefix -> Element prefix
    # Parameter: name -> Element name
    # Parameter: uri -> URI of the prefix
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_start_element(self, prefix: str, name: str, uri: str) -> None:
        if type(prefix) != str:
            raise srcMLTypeError(self.write_start_element,"prefix",prefix)
        if type(name) != str:
            raise srcMLTypeError(self.write_start_element,"name",name)
        if type(uri) != str:
            raise srcMLTypeError(self.write_start_element,"uri",uri)
        
        status = libsrcml.srcml_write_start_element(self.c_unit, prefix.encode(), name.encode(), uri.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Write an end tag for a general element
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_end_element(self) :
        status = libsrcml.srcml_write_end_element(self.c_unit)
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Write a namespace
    # Parameter: prefix -> Namespace prefix
    # Parameter: uri -> Namespace URI
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_namespace(self, prefix: str, uri: str) -> None:
        if type(prefix) != str:
            raise srcMLTypeError(self.write_start_element,"prefix",prefix)
        if type(uri) != str:
            raise srcMLTypeError(self.write_start_element,"uri",uri)
        
        status = libsrcml.srcml_write_namespace(self.c_unit, prefix,encode(), uri.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Write an attribute
    # Parameter: prefix -> Element prefix
    # Parameter: name -> Element name
    # Parameter: uri -> URI of the prefix
    # Parameter: content -> Value of the attribute
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_attribute(self, prefix: str, name: str, uri: str, content: str) -> None :
        if type(prefix) != str:
            raise srcMLTypeError(self.write_attribute,"prefix",prefix)
        if type(name) != str:
            raise srcMLTypeError(self.write_attribute,"name",name)
        if type(uri) != str:
            raise srcMLTypeError(self.write_attribute,"uri",uri)
        if type(content) != str:
            raise srcMLTypeError(self.write_attribute,"content",content)
        

        status = libsrcml.srcml_write_attribute(self.c_unit, prefix.encode(), name.encode(), uri.encode(), content.encode())
        check_srcml_status(status)

    # -------------------------------------------------------------------------------------------
    # Write a general string
    # Parameter: content -> Null-terminated string to write
    # Return: CHANGED FOR PYLIBSRCML: returns nothing, simply raises an error if status isn't OK
    # -------------------------------------------------------------------------------------------
    def write_string(self, content: str) -> None :
        if type(content) != str:
            raise srcMLTypeError(self.write_string,"content",content)
        
        status = libsrcml.srcml_write_string(self.unit, content.encode())
        check_srcml_status(status)

   
