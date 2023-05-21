import pytest

from wvalidate import Validator, ValidatorReturn, ValidatorError
from wvalidate.validators.enum_validator import EnumValidator, EnumValidatorException


def test_enum_validator_is_instance_validator():
	assert issubclass(EnumValidator, Validator) == True
  
def test_enum_validator_without_a_list_of_options_2_items():           
	with pytest.raises(EnumValidatorException):
		EnumValidator()
	
	with pytest.raises(EnumValidatorException):
		EnumValidator([])

	TEST_WITHOUT_LIST_WITH_2_ITEMS = ["TEST"]
	with pytest.raises(EnumValidatorException):
		EnumValidator(TEST_WITHOUT_LIST_WITH_2_ITEMS)    

	
def test_enum_validator_not_validate():
	TESTS = [
		(["ACTIVE", "DELETED"], "OK"),
		([2, 3, 5], 7),
		([False, True], None),
		([None, "DELETED", 1], False),
	]

	for test, data in TESTS:
		validator_return = ValidatorReturn(False, ValidatorError(f"Is not among the options. {test}"))
		assert EnumValidator(test).is_valid(data) == validator_return


def test_enum_validator_validate():
	TESTS = [
		(["ACTIVE", "DELETED"], "ACTIVE"),
		(["ACTIVE", "DELETED"], "DELETED"),
		([2, 3, 5], 2),
		([False, True, None], None),
		([None, "DELETED", 1], 1),
		([41, None, 15, "DELETED", 31], 15),
	]

	for test, data in TESTS:
		validator_return = ValidatorReturn(True)
		assert EnumValidator(test).is_valid(data) == validator_return
