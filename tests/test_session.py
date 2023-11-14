import datetime
from typing import Dict
from touch_typing_practice.session import Session

class TestSession:

    ## Test Initialization
    def test_init(self):
        session = Session("Hello World")
        assert session.text == "Hello World"
        assert session.start_time is None
        assert session.end_time is None
        assert session.typed_text == ""

    ## Test Start
    def test_start(self):
        session = Session("Hello World")
        session.start()
        self.assertIsNotNone(session.start_time)
        self.assertIsInstance(session.start_time, datetime.datetime)

    ## Test End
    def test_end(self):
        session = Session("Hello World")
        session.start()
        session.end("Hello World")
        self.assertIsNotNone(session.end_time)
        self.assertIsInstance(session.end_time, datetime.datetime)
        self.assertEqual(session.typed_text, "Hello World")

    ## Test Start
    def test_start(self):
        session = Session("Hello World")
        session.start()
        assert session.start_time is not None
        assert isinstance(session.start_time, datetime.datetime)

    ## Test End
    def test_end(self):
    def test_calculate_statistics(self):
        session = Session("Hello World")
        session.start()
        session.end("Hello World")
        assert session.end_time is not None
        assert isinstance(session.end_time, datetime.datetime)
        assert session.typed_text == "Hello World"
    
    ## Test Calculate Statistics
    def test_calculate_statistics(self):
        self.assertIsInstance(stats, Dict)
        self.assertIn('start_time', stats)
        self.assertIn('end_time', stats)
        self.assertIn('time_taken', stats)
        self.assertIn('characters_typed', stats)
        self.assertIn('words_typed', stats)
        self.assertIn('speed', stats)
        self.assertIn('accuracy', stats)
        self.assertEqual(stats['characters_typed'], len("Hello World"))
        self.assertEqual(stats['words_typed'], len("Hello World".split()))
        self.assertEqual(stats['accuracy'], 100.0)

    ## Test Calculate Statistics with incorrect input
    def test_calculate_statistics_incorrect_input(self):
        session = Session("Hello World")
        session.start()
        session.end("Hello World")
        stats = session.calculate_statistics()
        assert isinstance(stats, Dict)
        assert 'start_time' in stats
        assert 'end_time' in stats
        assert 'time_taken' in stats
        assert 'characters_typed' in stats
        assert 'words_typed' in stats
        assert 'speed' in stats
        assert 'accuracy' in stats
        assert stats['characters_typed'] == len("Hello World")
        assert stats['words_typed'] == len("Hello World".split())
        assert stats['accuracy'] == 100.0

    ## Test Calculate Statistics with incorrect input
    def test_calculate_statistics_incorrect_input(self):
        session = Session("Hello World")
        session.start()
        session.end("Hello Wrld")
        stats = session.calculate_statistics()
        assert isinstance(stats, Dict)
        assert 'start_time' in stats
        assert 'end_time' in stats
        assert 'time_taken' in stats
        assert 'characters_typed' in stats
        assert 'words_typed' in stats
        assert 'speed' in stats
        assert 'accuracy' in stats
        assert stats['characters_typed'] == len("Hello Wrld")
        assert stats['words_typed'] == len("Hello Wrld".split())
        assert stats['accuracy'] != 100.0
        session.end("Hello Wrld")
        stats = session.calculate_statistics()
        self.assertIsInstance(stats, Dict)
        self.assertIn('start_time', stats)
        self.assertIn('end_time', stats)
        self.assertIn('time_taken', stats)
        self.assertIn('characters_typed', stats)
        self.assertIn('words_typed', stats)
        self.assertIn('speed', stats)
        self.assertIn('accuracy', stats)
        self.assertEqual(stats['characters_typed'], len("Hello Wrld"))
        self.assertEqual(stats['words_typed'], len("Hello Wrld".split()))
        self.assertNotEqual(stats['accuracy'], 100.0)

if __name__ == '__main__':
    unittest.main()
