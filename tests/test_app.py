import unittest
from app import create_app
from app.models import books


class FlaskTestCase(unittest.TestCase):
    """
    A test case class for testing the Flask application endpoints.

    This class includes test methods for adding, getting, and deleting books from the backend API.

    Attributes:
        app: The test client for the Flask application.
        test_book: A dictionary representing a test book data used for testing.

    Methods:
        setUp(): Initializes the test client and test data before each test method.
        tearDown(): Clears the books list after each test method.
        test_add_book(): Tests the endpoint for adding a new book to the backend API.
        test_get_book(): Tests the endpoint for retrieving a book from the backend API.
        test_delete_book(): Tests the endpoint for deleting a book from the backend API.

    """

    def setUp(self):
        """
        Initializes the test client and test data before each test method.
        """
        # Creates a test client
        self.app = create_app().test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

        # Setup your data here
        self.test_book = {"title": "Test Book", "author": "Test Author", "publication_date": "2024-02-06"}

    def tearDown(self):
        """
        Clears the books list after each test method.
        """
        # Clear the books list after each test
        books.clear()

    def test_add_book(self):
        """
        Tests the endpoint for adding a new book to the backend API.
        """
        # Send a POST request
        response = self.app.post('/books', json=self.test_book)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Book', str(response.data))

    def test_get_book(self):
        """
        Tests the endpoint for retrieving a book from the backend API.
        """
        # Add a book first
        self.app.post('/books', json=self.test_book)
        # Attempt to fetch the added book
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', str(response.data))

    def test_delete_book(self):
        """
        Tests the endpoint for deleting a book from the backend API.
        """
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
