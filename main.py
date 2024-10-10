from board import Board
from display.console_display import ConsoleDisplay
from game import GameLogic
from input.console_input import ConsoleInput

if __name__ == "__main__":
	board = Board(3)
	display = ConsoleDisplay()
	user_input = ConsoleInput()
	game = GameLogic(board, display, user_input)
	game.play()
