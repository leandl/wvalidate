from __future__ import annotations
from ..validator import Validator, ValidatorReturn

class NullableValidatorException(Exception):
  pass

class NullableValidator(Validator):
    
  def __init__(
    self,
    validator: Validator = None
  ) -> None:
    if not isinstance(validator, Validator):
      raise NullableValidatorException("Expected a Validator")

    super().__init__()
    self.__validator = validator
        

  
  def is_valid(self, data) -> ValidatorReturn:
    if data is None:
      return ValidatorReturn(True)
  
    return self.__validator.is_valid(data)