import unittest
from os.path import pathsep
from unittest.mock import patch

import board
from board import Board

class BoardTest(unittest.TestCase):
	def setUp(self):
		self.dimension=3
		self.board = Board(self.dimension)


	def test_init_board_creates_solvable_board(self):
		board = Board(self.dimension)
		self.assertTrue(board.is_solvable())

	def test_board_is_solvable_true(self):
		self.board.board=[1,2,3,4,5,6,7,8,0]
		self.assertTrue(self.board.is_solvable())

	def test_board_is_solvable_false(self):
		self.board.board=[1,2,3,5,4,6,7,8,0]
		self.assertFalse(self.board.is_solvable())

	def test_board_is_solved_valid(self):
		self.board.board=[1,2,3,4,5,6,7,8,0]
		self.assertTrue(self.board.is_solved())

	def test_board_is_solved_invalid(self):
		self.board.board=[1,2,3,4,5,6,7,0,8]
		self.assertFalse(self.board.is_solved())

	def test_move_tile_valid(self):
		self.board.board=[1,2,3,4,5,6,7,0,8]
		self.board.empty_tile=(1,2)
		is_moved=self.board.move_tile(8)
		self.assertTrue(is_moved)
		self.assertEqual(self.board.board,[1,2,3,4,5,6,7,8,0])

	def test_move_tile_invalid(self):
		self.board.board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
		self.board.empty_tile = (1, 2)
		is_moved = self.board.move_tile(3)
		self.assertFalse(is_moved)
		self.assertEqual(self.board.board, [1, 2, 3, 4, 5, 6, 7, 0, 8])

if __name__ == '__main__':
	unittest.main()
