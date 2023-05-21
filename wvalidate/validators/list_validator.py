from __future__ import annotations
from typing import Optional, Union, List

from .. import Validator, ValidatorReturn, ValidatorError, ValidatorPath

def isinstance_validator_or_list_validators(validators: object):
	if isinstance(validators, Validator):
		return True
	
	if not isinstance(validators, list):
		return False
	
	if len(validators) == 0:
		return False
	
	for validator in validators:
		if not isinstance(validator, Validator):
			return False
	
	return True


class ListValidatorException(Exception):
  pass

class ListValidator(Validator):
    
  def __init__(self, validators: Optional[Union[Validator, List[Validator]]] = None) -> None:
    if validators != None and not isinstance_validator_or_list_validators(validators):
      raise ListValidatorException("The \"validators\" property must be None, Validator or list of Validator.")
			
    super().__init__()
    if validators == None:
      self.__validators = []
    else:
      self.__validators = validators if isinstance(validators, list) else [validators]
        

  
  def is_valid(self, data: object) -> ValidatorReturn:
    if not isinstance(data, list):
      return ValidatorReturn(False, ValidatorError("Is not an instance of list."))
  
    errors = []
    for index, d in enumerate(data):
      for validator in self.__validators:
        is_valid, validator_errors = validator.is_valid(d)

        if not is_valid:
          for e in validator_errors:
            errors.append(
              ValidatorError(message=e.message, path=ValidatorPath(index, *e.path))
            )
    
    if len(errors) == 0:
      return ValidatorReturn(True)
    
    return ValidatorReturn(False, errors)