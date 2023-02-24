from .globals import libsrcml
from .values import srcMLStatus, srcMLResult
from .exceptions import srcMLTypeError, srcMLInvalidResultType, check_srcml_status
from .srcml_unit import srcml_unit

class srcml_transform_result:

    # -------------------------------------------------------------------------------------------
    # Create a new srcml_transform_unit
    # -------------------------------------------------------------------------------------------
    def __init__(self, res_ptr: int):
        if type(res_ptr) != int:
            raise srcMLTypeError(self.__init__,"res_ptr",res_ptr)
        self.c_res = res_ptr

    # -------------------------------------------------------------------------------------------
    # Free the resources in a tranformation result.
    # -------------------------------------------------------------------------------------------
    def __del__(self):
        libsrcml.srcml_transform_free(self.c_res)

    # -------------------------------------------------------------------------------------------
    # Return: An int representing the transform type
    # -------------------------------------------------------------------------------------------
    def get_type(self) -> int:
        return libsrcml.srcml_transform_get_type(self.c_res)

    # -------------------------------------------------------------------------------------------
    # Return: The number of units in the transformation result
    # -------------------------------------------------------------------------------------------
    def get_unit_size(self) -> int:
        return libsrcml.srcml_transform_get_unit_size(self.c_res)

    # -------------------------------------------------------------------------------------------
    # Return: The unit at index i
    # -------------------------------------------------------------------------------------------
    def get_unit(self, i: int) -> srcml_unit:
        if type(i) != int:
            raise srcMLTypeError(self.get_unit,"i",i)
        if self.get_type() != srcMLResult.UNITS:
            raise srcMLInvalidResultType()
        rtn = libsrcml.srcml_transform_get_unit(self.c_res,i)
        if rtn == 0:
            raise srcMLException(srcMLStatus.ERROR)
        return srcml_unit(None,rtn)

    # -------------------------------------------------------------------------------------------
    # Return: The trasnformation result string
    # -------------------------------------------------------------------------------------------
    def get_string() -> str | None:
        if self.get_type() != srcMLResult.STRING:
            raise srcMLInvalidResultType()
        rtn = libsrcml.srcml_transform_get_string(self.c_res)
        return rtn.decode() if rtn else None

    # -------------------------------------------------------------------------------------------
    # Return: The transformation result number
    # -------------------------------------------------------------------------------------------
    def get_number() -> float:
        if self.get_type() != srcMLResult.NUMBER:
            raise srcMLInvalidResultType()
        return libsrcml.srcml_transform_get_number(self.c_res)

    # -------------------------------------------------------------------------------------------
    # Return: The transformation result number
    # -------------------------------------------------------------------------------------------
    def get_bool() -> bool:
        if self.get_type() != srcMLResult.BOOLEAN:
            raise srcMLInvalidResultType()
        return bool(libsrcml.srcml_transform_get_bool(self.c_res))