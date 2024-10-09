from input.user_input import UserInput


class ConsoleInput(UserInput):
	def get_tile_input(self, size: int):
		while True:
			try:
				tile = int(input(f"Enter number to move tile (1-{size - 1}): "))
				if tile in range(1, size):
					return tile
				print(f"Invalid number. Please enter a number between 1 and {size - 1}.")
			except ValueError:
				print("Invalid input. Please enter a number.")
