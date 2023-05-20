from __future__ import annotations
from abc import ABC, abstractmethod

from .validator_return import ValidatorReturn

class Validator(ABC):

	@abstractmethod
	def is_valid(self, _data: object) -> ValidatorReturn:
		"""
		Add validate for data
		"""
		pass