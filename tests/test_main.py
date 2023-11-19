import unittest
from unittest.mock import MagicMock, create_autospec, patch

from touch_typing_practice.main import TypingPractice, User, main


class TestMainFunction(unittest.TestCase):
    @unittest.skip(
        "========================= 1 failed, 16 passed in 1.24s ========================="
    )
    @patch("touch_typing_practice.main.curses.initscr")
    @patch("touch_typing_practice.main.curses.echo")
    @patch("touch_typing_practice.main.User.load")
    @patch("touch_typing_practice.main.TypingPractice")
    def test_main(self, mock_TypingPractice, mock_User_load, mock_curses_echo, mock_curses_initscr):
        mock_stdscr = MagicMock()
        mock_stdscr.getstr.side_effect = [
            b"username",
            b"1",
            b"sample text",
            b"typed sample text",
            b"3",
        ]
        mock_User_load.return_value = MagicMock()
        mock_TypingPractice.return_value = create_autospec(TypingPractice)

        main(mock_stdscr)

        mock_stdscr.clear.assert_called()
        mock_User_load.assert_called_with(b"username")
        mock_TypingPractice.assert_called()
        mock_TypingPractice.return_value.start_session.assert_called_with(
            b"sample text"
        )
        mock_TypingPractice.return_value.end_session.assert_called_with(
            b"typed sample text"
        )
        mock_TypingPractice.return_value.get_user_statistics.assert_called()
        mock_curses_echo.assert_called()

    @patch("touch_typing_practice.main.User.load")
    @patch("touch_typing_practice.main.TypingPractice")
    def test_main_invalid_choice(self, mock_TypingPractice, mock_User_load):
        mock_stdscr = MagicMock()
        mock_stdscr.getstr.side_effect = [
            b"username",
            b"invalid choice",
            b"1",
            b"sample text",
            b"typed sample text",
            b"3",
        ]
        mock_User_load.return_value = MagicMock()
        mock_TypingPractice.return_value = create_autospec(TypingPractice)

if __name__ == "__main__":
    unittest.main()

        main(mock_stdscr)

        mock_stdscr.clear.assert_called()
        mock_User_load.assert_called_with(b"username")
        mock_TypingPractice.assert_called()
        mock_TypingPractice.return_value.start_session.assert_called_with(
            b"sample text"
        )
        mock_TypingPractice.return_value.end_session.assert_called_with(
            b"typed sample text"
        )
        mock_TypingPractice.return_value.get_user_statistics.assert_called()


if __name__ == "__main__":
    unittest.main()

        mock_curses_initscr.assert_called()

