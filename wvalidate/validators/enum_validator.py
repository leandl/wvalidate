from __future__ import annotations
from typing import List, Any

from .. import Validator, ValidatorError, ValidatorReturn


class EnumValidatorException(Exception):
	pass

class EnumValidator(Validator):
    
	def __init__(self, options: List[Any] = None) -> None:
		if options == None or not isinstance(options, list) or len(options) < 2:
			raise EnumValidatorException("Expected a list of options with at least 2 items")

		super().__init__()
		self.__options = options
  
	def is_valid(self, data) -> ValidatorReturn:
		if data not in self.__options:
			return ValidatorReturn(False, ValidatorError(f"Is not among the options. {self.__options}"))
		
		return ValidatorReturn(True)