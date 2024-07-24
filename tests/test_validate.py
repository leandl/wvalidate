from wvalidate.validator import Validator
from wvalidate.validate import Validate as v
from wvalidate.validator_return import ValidatorReturn

class CustomValidator(Validator):
  def is_valid(self, _data: object) -> ValidatorReturn:
    return ValidatorReturn(True)

def test_nullable_validator_is_instance_validator():
	assert isinstance(v.dict(), Validator)
	assert isinstance(v.email(), Validator)
	assert isinstance(v.enum([1, 2]), Validator)
	assert isinstance(v.float(), Validator)
	assert isinstance(v.integer(), Validator)
	assert isinstance(v.list(), Validator)
	assert isinstance(v.nullable(CustomValidator()), Validator)
	assert isinstance(v.numeric(), Validator)
	assert isinstance(v.string(), Validator)
