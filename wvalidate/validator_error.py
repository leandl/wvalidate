from __future__ import annotations

from .validator_path import ValidatorPath

class ValidatorErrorException(Exception):
	pass

class ValidatorError:
	def __init__(self, message: str, path: ValidatorPath = None) -> None:
		if not isinstance(message, str):
			raise ValidatorErrorException("The \"message\" property must be an instance of str")
		
		if not isinstance(path, ValidatorPath) and path is not None:
			raise ValidatorErrorException("The \"path\" property must be an instance of ValidatorPath or None")
		
		self.message = message
		self.path = path if path else ValidatorPath()
	
	def __repr__(self) -> str:
		return f"ValidatorError(messae='{self.message}', path={self.path})"
	
	def __eq__(self, error: object) -> bool:
		if not isinstance(error, (str, ValidatorError)):
			return False
		
		if isinstance(error, str):
			return self.message == error
		
		if isinstance(error, ValidatorError):
			if self.message != error.message:
				return False
			
			return self.path == error.path
		
	def values(self):
		return {
			"message": self.message,
			"path": self.path.values()
		}
