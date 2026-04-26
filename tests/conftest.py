import os
import sys
import pytest

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from model.database import init_database, get_connection
from config import TEST_DATABASE_PATH


@pytest.fixture(autouse=True)
def setup_database():
    """Setup test database before each test"""
    # Remove old test db if exists
    if os.path.exists(TEST_DATABASE_PATH):
        os.remove(TEST_DATABASE_PATH)

    init_database(TEST_DATABASE_PATH)
    yield

    # Cleanup
    if os.path.exists(TEST_DATABASE_PATH):
        os.remove(TEST_DATABASE_PATH)


@pytest.fixture
def db_path():
    return TEST_DATABASE_PATH
