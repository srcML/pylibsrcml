# SPDX-License-Identifier: GPL-3.0-only
"""
@file srcml_transform_result.py

@copyright Copyright (C) 2014-2025 srcML, LLC. (www.srcML.org)

This file is part of pylibsrcml, a Python binding of libsrcml
"""

from .globals import libsrcml
from .values import srcMLStatus, srcMLResult
from .exceptions import srcMLTypeError, srcMLInvalidResultType, check_srcml_status
from .srcml_unit import srcMLUnit

from ctypes import c_int, c_long, c_size_t, c_void_p

class srcMLTransformResult:
    def __init__(self, res_ptr: int = 0):
        """Create a new srcml_transform_unit"""
        if type(res_ptr) != int:
            raise srcMLTypeError(self.__init__,"res_ptr",res_ptr)
        self.c_res = c_size_t(res_ptr)

    def __del__(self):
        """Free the resources in a tranformation result."""
        if self.c_res.value != 0 and self.c_res.value != None:
            libsrcml.srcml_transform_free(self.c_res)

    def get_type(self) -> int:
        """Return: An int representing the transform type"""
        return libsrcml.srcml_transform_get_type(self.c_res.value)

    def get_unit_size(self) -> int:
        """Return: The number of units in the transformation result"""
        if self.get_type() != srcMLResult.UNITS:
            raise srcMLInvalidResultType()
        return libsrcml.srcml_transform_get_unit_size(self.c_res)

    def __len__(self) -> int:
        """Return: The number of units in the transformation result | identical to get_unit_size"""
        return self.get_unit_size()

    def __iter__(self):
        """iter function for working with for loops"""
        if self.get_type() != srcMLResult.UNITS:
            raise srcMLInvalidResultType()
        for i in range(self.get_unit_size()):
            yield self.get_unit(i)

    def get_unit(self, i: int) -> srcMLUnit:
        """Return: The unit at index i"""
        if type(i) != int:
            raise srcMLTypeError(self.get_unit,"i",i)
        if self.get_type() != srcMLResult.UNITS:
            raise srcMLInvalidResultType()
        rtn = libsrcml.srcml_transform_get_unit(self.c_res.value,i)
        if rtn == 0:
            raise srcMLException(srcMLStatus.ERROR)
        return srcMLUnit(rtn,False)

    def __getitem__(self, i: int) -> srcMLUnit:
        """Return: The unit at index i | Identical to get_unit"""
        if type(i) != int:
            raise srcMLTypeError(self.get_unit,"i",i)
        if self.get_type() != srcMLResult.UNITS:
            raise srcMLInvalidResultType()
        rtn = libsrcml.srcml_transform_get_unit(self.c_res.value,i)
        if rtn == 0:
            raise srcMLException(srcMLStatus.ERROR)
        return srcMLUnit(rtn,False)

    def is_unit_result(self) -> bool:
        """Return: True if the result type is UNITS"""
        return self.get_type() == srcMLResult.UNITS

    def get_units(self) -> list[srcMLUnit]:
        """Return: The list of units in the result"""
        if self.get_type() != srcMLResult.UNITS:
            raise srcMLInvalidResultType()
        array = []
        for i in range(self.get_unit_size()):
            array.append(self.get_unit(i))
        return array

    def get_string(self) -> str:
        """Return: The trasnformation result string"""
        if self.get_type() != srcMLResult.STRING:
            raise srcMLInvalidResultType()
        rtn = libsrcml.srcml_transform_get_string(self.c_res.value)
        return rtn.decode() if rtn else ""

    def is_string_result(self) -> bool:
        """Return: True if the result type is STRING"""
        return self.get_type() == srcMLResult.STRING

    def get_number(self) -> float:
        """Return: The transformation result number"""
        if self.get_type() != srcMLResult.NUMBER:
            raise srcMLInvalidResultType()
        return libsrcml.srcml_transform_get_number(self.c_res.value)

    def is_number_result(self) -> bool:
        """Return: True if the result type is NUMBER"""
        return self.get_type() == srcMLResult.NUMBER

    def get_bool(self) -> bool:
        """Return: The transformation result number"""
        if self.get_type() != srcMLResult.BOOLEAN:
            raise srcMLInvalidResultType()
        return bool(libsrcml.srcml_transform_get_bool(self.c_res.value))

    def is_bool_result(self) -> bool:
        """Return: True if the result type is BOOLEAN"""
        return self.get_type() == srcMLResult.BOOLEAN

    def get_value(self) -> list[srcMLUnit] | str | float | bool | None:
        """Return: The result, regardless of type"""
        type = self.get_type()
        if type == srcMLResult.UNITS:
            return self.get_units()
        elif type == srcMLResult.STRING:
            return self.get_string()
        elif type == srcMLResult.NUMBER:
            return self.get_number()
        elif type == srcMLResult.BOOLEAN:
            return self.get_bool()
        else:
            return None
