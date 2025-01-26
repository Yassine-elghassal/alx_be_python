# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the book is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String Representation: Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official Representation: Returns a string that could recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
