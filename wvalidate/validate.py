from typing import Optional, Union, List

from .validator import Validator

from .validators.integer_validator import IntegerValidator
from .validators.float_validator import FloatValidator
from .validators.numeric_validator import NumericValidator
from .validators.string_validator import StringValidator
from .validators.email_validator import EmailValidator
from .validators.enum_validator import EnumValidator
from .validators.nullable_validator import NullableValidator
from .validators.list_validator import ListValidator
from .validators.dict_validator import DictValidator, DictValidatorFormat

class Validate: 
    
	@staticmethod
	def list(validators: Optional[Union[List[Validator], Validator]] = None) -> Validator:
		return ListValidator(validators)
    
	@staticmethod
	def dict(format_validate: DictValidatorFormat = None) -> Validator:
		return DictValidator(format_validate)

	@staticmethod
	def string(equal: Optional[str] = None, min: Optional[int] = None, max: Optional[int] = None) -> Validator:
		return StringValidator(equal=equal, min=min, max=max)

	@staticmethod
	def email() -> Validator:
		return EmailValidator()

	@staticmethod
	def nullable(validator: Validator) -> Validator:
		return NullableValidator(validator)

	@staticmethod
	def numeric(min: Optional[Union[int, float]] = None, max: Optional[Union[int, float]] = None) -> Validator:
		return NumericValidator(min=min, max=max)

	@staticmethod
	def float(min: Optional[Union[int, float]] = None, max: Optional[Union[int, float]] = None) -> Validator:
		return FloatValidator(min=min, max=max)

	@staticmethod
	def integer(min: Optional[int] = None, max: Optional[int] = None) -> Validator:
		return IntegerValidator(min=min, max=max)

	@staticmethod
	def enum(options: List) -> Validator:
		return EnumValidator(options)