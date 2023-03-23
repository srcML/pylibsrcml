from .globals import libsrcml
from .exceptions import srcMLTypeError

# -------------------------------------------------------------------------------------------
# The current version of the library
# Return: Version of libsrcml as a number
# -------------------------------------------------------------------------------------------
def version_number() -> int:
    return libsrcml.srcml_version_number()

# -------------------------------------------------------------------------------------------
# The current version of the library
# Return: Version of libsrcml as a string
# -------------------------------------------------------------------------------------------
def version_string() -> str:
    return libsrcml.srcml_version_string().decode()

# -------------------------------------------------------------------------------------------
# Checks if a source-code language is supported.
# Parameter: language -> The language to check support for as a string
# Return Value: pos -> The numeric representation for that language
# Return Value: 0 -> If the language is not supported
# -------------------------------------------------------------------------------------------
def check_language(language: str) -> int:
    if type(language) != str:
        #raise TypeError(f"check_language requires a str (not {type(language)}")
        raise srcMLTypeError(check_language,"language",language)
    return libsrcml.srcml_check_language(language.encode())

# -------------------------------------------------------------------------------------------
# Check the current registered language for a file extension
# Parameter: filename -> The name of a file. When a full filename is given, the extension is extracted
# Return: The language name registered with that extension on success
# Return: None on failure
# -------------------------------------------------------------------------------------------
def check_extension(filename: str) -> str | None:
    if type(filename) != str:
        raise srcMLTypeError(check_extension,"filename",filename)
    result = libsrcml.srcml_check_extension(filename.encode())
    return result.decode() if result else None

# -------------------------------------------------------------------------------------------
# Gets the number of supported source-code languages
# Return: The number of source-code languages supported
# -------------------------------------------------------------------------------------------
def get_language_list_size() -> int:
    return libsrcml.srcml_get_language_list_size()

# -------------------------------------------------------------------------------------------
# Gets the name of the supported language at a given position
# Parameter: pos -> The position of the language in the supported language list
# Return: The name of the supported source-code language on success
# Return: NULL on failure
# -------------------------------------------------------------------------------------------
def get_language_from_list_pos(pos: int) -> str | None:
    if type(pos) != int:
        raise srcMLTypeError(get_language_from_list_pos,"pos",pos)
    if pos < 0 or pos > get_language_list_size()-1:
        raise IndexError("Language index out of bounds")
    result = libsrcml.srcml_get_language_list(pos)
    return result.decode() if result else None

# New Python Function
# -------------------------------------------------------------------------------------------
# Uses get_language_list_size and get_language_from_list_pos to return a
# list of languages
# -------------------------------------------------------------------------------------------
def get_language_list() -> [str]:
    language_list = []
    for i in range(get_language_list_size()):
        language_list.append(get_language_from_list_pos(i))
    return language_list

# -------------------------------------------------------------------------------------------
# Check if a particular encoding is supported for input and output
# Parameter: encoding -> The name of the encoding
# -------------------------------------------------------------------------------------------
def check_encoding(encoding: str) -> int:
    if type(encoding) != str:
        raise srcMLTypeError(check_encoding,"encoding",encoding)
    return libsrcml.srcml_check_encoding(encoding.encode())

# -------------------------------------------------------------------------------------------
# Check if XSLT is available
# Return Value: 1 ->  if XSLT is available
# Return Value: 0 -> if it is unavailable
# -------------------------------------------------------------------------------------------
def check_xslt() -> int:
    return libsrcml.srcml_check_xslt()

# -------------------------------------------------------------------------------------------
# Check if EXSLT is available
# Return Value: 1 ->  if EXSLT is available
# Return Value: 0 -> if it is unavailable
# -------------------------------------------------------------------------------------------
def check_exslt() -> int:
    return libsrcml.srcml_check_exslt()

# -------------------------------------------------------------------------------------------
# Provides a description of the last error to occur
# Return: A string describing last recorded error
# -------------------------------------------------------------------------------------------
def error_string() -> str:
    result = libsrcml.srcml_error_string()
    return result.decode() if result else None

# -------------------------------------------------------------------------------------------
# Free a memory buffer allocated by functions such as srcml_archive_write_open_memory()
# Parameter: buffer -> The allocated buffer
# -------------------------------------------------------------------------------------------
def memory_free(buffer: bytes) -> None:
    if type(buffer) != bytes:
        raise srcMLTypeError(memory_free,"buffer",buffer)
    libsrcml.srcml_memory_free(buffer)
