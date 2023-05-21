
from typing import Union, List, Dict, Type
from .. import Validator, ValidatorReturn, ValidatorError, ValidatorPath
from .list_validator import isinstance_validator_or_list_validators

def isinstance_dict_validator_format(dict_validator_format: object):
  if not isinstance(dict_validator_format, dict):
    return False
  
  if len(dict_validator_format) == 0:
    return False
  
  for d in dict_validator_format.values():
    if not isinstance_dict_validator_format(d) and not isinstance_validator_or_list_validators(d):
      return False

  return True


DictValidatorFormat = Dict[str, Union[Validator, List[Validator], Type['DictValidatorFormat']]]

class DictValidatorException(Exception):
  pass

class DictValidator(Validator):

  def __init__(self, dict_validator_format: DictValidatorFormat = None) -> None:
    if dict_validator_format != None  and not isinstance_dict_validator_format(dict_validator_format):
      raise DictValidatorException("The 'dict_validator_format' property must be None, a dictionary of Validator, or a dictionary of lists of Validator.")

    super().__init__()
    self.__dict_validator_format = dict_validator_format if dict_validator_format != None else {}

    
  def is_valid(self, data: object) -> ValidatorReturn:
    return self.__is_valid(data, self.__dict_validator_format)

  def __is_valid(
    self,
    data: object,
    validators: DictValidatorFormat
  ) -> ValidatorReturn:
    if not isinstance(data, dict):
      return ValidatorReturn(False, ValidatorError("Is not an instance of dict."))

    errors = []
    for att, wrapper_validators in validators.items():
      if att not in data:
        errors.append(
          ValidatorError(f"Key '{att}' does not exist in the dict")
        )
        continue
      
      sub_data = data.get(att, None)
    
      if isinstance(wrapper_validators, dict):

        is_valid, validator_errors = self.__is_valid(sub_data, wrapper_validators)
        if not is_valid:
          for e in validator_errors:
            errors.append(
              ValidatorError(message=e.message, path=ValidatorPath(att, *e.path))
            )
      
      elif isinstance(wrapper_validators, list):
        for validator in wrapper_validators:
          is_valid, validator_errors = validator.is_valid(sub_data)

          if not is_valid:
            for e in validator_errors:
              errors.append(
                ValidatorError(message=e.message, path=ValidatorPath(att, *e.path))
              )
          
      else:
        validator = wrapper_validators
        is_valid, validator_errors = validator.is_valid(sub_data)

        if not is_valid:
          for e in validator_errors:
            errors.append(
              ValidatorError(message=e.message, path=ValidatorPath(att, *e.path))
            )
        
    if len(errors) == 0:
      return ValidatorReturn(True)
    
    return ValidatorReturn(False, errors)