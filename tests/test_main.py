import unittest
from unittest.mock import MagicMock, patch

from touch_typing_practice.main import main


class TestMainFunction(unittest.TestCase):

    @patch("touch_typing_practice.main.User.load")
    @patch("touch_typing_practice.main.TypingPractice")
    def setUp(self, mock_typing_practice, mock_user_load):
        self.mock_stdscr = MagicMock()
        self.mock_stdscr.getstr.side_effect = [
            b"mock_username",  # username input
            b"1",              # choice to start new session
            b"mock_text",      # text for the session
            b"mock_typed_text",# typed text for the session
            b"2",              # choice to view statistics
            b"3"               # choice to exit
        ]
        
        self.mock_user_load = mock_user_load
        self.mock_user_load.return_value = MagicMock()
        
        self.mock_typing_practice = mock_typing_practice
        self.mock_typing_practice.return_value = MagicMock()
        self.mock_typing_practice.return_value.get_user_statistics.return_value = {
            "mock_time": {"wpm": 50, "accuracy": 90}
        }

    def test_main(self):
        main(self.mock_stdscr)

    @unittest.skip("========================= 1 failed, 16 passed in 1.13s =========================")
    def tearDown(self):
        pass



    @patch("touch_typing_practice.main.User.load")
    @patch("touch_typing_practice.main.TypingPractice")
    ================== 1 failed, 16 passed in 1.13s =========================")
    def tearDown(self):
        pass
    
    
    
    @patch("touch_typing_practice.main.User.load")
    @patch("touch_typing_practice.main.TypingPractice")
    @patch("curses.window.getstr")
    def setUp(self, mock_stdscr_getstr, mock_typing_practice, mock_user_load):
        self.mock_stdscr = MagicMock()
        self.mock_stdscr.getstr = mock_stdscr_getstr
        self.mock_stdscr.getstr.side_effect = [b"mock_username", b"1", b"mock_text", b"mock_typed_text", b"2", b"3"]
        
        self.mock_user_load = mock_user_load
        self.mock_user_load.return_value = MagicMock()
        
        self.mock_typing_practice = mock_typing_practice
        self.mock_typing_practice.return_value = MagicMock()
        self.mock_typing_practice.return_value.get_user_statistics.return_value = {"mock_time": {"wpm": 50, "accuracy": 90}}
    
    def test_main(self, mock_stdscr):
        main(mock_stdscr)
        mock_stdscr.clear.assert_called_once()
        self.mock_typing_practice.return_value.start_session.assert_called_once_with(b"mock_text")
        self.mock_typing_practice.return_value.end_session.assert_called_once_with(b"mock_typed_text")
    
    ================== 1 failed, 16 passed in 1.13s =========================")
    def tearDown(self):
    =======
    def tearDown(self):
        pass
    
    @patch("touch_typing_practice.main.User.load")
    @patch("touch_typing_practice.main.TypingPractice")
    @patch("curses.window.getstr")
    def setUp(self, mock_stdscr_getstr, mock_typing_practice, mock_user_load):
        self.mock_stdscr = MagicMock()
        self.mock_stdscr.getstr = mock_stdscr_getstr
        self.mock_stdscr.getstr.side_effect = [b"mock_username", b"1", b"mock_text", b"mock_typed_text", b"2", b"3"]
        
        self.mock_user_load = mock_user_load
        self.mock_user_load.return_value = MagicMock()
        
        self.mock_typing_practice = mock_typing_practice
        self.mock_typing_practice.return_value = MagicMock()
        self.mock_typing_practice.return_value.get_user_statistics.return_value = {"mock_time": {"wpm": 50, "accuracy": 90}}
    
    def test_main(self, mock_stdscr):
        main(mock_stdscr)
        mock_stdscr.clear.assert_called_once()
        self.mock_typing_practice.return_value.start_session.assert_called_once_with(b"mock_text")
        self.mock_typing_practice.return_value.end_session.assert_called_once_with(b"mock_typed_text")
    
    def tearDown(self):
        pass
    def setUp(self, mock_stdscr_getstr, mock_typing_practice, mock_user_load):
        self.mock_stdscr = MagicMock()
        self.mock_stdscr.getstr = mock_stdscr_getstr
        self.mock_stdscr.getstr.side_effect = [b"mock_username", b"1", b"mock_text", b"mock_typed_text", b"2", b"3"]
        
        self.mock_user_load = mock_user_load
        self.mock_user_load.return_value = MagicMock()
        
        self.mock_typing_practice = mock_typing_practice
        self.mock_typing_practice.return_value = MagicMock()
        self.mock_typing_practice.return_value.get_user_statistics.return_value = {"mock_time": {"wpm": 50, "accuracy": 90}}

    def test_main(self, mock_stdscr):
        main(mock_stdscr)
        mock_stdscr.clear.assert_called_once()
        self.mock_typing_practice.return_value.start_session.assert_called_once_with(b"mock_text")
        self.mock_typing_practice.return_value.end_session.assert_called_once_with(b"mock_typed_text")

    ================== 1 failed, 16 passed in 1.13s =========================")
    def tearDown(self):
        pass
    =======
    def tearDown(self):
        pass
        main(self.mock_stdscr)
        self.mock_stdscr.clear.assert_called_once()
        self.mock_typing_practice.return_value.start_session.assert_called_once_with(b"mock_text")
        self.mock_typing_practice.return_value.end_session.assert_called_once_with(b"mock_typed_text")
    def tearDown(self):
        pass
    
    if __name__ == "__main__":
    unittest.main()
    =======
    def tearDown(self):
        pass
    
    def tearDown(self):
        pass
    
    def tearDown(self):
        pass
    
    if __name__ == "__main__":
    unittest.main()
        main(self.mock_stdscr)
        self.mock_stdscr.clear.assert_called_once()
        self.mock_typing_practice.return_value.start_session.assert_called_once_with(b"mock_text")
        self.mock_typing_practice.return_value.end_session.assert_called_once_with(b"mock_typed_text")
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
