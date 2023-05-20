import pytest
from typing import Union

from wvalidate import Validator, ValidatorReturn, ValidatorError
from wvalidate.validators.float_validator import FloatValidator, FloatValidatorException

def get_error_is_not_float() -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError("Is not an instance of float.")) 

def get_error_less_than(min: Union[int, float]) -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError(f"The data provided is less than {min}.")) 

def get_error_greater_than(max: Union[int, float]) -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError(f"The data provided is greater than {max}."))

def get_error_range(min: Union[int, float], max: Union[int, float]) -> ValidatorReturn:
	return ValidatorReturn(False, ValidatorError(f"The data provided is not within the range of {min} to {max}.")) 


def test_float_validator_is_instance_validator():
	assert issubclass(FloatValidator, Validator) == True
  

@pytest.mark.parametrize("n", ["125", True, False, [1], [""]])
def test_float_validator_with_min_max_invalid(n):           
	with pytest.raises(FloatValidatorException):
		FloatValidator(min=n)
	
	with pytest.raises(FloatValidatorException):
		FloatValidator(max=n)
   
@pytest.mark.parametrize("min, max", [
	(3, 1.15),
	(-1, -15),
	(50.5, -1),
	(49, 48.9),
])
def test_float_validator_with_range_min_max_invalid(min, max):           
	with pytest.raises(FloatValidatorException):
		FloatValidator(min=min, max=max)
	


def test_float_validator_validate():
	assert FloatValidator().is_valid(1.0) == ValidatorReturn(True)
	assert FloatValidator().is_valid(-100.15) == ValidatorReturn(True)
	assert FloatValidator().is_valid(200.9) == ValidatorReturn(True)

	assert FloatValidator().is_valid("1") == get_error_is_not_float()
	assert FloatValidator().is_valid(None) == get_error_is_not_float()
	assert FloatValidator().is_valid(True) == get_error_is_not_float()
	assert FloatValidator().is_valid(False) == get_error_is_not_float()
	assert FloatValidator().is_valid([121]) == get_error_is_not_float()
	assert FloatValidator().is_valid({}) == get_error_is_not_float()

def test_float_validator_validate_min():
	assert FloatValidator(min=1).is_valid(1.0) == ValidatorReturn(True)
	assert FloatValidator(min=-100.5).is_valid(-100.5) == ValidatorReturn(True)
	assert FloatValidator(min=-800).is_valid(-799.9) == ValidatorReturn(True)
	assert FloatValidator(min=10).is_valid(200.56) == ValidatorReturn(True)

	assert FloatValidator(min=1).is_valid(0.0) == get_error_less_than(1)
	assert FloatValidator(min=-100.21).is_valid(-100.22) == get_error_less_than(-100.21)
	assert FloatValidator(min=-80).is_valid(-100.45) == get_error_less_than(-80)
	assert FloatValidator(min=1000.38).is_valid(200.5) == get_error_less_than(1000.38)

def test_float_validator_validate_max():
	assert FloatValidator(max=1).is_valid(1.0) == ValidatorReturn(True)
	assert FloatValidator(max=-100.0).is_valid(-100.0) == ValidatorReturn(True)
	assert FloatValidator(max=80).is_valid(-100.12) == ValidatorReturn(True)
	assert FloatValidator(max=10).is_valid(-200.3) == ValidatorReturn(True)

	assert FloatValidator(max=1).is_valid(1.1) == get_error_greater_than(1)
	assert FloatValidator(max=-100.0).is_valid(-99.9) == get_error_greater_than(-100.0)
	assert FloatValidator(max=-800).is_valid(-100.5) == get_error_greater_than(-800)
	assert FloatValidator(max=1000.23).is_valid(2000.0) == get_error_greater_than(1000.23)

def test_float_validator_validate_range_min_and_max():
	assert FloatValidator(min=1, max=1).is_valid(1.0) == ValidatorReturn(True)
	assert FloatValidator(min=0, max=100).is_valid(0.0) == ValidatorReturn(True)
	assert FloatValidator(min=0.0, max=100).is_valid(100.0) == ValidatorReturn(True)
	assert FloatValidator(min=0, max=100).is_valid(50.1) == ValidatorReturn(True)
	assert FloatValidator(min=-15, max=-5).is_valid(-15.0) == ValidatorReturn(True)
	assert FloatValidator(min=-15, max=-5).is_valid(-5.0) == ValidatorReturn(True)
	assert FloatValidator(min=-15.52, max=-5).is_valid(-10.12) == ValidatorReturn(True)

	assert FloatValidator(min=1, max=1.9).is_valid(2.0) == get_error_range(min=1, max=1.9)
	assert FloatValidator(min=0.9, max=1).is_valid(0.8) == get_error_range(min=0.9, max=1)
	assert FloatValidator(min=0, max=100).is_valid(-1.1) == get_error_range(min=0, max=100)
	assert FloatValidator(min=0, max=100.36).is_valid(101.9) == get_error_range(min=0, max=100.36)
	assert FloatValidator(min=-15, max=-5).is_valid(-156.5) == get_error_range(min=-15, max=-5)
	assert FloatValidator(min=-15.15, max=-5).is_valid(-4.12) == get_error_range(min=-15.15, max=-5)