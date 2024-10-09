from board import Board
from display.display import Display


class ConsoleDisplay(Display):
	def show_board(self, board: Board):
		for i in range(board.dimension):
			row = board.board[i * board.dimension: (i + 1) * board.dimension]
			print(' '.join(f"{num:2}" if num != 0 else '  ' for num in row))
		print()
