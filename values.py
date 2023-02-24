#from enum import Enum

class srcMLStatus:
    OK = 0 # Return status indicating no errors
    ERROR = 1 # Return status indicating general errors occurred
    INVALID_ARGUMENT = 2 # Return status indicating an invalid argument
    INVALID_INPUT = 3 # Return status indicating that there is some problem with the input
    INVALID_IO_OPERATION = 4 # Return status indicating an invalid read I/O operation (such as write on read only archive)
    IO_ERROR = 5 # Return status indicating that there is some problem with the input
    UNITIALIZED_UNIT = 6 # Return status indicating an unitialized unit
    UNSET_LANGUAGE = 7 # Return status indicating an unset language
    NO_TRANSFORMATION = 8 # Return status indicating there are no transformations

class srcMLOption:
    NO_XML_DECL = 1<<1 # Do not issue an XML declaration (default: include XML declaration
    POSITION = 1<<2 # Include line/column position attributes
    CPP = 1<<3 # Markup preprocessor elements (default for C, C++)
    CPP_TEXT_ELSE = 1<<4 # Leave as text preprocessor else parts (default: markup)
    CPP_MARKUP_IF0 = 1<<5 # Markup preprocessor @code #if 0 @endcode sections (default: leave as text)
    STORE_ENCODING = 1<<6 # Encode the original source encoding as an attribute

class SourceOutputEOL:
    AUTO = 0 # Source-code end of line determined automatically
    NATIVE = 0 # Source-code end of line determined according to operating system
    LF = 1 # Source-code end of line is new line only
    CR = 2 # Source-code end of line is carriage return only
    CRLF = 3 # Source-code end of line is carriage return and new line

class srcMLResult:
    NONE = 0
    UNITS = 1
    BOOLEAN = 2
    NUMBER = 3
    STRING = 4

class srcDiffRevision:
    ORIGINAL = 0
    MODIFIED = 1
    INVALID = 2