from datetime import datetime, timezone

class BookService:
    """
    A service class for managing books in an in-memory data store.

    This class provides methods to add, retrieve by ID, and delete books
    from a provided data store. Each book is represented as a dictionary
    within the data store list.

    Attributes:
        data_store (list): A list of dictionaries, where each dictionary represents a book.
                           Books are stored with 'id', 'title', 'author', and 'timestamp' keys.
    """
    def __init__(self, data_store):
        """
        Initialize the BookService with a data store.

        :param data_store: A list that acts as the in-memory database for books.
        """
        self.data_store = data_store

    def add_book(self, book_data):
        """
        Adds a new book to the data store with a unique ID and current timestamp.

        Assumes book_data is already validated and contains 'title' and 'author'.
        Automatically assigns a new unique ID and the current timestamp to the book.

        :param book_data: A dictionary containing 'title' and 'author' of the book.
        :return: The newly added book, including its 'id' and 'timestamp'.
        """
        new_id = max(book['id'] for book in self.data_store) + 1 if self.data_store else 1
        book_data['id'] = new_id
        self.data_store.append(book_data)
        return book_data

    def get_book_by_id(self, book_id):
        """
        Retrieves a book by its ID from the data store.

        :param book_id: The unique identifier of the book to find.
        :return: The book with the matching ID, or None if no match is found.
        """
        return next((book for book in self.data_store if book['id'] == book_id), None)

    def delete_book(self, book_id):
        """
        Deletes a book by its ID from the data store.

        :param book_id: The unique identifier of the book to delete.
        :return: The deleted book if found and removed, None otherwise.
        """
        book_to_delete = self.get_book_by_id(book_id)
        if book_to_delete:
            self.data_store.remove(book_to_delete)
            return book_to_delete
        return None
