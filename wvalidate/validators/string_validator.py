from __future__ import annotations
from typing import Optional
import re

from .. import Validator, ValidatorReturn, ValidatorError

class StringValidatorException(Exception):
  pass

class StringValidator(Validator):
    
  def __init__(
    self,
    equal: Optional[str] = None,
    min: Optional[int] = None,
    max: Optional[int] = None,
    regex: Optional[str] = None,
    message_error_invalid_regex: Optional[str] = None,
  ) -> None:
    if equal != None and not isinstance(equal, str):
      raise StringValidatorException("The \"equal\" property must be an instance of str")

    if min != None and (not isinstance(min, int) or isinstance(min, bool) or min < 0):
      raise StringValidatorException("The \"min\" property must be an instance of int and greater than or equal to zero.")
    
    if max != None and (not isinstance(max, int) or isinstance(max, bool) or max < 0):
      raise StringValidatorException("The \"max\" property must be an instance of int and greater than or equal to zero.")
    
    is_range = min != None and max != None
    if is_range and min > max:
      raise StringValidatorException("The \"min\" property must be less than or equal to the \"max\" property.")
    
    if regex != None and not isinstance(regex, str):
      raise StringValidatorException("The \"regex\" property must be an instance of str")
    
    if regex != None and not isinstance(message_error_invalid_regex, str):
      raise StringValidatorException("The \"message_error_invalid_regex\" property must be an instance of str when the \"regex\" property is provided.")

    super().__init__()
    self.__equal = equal
    self.__min = min
    self.__max = max

    self.__regex = re.compile(regex) if regex else None
    self.__message_error_invalid_regex = message_error_invalid_regex if regex else None

  
  def is_valid(self, data) -> ValidatorReturn:
    if not isinstance(data, str):
      return ValidatorReturn(False, ValidatorError("Is not an instance of str."))
    
    if self.__equal != None and self.__equal != data:
      return ValidatorReturn(False, ValidatorError(f"The data is not equal to '{self.__equal}'."))
    
    is_range = self.__min != None and self.__max != None
    if is_range:
      if self.__max >= len(data) >= self.__min:
        return ValidatorReturn(True)
      
      message_error = f"Data provided is not within the range of {self.__min} to {self.__max} characters."
      return ValidatorReturn(False, ValidatorError(message_error)) 
    
    if self.__min != None and self.__min > len(data):
      return ValidatorReturn(False, ValidatorError(f"The data provided is less than {self.__min} characters.")) 
    
    if self.__max != None and self.__max < len(data):
      return ValidatorReturn(False, ValidatorError(f"The data provided is greater than {self.__max} characters.")) 
    
    
    if self.__regex != None and not re.fullmatch(self.__regex, data):
      return ValidatorReturn(False, ValidatorError(self.__message_error_invalid_regex))
    
    return ValidatorReturn(True)
  
