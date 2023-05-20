import pytest

from wvalidate import Validator, ValidatorReturn, ValidatorError
from wvalidate.validators.integer_validator import IntegerValidator, IntegerValidatorException

def get_error_is_not_integer() -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError("Is not an instance of int.")) 

def get_error_less_than(min: int) -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError(f"The data provided is less than {min}.")) 

def get_error_greater_than(max: int) -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError(f"The data provided is greater than {max}."))

def get_error_range(min: int, max: int) -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError(f"The data provided is not within the range of {min} to {max}.")) 


def test_integer_validator_is_instance_validator():
	assert issubclass(IntegerValidator, Validator) == True
  

@pytest.mark.parametrize("n", [1.0, "125", True, False, [1], [""]])
def test_integer_validator_with_min_max_invalid(n):           
	with pytest.raises(IntegerValidatorException):
		IntegerValidator(min=n)
	
	with pytest.raises(IntegerValidatorException):
		IntegerValidator(max=n)
   
@pytest.mark.parametrize("min, max", [
	(3, 1),
	(-1, -15),
	(50, -1),
	(49, 48),
])
def test_integer_validator_with_range_min_max_invalid(min, max):           
	with pytest.raises(IntegerValidatorException):
		IntegerValidator(min=min, max=max)
	


def test_integer_validator_validate():
	assert IntegerValidator().is_valid(1) == ValidatorReturn(True)
	assert IntegerValidator().is_valid(-100) == ValidatorReturn(True)
	assert IntegerValidator().is_valid(200) == ValidatorReturn(True)

	assert IntegerValidator().is_valid("1") == get_error_is_not_integer()
	assert IntegerValidator().is_valid(None) == get_error_is_not_integer()
	assert IntegerValidator().is_valid(True) == get_error_is_not_integer()
	assert IntegerValidator().is_valid(False) == get_error_is_not_integer()
	assert IntegerValidator().is_valid([121]) == get_error_is_not_integer()
	assert IntegerValidator().is_valid({}) == get_error_is_not_integer()

def test_integer_validator_validate_min():
	assert IntegerValidator(min=1).is_valid(1) == ValidatorReturn(True)
	assert IntegerValidator(min=-100).is_valid(-100) == ValidatorReturn(True)
	assert IntegerValidator(min=-800).is_valid(-100) == ValidatorReturn(True)
	assert IntegerValidator(min=10).is_valid(200) == ValidatorReturn(True)

	assert IntegerValidator(min=1).is_valid(0) == get_error_less_than(1)
	assert IntegerValidator(min=-100).is_valid(-101) == get_error_less_than(-100)
	assert IntegerValidator(min=-80).is_valid(-100) == get_error_less_than(-80)
	assert IntegerValidator(min=1000).is_valid(200) == get_error_less_than(1000)

def test_integer_validator_validate_max():
	assert IntegerValidator(max=1).is_valid(1) == ValidatorReturn(True)
	assert IntegerValidator(max=-100).is_valid(-100) == ValidatorReturn(True)
	assert IntegerValidator(max=80).is_valid(-100) == ValidatorReturn(True)
	assert IntegerValidator(max=10).is_valid(-200) == ValidatorReturn(True)

	assert IntegerValidator(max=1).is_valid(2) == get_error_greater_than(1)
	assert IntegerValidator(max=-100).is_valid(-99) == get_error_greater_than(-100)
	assert IntegerValidator(max=-800).is_valid(-100) == get_error_greater_than(-800)
	assert IntegerValidator(max=1000).is_valid(2000) == get_error_greater_than(1000)

def test_integer_validator_validate_range_min_and_max():
	assert IntegerValidator(min=1, max=1).is_valid(1) == ValidatorReturn(True)
	assert IntegerValidator(min=0, max=100).is_valid(0) == ValidatorReturn(True)
	assert IntegerValidator(min=0, max=100).is_valid(100) == ValidatorReturn(True)
	assert IntegerValidator(min=0, max=100).is_valid(50) == ValidatorReturn(True)
	assert IntegerValidator(min=-15, max=-5).is_valid(-15) == ValidatorReturn(True)
	assert IntegerValidator(min=-15, max=-5).is_valid(-5) == ValidatorReturn(True)
	assert IntegerValidator(min=-15, max=-5).is_valid(-10) == ValidatorReturn(True)

	assert IntegerValidator(min=1, max=1).is_valid(2) == get_error_range(min=1, max=1)
	assert IntegerValidator(min=1, max=1).is_valid(0) == get_error_range(min=1, max=1)
	assert IntegerValidator(min=0, max=100).is_valid(-1) == get_error_range(min=0, max=100)
	assert IntegerValidator(min=0, max=100).is_valid(101) == get_error_range(min=0, max=100)
	assert IntegerValidator(min=-15, max=-5).is_valid(-156) == get_error_range(min=-15, max=-5)
	assert IntegerValidator(min=-15, max=-5).is_valid(-4) == get_error_range(min=-15, max=-5)