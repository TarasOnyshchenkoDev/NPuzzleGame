import random


class Board:
	def __init__(self, dimension: int):
		self.board = []
		self.empty_tile = None
		self.dimension = dimension
		self.size = dimension ** 2
		self.init_board()

	def init_board(self):
		for i in range(self.size):
			self.board.append(i)
		random.shuffle(self.board)
		if not self.is_solvable():
			# If not solvable, swap two adjacent non-empty tiles to make it solvable
			if self.board[0] != 0 and self.board[1] != 0:
				# Swap first two non-empty tiles
				self.board[0], self.board[1] = self.board[1], self.board[0]
			else:
				# Otherwise swap tiles at index 2 and 3
				self.board[2], self.board[3] = self.board[3], self.board[2]
		idx = 0
		for i in range(self.dimension):
			for j in range(self.dimension):
				if self.board[idx] == 0:
					self.empty_tile = (j, i)
					return
				idx += 1

	def is_solvable(self):
		inversions = 0
		for i in range(self.size):
			for j in range(i + 1, self.size):
				if self.board[i] and self.board[j] and self.board[i] > self.board[j]:
					inversions += 1
		if self.dimension % 2 == 0:
			empty_row = self.dimension - self.board.index(0) // self.dimension - 1
			if empty_row % 2 == 0:
				inversions += 1

		return inversions % 2 == 0

	# Moving tile to empty space
	def move_tile(self, tile):
		idx = self.board.index(tile)
		tile_y, tile_x = divmod(idx, self.dimension)
		empty_x, empty_y = self.empty_tile
		if abs(tile_x - empty_x) + abs(tile_y - empty_y) == 1:
			# Tile is adjacent; move it
			self.swap_tiles(tile_x, tile_y, empty_x, empty_y)
			self.empty_tile = (tile_x, tile_y)
			return True
		return False

	# Helper method to swap the tile with the empty tile
	def swap_tiles(self, x1, y1, x2, y2):
		idx1 = y1 * self.dimension + x1
		idx2 = y2 * self.dimension + x2
		self.board[idx1], self.board[idx2] = self.board[idx2], self.board[idx1]

	# Identify if puzzle solved
	def is_solved(self):
		correct_tiles = list(range(1, self.size)) + [0]
		return self.board == correct_tiles
