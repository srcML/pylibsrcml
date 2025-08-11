# SPDX-License-Identifier: GPL-3.0-only
"""
@file utility_funcs.py

@copyright Copyright (C) 2014-2025 srcML, LLC. (www.srcML.org)

This file is part of pylibsrcml, a Python binding of libsrcml
"""

from .globals import libsrcml
from .exceptions import srcMLTypeError

def version_number() -> int:
    """
    The current version of the srcml markup
    Return: Version of the srcml markup as a number
    """
    return libsrcml.srcml_version_number()

def version_string() -> str:
    """
    The current version of the srcml markup
    Return: Version of the srcml markup as a string
    """
    return libsrcml.srcml_version_string().decode()

def markup_version_number(language: str) -> int:
    """
    The current version of the srcml markup
    Parameter: language -> Source code language
    Return: Version of the srcml markup as a number
    """
    if type(language) != str:
        raise srcMLTypeError(markup_version_number,"language",language)
    return libsrcml.srcml_markup_version_number(language.encode())

def markup_version_string(language: str) -> str:
    """
    The current version of the srcml markup
    Parameter: language -> Source code language
    Return: Version of the srcml markup as a string
    """
    if type(language) != str:
        raise srcMLTypeError(markup_version_number,"language",language)
    return libsrcml.srcml_markup_version_string(language.encode())

def libsrcml_version_number() -> int:
    """
    The current version of the library
    Return: Version of libsrcml as a number
    """
    return libsrcml.srcml_libsrcml_version_number()

def libsrcml_version_string() -> str:
    """
    The current version of the library
    Return: Version of libsrcml as a string
    """
    return libsrcml.srcml_libsrcml_version_string().decode()

def check_language(language: str) -> int:
    """
    Checks if a source-code language is supported.
    Parameter: language -> The language to check support for as a string
    Return Value: pos -> The numeric representation for that language
    Return Value: 0 -> If the language is not supported
    """
    if type(language) != str:
        #raise TypeError(f"check_language requires a str (not {type(language)}")
        raise srcMLTypeError(check_language,"language",language)
    return libsrcml.srcml_check_language(language.encode())

def check_extension(filename: str) -> str | None:
    """
    Check the current registered language for a file extension
    Parameter: filename -> The name of a file. When a full filename is given, the extension is extracted
    Return: The language name registered with that extension on success
    Return: None on failure
    """
    if type(filename) != str:
        raise srcMLTypeError(check_extension,"filename",filename)
    result = libsrcml.srcml_check_extension(filename.encode())
    return result.decode() if result else None

def get_language_list_size() -> int:
    """
    Gets the number of supported source-code languages
    Return: The number of source-code languages supported
    """
    return libsrcml.srcml_get_language_list_size()

def get_language_from_list_pos(pos: int) -> str | None:
    """
    Gets the name of the supported language at a given position
    Parameter: pos -> The position of the language in the supported language list
    Return: The name of the supported source-code language on success
    Return: NULL on failure
    """
    if type(pos) != int:
        raise srcMLTypeError(get_language_from_list_pos,"pos",pos)
    if pos < 0 or pos > get_language_list_size()-1:
        raise IndexError("Language index out of bounds")
    result = libsrcml.srcml_get_language_list(pos)
    return result.decode() if result else None

def get_language_list() -> [str]:
    """
    Uses get_language_list_size and get_language_from_list_pos to return a
    list of languages
    """
    language_list = []
    for i in range(get_language_list_size()):
        language_list.append(get_language_from_list_pos(i))
    return language_list

def check_encoding(encoding: str) -> int:
    """
    Check if a particular encoding is supported for input and output
    Parameter: encoding -> The name of the encoding
    """
    if type(encoding) != str:
        raise srcMLTypeError(check_encoding,"encoding",encoding)
    return libsrcml.srcml_check_encoding(encoding.encode())

def check_xslt() -> int:
    """
    Check if XSLT is available
    Return Value: 1 ->  if XSLT is available
    Return Value: 0 -> if it is unavailable
    """
    return libsrcml.srcml_check_xslt()

def check_exslt() -> int:
    """
    Check if EXSLT is available
    Return Value: 1 ->  if EXSLT is available
    Return Value: 0 -> if it is unavailable
    """
    return libsrcml.srcml_check_exslt()

def error_string() -> str:
    """
    Provides a description of the last error to occur
    Return: A string describing last recorded error
    """
    result = libsrcml.srcml_error_string()
    return result.decode() if result else None
