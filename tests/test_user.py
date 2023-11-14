## test_user.py
import os
import json
import pytest
from datetime import datetime
from touch_typing_practice.user import User
from touch_typing_practice.session import Session

class TestUser:
    ## Test User Initialization
    def test_init(self):
        user = User('testuser')
        assert user.username == 'testuser'
        assert user.history == {}

    ## Test Session Recording
    def test_record_session(self):
        user = User('testuser')
        session = Session('test')  # Corrected the number of arguments passed to Session
        user.record_session(session)
        assert len(user.history) == 1

    ## Test Statistics Retrieval
    def test_get_statistics(self):
        user = User('testuser')
        session = Session('test')  # Corrected the number of arguments passed to Session
        user.record_session(session)
        stats = user.get_statistics()
        assert len(stats) == 1

    ## Test User Save
    def test_save(self, user_and_cleanup):
        user = user_and_cleanup
        assert os.path.isfile('testuser.json')

    def test_load(self, user_and_cleanup):
        user = user_and_cleanup
        loaded_user = User.load('testuser')
        assert loaded_user.username == 'testuser'
        assert loaded_user.history == user.history

    ## Test Load Non-Existent User
    def test_load_non_existent(self):
        loaded_user = User.load('non_existent_user')
        assert loaded_user.username == 'non_existent_user'
        assert loaded_user.history == {}
@pytest.fixture
def user_and_cleanup():
    user = User('testuser')
    session = Session('test')
    user.record_session(session)
    user.save()
    yield user
    if os.path.isfile('testuser.json'):
        os.remove('testuser.json')
    def test_load(self, user_and_cleanup):
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
