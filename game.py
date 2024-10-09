from board import Board
from display.display import Display
from input.user_input import UserInput


class GameLogic:
	def __init__(self, board: Board, display: Display, user_input: UserInput):
		self.board = board
		self.display = display
		self.user_input = user_input

	def play(self):
		print(f"Welcome to {self.board.size} Puzzle!")
		while not self.board.is_solved():
			self.display.show_board(self.board)
			tile = self.user_input.get_tile_input(self.board.size)
			if not self.board.move_tile(tile):
				print("Invalid move. Try again.")
		print("Congratulations! You've solved the puzzle!")
		self.display.show_board(self.board)
