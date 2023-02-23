import pytest
import sys;
sys.path.insert(1,"C:\\Users\\nicol\\OneDrive\\Documents\\Professionnel\\Ynov\\E2-Tests\\tp-tests-unitaires-api\\app")

from app import app

@pytest.fixture
def client():
    app.app.testing = True
    client = app.app
    yield client.test_client()

@pytest.fixture
def new_user1():
    user = {
        'id':1,'name': 'Paul', 'age': 20
    }
    return user

@pytest.fixture
def new_user2():
    user = {
        'id':2,'name': 'Pierre', 'age': 30
    }
    return user

@pytest.fixture
def update_user():
    user = {
        'id':1,'name': 'Jean', 'age': 23
    }
    return user