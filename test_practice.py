import unittest
from practice import app, engine
from sqlalchemy import text

class TestFlaskApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        This runs once before all tests. Set up the test database.
        """
        cls.connection = engine.connect()
        
        # Create the table and add mock data
        cls.connection.execute(text("""
            CREATE TABLE IF NOT EXISTS employee (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INTEGER,
                department VARCHAR(50)
            )
        """))
        cls.connection.execute(text("""
            INSERT INTO employee (name, age, department)
            VALUES ('Alice', 30, 'HR'), ('Bob', 40, 'Finance')
        """))
