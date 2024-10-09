from abc import ABC, abstractmethod

from board import Board


class Display(ABC):
	@abstractmethod
	def show_board(self, board: Board):
		pass
