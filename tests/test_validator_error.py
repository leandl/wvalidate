import pytest
from wvalidate.validator_error import ValidatorError, ValidatorErrorException
from wvalidate.validator_path import ValidatorPath

@pytest.mark.parametrize("message", [None, True, False, list(), 1, 1.3])
def test_validator_error_with_message_invalid(message): 
	with pytest.raises(ValidatorErrorException):
		ValidatorError(message)
			
@pytest.mark.parametrize("path", ["str", True, False, list(), dict(), 1, 1.3])
def test_validator_error_with_invalid_path(path): 
	with pytest.raises(ValidatorErrorException):
		ValidatorError('message', path)
		

def test_validator_error_intance(): 
	validator_error_without_path = ValidatorError('message')
	assert validator_error_without_path.message == 'message'
	assert validator_error_without_path.path == ValidatorPath()
	
	validator_error_without_path_again = ValidatorError('message', None)
	assert validator_error_without_path_again.message == 'message'
	assert validator_error_without_path_again.path == ValidatorPath()

	validator_error_with_path = ValidatorError('message', ValidatorPath("test", 1))
	assert validator_error_with_path.message == 'message'
	assert validator_error_with_path.path == ValidatorPath("test", 1)
	


def test_validator_error_equal_str():
	assert ValidatorError("message_error") == "message_error"
	assert ValidatorError("message_error_1") == "message_error_1"
	assert ValidatorError("message_error_2") == "message_error_2"


	assert ValidatorError("message_error") != "message_error_2"
	assert ValidatorError("message_error_1") != "message_error"
	assert ValidatorError("message_error_2") != "message_error_1"


def test_validator_error_equal_other_validator_error():
	assert ValidatorError("message_error") == ValidatorError("message_error")
	assert ValidatorError("message_error") == ValidatorError("message_error", ValidatorPath())
	assert ValidatorError("message_error_1", ValidatorPath("user")) == ValidatorError("message_error_1", ValidatorPath("user"))
	assert ValidatorError("message_error_2", ValidatorPath(0, "age")) == ValidatorError("message_error_2", ValidatorPath(0, "age"))


	assert ValidatorError("message_error") != ValidatorError("message_error_2")
	assert ValidatorError("message_error") != ValidatorError("message_error_2", ValidatorPath())
	assert ValidatorError("message_error") != ValidatorError("message_error", ValidatorPath("user"))
	assert ValidatorError("message_error", ValidatorPath(0)) != ValidatorError("message_error", ValidatorPath(0, "age"))
	