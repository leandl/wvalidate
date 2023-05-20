from __future__ import annotations
from typing import Optional
from .. import Validator, ValidatorReturn, ValidatorError


class IntegerValidatorException(Exception):
  pass

class IntegerValidator(Validator):
    
  def __init__(
    self,
    min: Optional[int] = None,
    max: Optional[int] = None,
  ) -> None:
    if min != None and (not isinstance(min, int) or isinstance(min, bool)):
      raise IntegerValidatorException("The \"min\" property must be an instance of int")
    
    if max != None and (not isinstance(max, int) or isinstance(max, bool)):
      raise IntegerValidatorException("The \"max\" property must be an instance of int")
    
    is_range = min != None and max != None
    if is_range and min > max:
      raise IntegerValidatorException("The \"min\" property must be less than or equal to the \"max\" property.")
      
    super().__init__()
    self.__min = min
    self.__max = max

  
  def is_valid(self, data) -> ValidatorReturn:
    if not isinstance(data, int) or isinstance(data, bool):
      return ValidatorReturn(False, ValidatorError("Is not an instance of int.")) 
    
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