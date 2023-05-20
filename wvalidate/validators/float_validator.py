from __future__ import annotations
from typing import Optional, Union
from .. import Validator, ValidatorReturn, ValidatorError


class FloatValidatorException(Exception):
  pass

class FloatValidator(Validator):
    
  def __init__(
    self,
    min: Optional[Union[int, float]] = None,
    max: Optional[Union[int, float]] = None,
  ) -> None:
    if min != None and (not isinstance(min, (int, float)) or isinstance(min, bool)):
      raise FloatValidatorException("The \"min\" property must be an instance of int or float")
    
    if max != None and (not isinstance(max, (int, float)) or isinstance(max, bool)):
      raise FloatValidatorException("The \"max\" property must be an instance of int or float")
    
    is_range = min != None and max != None
    if is_range and min > max:
      raise FloatValidatorException("The \"min\" property must be less than or equal to the \"max\" property.")
      
    super().__init__()
    self.__min = min
    self.__max = max

  
  def is_valid(self, data) -> ValidatorReturn:
    if not isinstance(data, float):
      return ValidatorReturn(False, ValidatorError("Is not an instance of float.")) 
    
    is_range = self.__min != None and self.__max != None
    if is_range:
      if self.__max >= data >= self.__min:
        return ValidatorReturn(True)
      
      message_error = f"The data provided is not within the range of {self.__min} to {self.__max}."
      return ValidatorReturn(False, ValidatorError(message_error)) 
    
    if self.__min != None and self.__min > data:
      return ValidatorReturn(False, ValidatorError(f"The data provided is less than {self.__min}.")) 
    
    if self.__max != None and self.__max < data:
      return ValidatorReturn(False, ValidatorError(f"The data provided is greater than {self.__max}.")) 
    
    return ValidatorReturn(True)