## test_main.py
import unittest
from unittest.mock import patch
from touch_typing_practice.main import main
from touch_typing_practice.user import User
from touch_typing_practice.typing_practice import TypingPractice

class TestMain(unittest.TestCase):
    ## Test user input
    @patch('builtins.input', side_effect=['test_user', '1', 'test_text', 'typed_text', '3'])
    def test_main(self, mock_input):
        with patch('curses.wrapper') as mock_curses:
            main(mock_curses)
            self.assertEqual(mock_input.call_count, 5)
    
    ## Test invalid choice
    @patch('builtins.input', side_effect=['test_user', '4', '3'])
    def test_invalid_choice(self, mock_input):
        with patch('curses.wrapper') as mock_curses:
            main(mock_curses)
            self.assertEqual(mock_input.call_count, 3)

    ## Test ValueError on choice
    @patch('builtins.input', side_effect=['test_user', 'not_a_number', '3'])
    def test_value_error_choice(self, mock_input):
        with patch('curses.wrapper') as mock_curses:
            main(mock_curses)
            self.assertEqual(mock_input.call_count, 3)

    ## Test statistics
    @patch('builtins.input', side_effect=['test_user', '2', '3'])
    def test_statistics(self, mock_input):
        with patch('curses.wrapper') as mock_curses:
            main(mock_curses)
            self.assertEqual(mock_input.call_count, 3)

if __name__ == "__main__":
    unittest.main()
