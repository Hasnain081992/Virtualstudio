import unittest
from unittest.mock import patch
from practice import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch('practice.fetch_data')
    def test_get_data_empty(self, mock_fetch_data):
        # Mock fetch_data to return an empty list
        mock_fetch_data.return_value = []
        response = self.client.get('/get_data')
        self.assertEqual(response.status_code, 500)  # Expect 500 due to error
        self.assertEqual(response.get_json(), {"error": "Unable to fetch data from database"})

    @patch('practice.fetch_data')
    def test_get_data_success(self, mock_fetch_data):
        # Mock fetch_data to return sample data
        mock_fetch_data.return_value = [
            {"id": 1, "name": "Alice", "age": 30, "department": "HR"},
            {"id": 2, "name": "Bob", "age": 40, "department": "Finance"}
        ]
        response = self.client.get('/get_data')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data, mock_fetch_data.return_value)

