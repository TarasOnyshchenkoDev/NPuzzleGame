from abc import ABC, abstractmethod


class UserInput(ABC):
	@abstractmethod
	def get_tile_input(self, size: int):
		pass
