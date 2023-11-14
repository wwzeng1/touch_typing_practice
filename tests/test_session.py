import unittest
import datetime
from typing import Dict
from touch_typing_practice.session import Session

class TestSession(unittest.TestCase):

    ## Test Initialization
    def test_init(self):
        session = Session("Hello World")
        self.assertEqual(session.text, "Hello World")
        self.assertIsNone(session.start_time)
        self.assertIsNone(session.end_time)
        self.assertEqual(session.typed_text, "")

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

    ## Test Calculate Statistics
    def test_calculate_statistics(self):
        session = Session("Hello World")
        session.start()
        session.end("Hello World")
        stats = session.calculate_statistics()
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
