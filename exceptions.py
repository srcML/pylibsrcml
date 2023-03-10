from .values import srcMLStatus

# Class representing an error for when srcML cannot be found
class srcMLNotFoundError(Exception):
    def __str__(self):
        return "srcML could not be found on your system. For installation instructions, visit https://www.srcml.org/"

# Class representing an error for when an invalid type is passed to a pylibsrcml function
class srcMLTypeError(Exception):
    def __init__(self, func: "function", arg: str, val, *, inheritance_flag = False):
        if not inheritance_flag:
            self.msg = f"{func.__name__} requires that parameter `{arg}` be {str(func.__annotations__[arg])} (not {str(type(val))})"
        else:
            self.msg = f"{func.__name__} requires that parameter {arg} be or inherit from {str(func.__annotations__[arg])} (not {str(type(val))})"
    def __str__(self):
        return self.msg

class srcMLInvalidConstruction(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class srcMLException(Exception):
    def __init__(self,error_code):
        self.error_code = error_code
    def __str__(self):
        #print("ST:",status_code)
        match self.error_code:
            case srcMLStatus.ERROR:
                return "General srcML Error occured"
            case srcMLStatus.INVALID_ARGUMENT:
                return "An invalid argument was passed"
            case srcMLStatus.INVALID_INPUT:
                return "The provided input was invalid"
            case srcMLStatus.INVALID_IO_OPERATION:
                return "Unable to execute read I/O operation (input might be read-only)"
            case srcMLStatus.UNINITIALIZED_UNIT:
                return "Unit is uninitialized"
            case srcMLStatus.UNSET_LANGUAGE:
                return "There is no language set"
            case srcMLStatus.NO_TRANSFORMATION:
                return "There are no transformations"
            case _:
                return f"Unknown srcMLStatus: error code {self.error_code}"

class srcMLInvalidResultType(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "An invalid srcMLResult type was incountered."

class srcDiffRevisionInvalid(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "The srcDiff Revision is invalid."

def check_srcml_status(status_code):
    if status_code != srcMLStatus.OK:
        raise srcMLException(status_code)
