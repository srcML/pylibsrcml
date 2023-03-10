from .values import srcMLStatus

# Class representing an error for when srcML cannot be found
class srcMLNotFoundError(Exception):
    def __init__(self):
        super().__init__("srcML could not be found on your system. For installation instructions, visit https://www.srcml.org/")

# Class representing an error for when an invalid type is passed to a pylibsrcml function
class srcMLTypeError(Exception):
    def __init__(self, func: "function", arg: str, val, *, inheritance_flag = False):
        print(func.__annotations__)
        if not inheritance_flag:
            msg = f"{func.__name__} requires that parameter `{arg}` be {str(func.__annotations__[arg])} (not {str(type(val))})"
        else:
            msg = f"{func.__name__} requires that parameter {arg} be or inherit from {str(func.__annotations__[arg])} (not {str(type(val))})"
        super().__init__(msg)

class srcMLInvalidConstruction(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class srcMLException(Exception):
    def __init__(self,error_code):
        match error_code:
            case srcMLStatus.ERROR:
                error_string = "srcMLStatus.ERROR: General srcML Error occured"
            case srcMLStatus.INVALID_ARGUMENT:
                error_string = "srcMLStatus.INVALID_ARGUMENT: An invalid argument was passed"
            case srcMLStatus.INVALID_INPUT:
                error_string = "srcMLStatus.INVALID_INPUT: The provided input was invalid"
            case srcMLStatus.INVALID_IO_OPERATION:
                error_string = "srcMLStatus.INVALID_IO_OPERATION: Unable to execute read I/O operation (input might be read-only)"
            case srcMLStatus.UNINITIALIZED_UNIT:
                error_string = "srcMLStatus.UNINITIALIZED_UNIT: Unit is uninitialized"
            case srcMLStatus.UNSET_LANGUAGE:
                error_string = "srcMLStatus.UNSET_LANGUAGE: There is no language set"
            case srcMLStatus.NO_TRANSFORMATION:
                error_string = "srcMLStatus.NO_TRANSFORMATION: There are no transformations"
            case _:
                error_string =f"Unknown srcMLStatus: error code {self.error_code}"
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
