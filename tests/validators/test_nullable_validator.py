import pytest

from wvalidate import Validator, ValidatorReturn, ValidatorError
from wvalidate.validators.nullable_validator import NullableValidator, NullableValidatorException

class CustomValidator(Validator):
	def __init__(self, is_valid: bool) -> None:
		super().__init__()
		self.__is_valid = is_valid

	def is_valid(self, data: str) -> ValidatorReturn:
		if self.__is_valid:
			return ValidatorReturn(True)

		return ValidatorReturn(False, ValidatorError("INVALID"))
	

def test_nullable_validator_is_instance_validator():
	assert issubclass(NullableValidator, Validator) == True
  
def test_nullable_validator_without_a_list_of_options_2_items():           
	with pytest.raises(NullableValidatorException):
		NullableValidator()

	with pytest.raises(NullableValidatorException):
		NullableValidator("TEST") 
	
	with pytest.raises(NullableValidatorException):
		NullableValidator([])

	with pytest.raises(NullableValidatorException):
		NullableValidator(["OPTION1"])  
	 
	
def test_nullable_validator():
	custom_validator_valid = CustomValidator(True)
	custom_validator_invalid = CustomValidator(False)

	validator_with_custom_valid = NullableValidator(custom_validator_valid)
	validator_with_custom_invalid = NullableValidator(custom_validator_invalid)

	assert validator_with_custom_valid.is_valid(None) == ValidatorReturn(True)
	assert validator_with_custom_valid.is_valid("VALID") == ValidatorReturn(True)

	assert validator_with_custom_invalid.is_valid(None) == ValidatorReturn(True)
	assert validator_with_custom_invalid.is_valid("INVALID") == ValidatorReturn(False, ValidatorError("INVALID"))
