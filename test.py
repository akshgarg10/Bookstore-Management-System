import unittest
import requests
import json
from multiprocessing import Process
from time import sleep
from main import app


class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        # Start the Flask app in a separate process
        self.process = Process(target=app.run, kwargs={"debug": False})
        self.process.start()
        # Give the server some time to start
        sleep(2)

    def tearDown(self):
        # Terminate the Flask app process
        self.process.terminate()

    def test_add_book_with_valid_token(self):
        base_url = "http://127.0.0.1:5000/api/addBook"
        headers = {"Authorization": f"Bearer mysecretkey"}

        # Sample book data
        book_data = {
            "title": "Sample Book",
            "author": "John Doe",
            "price": 20,
            "quantity": 30
        }

        response = requests.post(base_url, json=book_data, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("isbn", data)
        self.assertIn("title", data)
        self.assertIn("author", data)
        self.assertIn("price", data)
        self.assertIn("quantity", data)

    def test_add_book_with_invalid_token(self):
        base_url = "http://127.0.0.1:5000/api/addBook"
        headers = {"Authorization": "Bearer invalid_token"}

        # Sample book data
        book_data = {
            "title": "Sample Book",
            "author": "John Doe",
            "price": 20,
            "quantity": 30
        }

        response = requests.post(base_url, json=book_data, headers=headers)
        self.assertEqual(response.status_code, 401)

    def test_get_all_books_with_valid_token(self):
        base_url = "http://127.0.0.1:5000/api/getAllBooks"
        headers = {"Authorization": f"Bearer mysecretkey"}

        response = requests.get(base_url, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("books", data)
        self.assertIsInstance(data["books"], list)

    def test_get_all_books_with_invalid_token(self):
        base_url = "http://127.0.0.1:5000/api/getAllBooks"
        headers = {"Authorization": "Bearer invalid_token"}

        response = requests.get(base_url, headers=headers)
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()
