# ********************************************************************************************************************************************************
# @file options.py
#
# @copyright Copyright (C) 2022 srcML, LLC (srcML.org)
#
# This file is part of srcML Infrastructure www.srcml.org.
# srcML Infrastructure is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# srcML Infrastructure is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with srcML Infrastructure. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************************************************************************************************

# Current Version
# --------------------------------------------------------
# Number representing libsrcml version
SRCML_VERSION_NUMBER                             = 1000
# String containing libsrcml version
SRCML_VERSION_STRING                             = "1.0.0"
# --------------------------------------------------------


# Status
# --------------------------------------------------------
# Return status indicating no errors
SRCML_STATUS_OK                                  = 0
# Return status indicating general errors occurred
SRCML_STATUS_ERROR                               = 1
# Return status indicating an invalid argument
SRCML_STATUS_INVALID_ARGUMENT                    = 2
# Return status indicating that there is some problem with the input
SRCML_STATUS_INVALID_INPUT                       = 3
# Return status indicating an invalid read I/O operation (such as write on read only archive)
SRCML_STATUS_INVALID_STATUS_INVALID_IO_OPERATION = 4
# Return status indicating that there is some problem with the input
SRCML_STATUS_IO_ERROR                            = 5
# Return status indicating an unitialized unit
SRCML_STATUS_UNINITIALIZED_UNIT                  = 6
# Return status indicating an unset language
SRCML_STATUS_UNSET_LANGUAGE                      = 7
# Return status indicating their are no transformations
SRCML_STATUS_NO_TRANSFORMATION                   = 8
# --------------------------------------------------------


# Language Set
# --------------------------------------------------------
# Language not set
SRCML_LANGUAGE_NONE                              = 0
# Language C
SRCML_LANGUAGE_C                                 = "C"
# Language C++
SRCML_LANGUAGE_CXX                               = "C++"
# Language C#
SRCML_LANGUAGE_CSHARP                            = "C#"
# Language Java
SRCML_LANGUAGE_JAVA                              = "Java"
# Language XML
SRCML_LANGUAGE_XML                               = "XML"
# --------------------------------------------------------


# Options
# --------------------------------------------------------
# Do not issue an XML declaration (default: include XML declaration
SRCML_OPTION_NO_XML_DECL                         = 1<<1
# Include line/column position attributes
SRCML_OPTION_POSITION                            = 1<<2
# Markup preprocessor elements (default for C, C++)
SRCML_OPTION_CPP                                 = 1<<3
# Leave as text preprocessor else parts (default: markup)
SRCML_OPTION_CPP_TEXT_ELSE                       = 1<<4
# Markup preprocessor @code #if 0 @endcode sections (default: leave as text)
SRCML_OPTION_CPP_MARKUP_IF0                      = 1<<5
# Encode the original source encoding as an attribute
SRCML_OPTION_STORE_ENCODING                      = 1<<6
# --------------------------------------------------------


# Source Output EOL Options
# --------------------------------------------------------
# Source-code end of line determined automatically
SOURCE_OUTPUT_EOL_AUTO                           = 0
# Source-code end of line determined according to operating system
SOURCE_OUTPUT_EOL_NATIVE                         = 0
# Source-code end of line is new line only
SOURCE_OUTPUT_EOL_LF                             = 1
# Source-code end of line is carriage return only
SOURCE_OUTPUT_EOL_CR                             = 2
# Source-code end of line is carriage return and new line
SOURCE_OUTPUT_EOL_CRLF                           = 3
# --------------------------------------------------------