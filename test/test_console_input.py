import unittest
from io import StringIO
from unittest.mock import patch
from input.console_input import ConsoleInput

class ConsoleInputTest(unittest.TestCase):

    @patch('builtins.input')
    def test_get_tile_input_valid(self, mock_input):
        mock_input.side_effect = ['4']
        console_input = ConsoleInput()
        tile= console_input.get_tile_input(9)
        self.assertEqual(tile, 4)


    @patch('sys.stdout', new=StringIO())
    @patch('builtins.input')
    def test_get_tile_input_invalid(self, mock_input):
        mock_input.side_effect = ['a','12','3']
        console_input = ConsoleInput()
        tile = console_input.get_tile_input(9)
        self.assertEqual(tile, 3)


if __name__ == '__main__':
    unittest.main()
