from __future__ import annotations
from typing import List, Union

from .validator_error import ValidatorError

def isinstance_validator_error_or_list_validator_errors(errors: object):
	if isinstance(errors, ValidatorError):
		return True
	
	if not isinstance(errors, list):
		return False
	
	if len(errors) == 0:
		return False
	
	for error in errors:
		if not isinstance(error, ValidatorError):
			return False
	
	return True


class ValidatorReturnException(Exception):
	pass

class ValidatorReturn:
	def __init__(self, success: bool, errors: Union[ValidatorError, List[ValidatorError]] = None) -> None:

		if not isinstance(success, bool):
			raise ValidatorReturnException("The \"success\" property must be an instance of bool")
		
		if success:
			if errors is not None:
				raise ValidatorReturnException("The \"errors\" property must be None, when the \"success\" property is True")
			
			self._success = True
			self._errors = None
		else:
			if not isinstance_validator_error_or_list_validator_errors(errors):
				raise ValidatorReturnException("The \"errors\" property must be ValidatorError or list of ValidatorError, when the \"success\" property is False")
			
			self._success = False
			self._errors = errors if isinstance(errors, list) else [errors]


	@property
	def success(self):
		return self._success
	
	@property
	def errors(self):
		return self._errors

	def keys(self):
		return ["success", "errors"]
                
	def __getitem__(self, key: str):
		if key == "success":
			return self.success
		
		if key == "errors":
			return self.errors
	
		raise ValidatorReturnException(f"{key}: property does not exist")
	
	def __eq__(self, _return: object) -> bool:
		if not isinstance(_return, ValidatorReturn):
			return False
		
		if self.success != _return.success:
			return False
		
		if self.success == True:
			return True
		
		if len(self.errors) != len(_return.errors):
			return False
		
		for self_error, _return_error in zip(self.errors, _return.errors):
			if self_error != _return_error:
				return False
		
		return True

	def __iter__(self):
		yield self.success
		yield self.errors

	def __repr__(self) -> str:
		return f"({self.success}, {self.errors})"
	
	def __bool__(self) -> bool:
		return bool(self.success)

	def values(self):
		if self.success:
			return {
				"success": True,
				"errors": None
			}
		
		return {
			"success": False,
			"errors": [ error.values() for error in self.errors ]
		}