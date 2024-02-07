from marshmallow import Schema, fields, validate

# A list representing a simple in-memory data store for books.
#  Each book is a dictionary with an 'id', 'title', 'author', and 'timestamp'.
# This is a placeholder for what would typically be persisted in a database.
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_date": "1925-04-10"},
    {"id": 2, "title": "1984", "author": "George Orwell", "publication_date": "1949-06-08"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_date": "1960-07-11"}
]



class BookSchema(Schema):
    """
    Schema for serializing and deserializing book data using Marshmallow.

    Attributes:
        id (Int): A unique identifier for the book, not required when adding a new book as it is generated automatically.
        title (Str): The title of the book, required field with a minimum length of 1 character.
        author (Str): The author of the book, required field with a minimum length of 1 character.
        timestamp (DateTime): The date and time when the book was added, automatically generated and not required for new books.

    The `dump_only` attribute for 'id' means it's only used for serializing, not deserializing.
    This schema ensures that only valid data is accepted when creating or updating books and
    formats the book data correctly when retrieving it from the data store.
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    author = fields.Str(required=True, validate=validate.Length(min=1))
    publication_date = fields.Date()

