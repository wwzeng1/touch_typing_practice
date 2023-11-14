## test_user.py
import unittest
import os
import json
from datetime import datetime
from touch_typing_practice.user import User
from touch_typing_practice.session import Session

class TestUser(unittest.TestCase):
    ## Test User Initialization
    def test_init(self):
        user = User('testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.history, {})

    ## Test Session Recording
    def test_record_session(self):
        user = User('testuser')
        session = Session('test')  # Corrected the number of arguments passed to Session
        user.record_session(session)
        self.assertEqual(len(user.history), 1)

    ## Test Statistics Retrieval
    def test_get_statistics(self):
        user = User('testuser')
        session = Session('test')  # Corrected the number of arguments passed to Session
        user.record_session(session)
        stats = user.get_statistics()
        self.assertEqual(len(stats), 1)

    ## Test User Save
    def test_save(self):
        user = User('testuser')
        session = Session('test')  # Corrected the number of arguments passed to Session
        user.record_session(session)
        user.save()
        self.assertTrue(os.path.isfile('testuser.json'))

    ## Test User Load
    def test_load(self):
        user = User('testuser')
        session = Session('test')  # Corrected the number of arguments passed to Session
        user.record_session(session)
        user.save()
        loaded_user = User.load('testuser')
        self.assertEqual(loaded_user.username, 'testuser')
        self.assertEqual(loaded_user.history, user.history)

    ## Test Load Non-Existent User
    def test_load_non_existent(self):
        loaded_user = User.load('non_existent_user')
        self.assertEqual(loaded_user.username, 'non_existent_user')
        self.assertEqual(loaded_user.history, {})

    ## Clean up after tests
    @classmethod
    def tearDownClass(cls):
        if os.path.isfile('testuser.json'):
            os.remove('testuser.json')

if __name__ == '__main__':
    unittest.main()
