from flask import request, jsonify
from .models import BookSchema, books
from .services import BookService
from marshmallow import ValidationError

# Initialize BookSchema for single and multiple book operations
book_schema = BookSchema()
books_schema = BookSchema(many=True)
# Initialize the book service with the in-memory books list
book_service = BookService(books)

def init_app_routes(app):
    """
    Initialize routes for the Flask application.

    :param app: The Flask application instance.
    """

    @app.route('/books/<int:book_id>', methods=['GET'])
    def get_book(book_id):
        """
        Endpoint to retrieve a book by its ID.
        Returns a JSON response with the book data or an error message if not found.
        """
        book = book_service.get_book_by_id(book_id)
        if book:
            return jsonify(book_schema.dump(book)), 200
        return jsonify({"error": "Book not found"}), 404

    @app.route('/books', methods=['POST'])
    def add_book():
        """
        Endpoint to add a new book.
        Validates and deserializes the incoming request data, adds the book, and returns it.
        """
        try:
            # Deserialize and validate the incoming book data
            data = book_schema.load(request.json)
            # Add the book using the service, which assigns an ID and timestamp
            added_book = book_service.add_book(data)
            # Serialize the added book's data for the response
            return jsonify(book_schema.dump(added_book)), 201
        except ValidationError as err:
            # Return validation error messages if validation fails
            return jsonify(err.messages), 400

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        """
        Endpoint to delete a book by its ID.
        Returns a success message if deleted, or an error message if not found.
        """
        deleted_book = book_service.delete_book(book_id)
        if deleted_book:
            # Return a success message if the book was successfully deleted
            return jsonify({"message": "Book deleted successfully"}), 200
        else:
            # Return an error message if no book was found with the given ID
            return jsonify({"error": "Book not found"}), 404
