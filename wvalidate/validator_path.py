from __future__ import annotations
from typing import Union

class ValidatorPathException(Exception):
	pass

class ValidatorPath:
	def __init__(self, *path: Union[str, int]) -> None:
		for p in path:
			if not isinstance(p, (str, int)) or isinstance(p, bool):
				raise ValidatorPathException("The \"path\" property must be an list of str or int")

		self.__path = path
	

	def __eq__(self, path: object) -> bool:
		if not isinstance(path, ValidatorPath):
			return False
		
		if len(self) != len(path):
			return False
		
		for self_sub_path, path_sub_path in zip(self, path):
			if self_sub_path != path_sub_path:
				return False
		
		return True


	def __add__(self, path: object):
		if isinstance(path, ValidatorPath):
			return ValidatorPath(*self, *path)
		
		path_type_name = path.__class__.__name__
		self_type_name = self.__class__.__name__
		raise ValidatorPathException(f"Unsupported operand type(s) for +: '{self_type_name}' and '{path_type_name}'")


	def __iter__(self):
		for p in self.__path:
			yield p

	def __len__(self):
		return len(self.__path)
	
	def __repr__(self) -> str:
		self_type_name = self.__class__.__name__
		path_str = list(self.__path).__str__()

		return f"{self_type_name}({path_str})"
	
	def values(self):
		return list(self.__path)
