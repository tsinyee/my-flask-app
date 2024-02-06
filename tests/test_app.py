import unittest
from app import create_app
from app.models import books

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Creates a test client
        self.app = create_app().test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

        # Setup your data here
        self.test_book = {"title": "Test Book", "author": "Test Author"}

    def tearDown(self):
        # Clear the books list after each test
        books.clear()

    def test_add_book(self):
        # Send a POST request
        response = self.app.post('/books', json=self.test_book)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Book', str(response.data))

    def test_get_book(self):
        # Add a book first
        self.app.post('/books', json=self.test_book)
        # Attempt to fetch the added book
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', str(response.data))

    def test_delete_book(self):
        # Add a book first
        self.app.post('/books', json=self.test_book)
        # Attempt to delete the added book
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)
        # Verify the book is deleted
        get_response = self.app.get('/books/1')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
