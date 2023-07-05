from .values import srcMLStatus

# Class representing an error for when srcML cannot be found
class srcMLNotFoundError(Exception):
    def __init__(self):
        super().__init__("srcML could not be found on your system. For installation instructions, visit https://www.srcml.org/")

# Class representing an error for when an invalid type is passed to a pylibsrcml function
class srcMLTypeError(Exception):
    def __init__(self, func: "function", arg: str, val, *, inheritance_flag = False):
        if not inheritance_flag:
            msg = f"{func.__name__} requires that parameter `{arg}` be {str(func.__annotations__[arg])} (not {str(type(val))})"
        else:
            msg = f"{func.__name__} requires that parameter {arg} be or inherit from {str(func.__annotations__[arg])} (not {str(type(val))})"
        super().__init__(msg)

class srcMLInvalidConstruction(Exception):
    def __init__(self, msg):
        super().__init__(msg)


SRCML_STATUS_ERROR_STRINGS = {
    srcMLStatus.ERROR: "srcMLStatus.ERROR: General srcML Error occured",
    srcMLStatus.INVALID_ARGUMENT: "srcMLStatus.INVALID_ARGUMENT: An invalid argument was passed",
    srcMLStatus.INVALID_INPUT: "srcMLStatus.INVALID_INPUT: The provided input was invalid",
    srcMLStatus.INVALID_IO_OPERATION: "srcMLStatus.INVALID_IO_OPERATION: Unable to execute read I/O operation (input might be read-only)",
    srcMLStatus.IO_ERROR: "srcMLStatus.IO_ERROR: Unable to open provided file",
    srcMLStatus.UNINITIALIZED_UNIT: "srcMLStatus.UNINITIALIZED_UNIT: Unit is uninitialized",
    srcMLStatus.UNSET_LANGUAGE: "srcMLStatus.UNSET_LANGUAGE: There is no language set",
    srcMLStatus.NO_TRANSFORMATION: "srcMLStatus.NO_TRANSFORMATION: There are no transformations",
}
class srcMLException(Exception):
    def __init__(self,error_code):
        self.error_code = error_code
        if error_code not in SRCML_STATUS_ERROR_STRINGS:
            error_string = f"Unknown srcMLStatus: error code {self.error_code}"
        else:
            error_string = SRCML_STATUS_ERROR_STRINGS[error_code]
        super().__init__(error_string)

class srcMLInvalidResultType(Exception):
    def __init__(self):
        super().__init__("An invalid srcMLResult type was incountered.")

class srcDiffRevisionInvalid(Exception):
    def __init__(self):
        super().__init__("The srcDiff Revision is invalid.")

def check_srcml_status(status_code):
    if status_code != srcMLStatus.OK:
        raise srcMLException(status_code)
